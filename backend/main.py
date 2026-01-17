from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from datetime import datetime

from models import ScanRequest, ScanResult, ProductData, Violation
from database import get_db, init_db, ScanRecord
from rules import RULES


# -------------------------------------------------
# App Initialization
# -------------------------------------------------
app = FastAPI(
    title="SafeBuy – E-commerce Compliance API",
    description="Automated compliance & dark-pattern detection for e-commerce listings",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup():
    init_db()


# -------------------------------------------------
# Utility Functions
# -------------------------------------------------
def build_field_index(product: ProductData) -> dict:
    tech = (product.technical_details or "").lower()

    return {
        # general
        "seller": bool(product.seller),
        "price": bool(product.price),
        "returns": bool(product.returns),
        "delivery": bool(product.delivery),
        "title": bool(product.title),
        "brand": bool(product.brand) or "brand" in tech,
        "description": bool(product.description or tech),
        "origin": "country of origin" in tech,
        "grievance": "grievance" in tech,
        "images": True,

        # electronics
        "warranty": bool(product.warranty) or "warranty" in tech,
        "specifications": bool(product.technical_details),
        "model_number": "model" in tech,
        "voltage": "volt" in tech,
        "energy_rating": "star" in tech,

        # food
        "expiry": "expiry" in tech or "best before" in tech,
        "ingredients": "ingredients" in tech,
        "fssai": "fssai" in tech,
        "nutrition": "nutrition" in tech,

        # health
        "dosage": "dosage" in tech,
        "disclaimer": "disclaimer" in tech,
        "warning": "warning" in tech,
    }


def run_compliance_check(product: ProductData) -> dict:
    # 🔥 Lazy imports (VERY IMPORTANT)
    from evaluator import infer_product_category

    category = infer_product_category(product)
    field_index = build_field_index(product)

    violations: list[Violation] = []

    for rule in RULES:
        rule_category = rule.get("category", "all")

        if rule_category != "all" and rule_category != category:
            continue

        missing = [
            f for f in rule.get("required_fields", [])
            if not field_index.get(f, False)
        ]

        if missing:
            violations.append(
                Violation(
                    rule_id=rule["id"],
                    severity=rule["severity"],
                    description=f"{rule['title']} – missing: {', '.join(missing)}",
                    suggestion=f"Ensure disclosure of: {', '.join(missing)}",
                )
            )

    score = 100
    for v in violations:
        score -= {"HIGH": 20, "MEDIUM": 10, "LOW": 5}.get(v.severity.upper(), 0)

    return {
        "category": category,
        "score": max(0, score),
        "violations": violations,
    }


def compute_trust_index(product: ProductData, violations: list[Violation]) -> dict:
    tech = (product.technical_details or "").lower()
    score = 100
    reasons = []

    if "country of origin" not in tech:
        score -= 15
        reasons.append("Country of origin not disclosed.")

    if not product.seller:
        score -= 10
        reasons.append("Seller information missing.")

    if not product.returns:
        score -= 15
        reasons.append("Returns policy unclear.")

    for v in violations:
        score -= {"HIGH": 10, "MEDIUM": 5}.get(v.severity.upper(), 0)

    return {
        "score": max(0, min(score, 100)),
        "reasons": reasons,
    }


# -------------------------------------------------
# Routes
# -------------------------------------------------
@app.get("/")
def root():
    return {
        "service": "SafeBuy Compliance API",
        "status": "running",
        "docs": "/docs",
        "endpoints": ["/scan", "/history"],
    }


@app.post("/scan", response_model=ScanResult)
def scan_product(request: ScanRequest, db: Session = Depends(get_db)):
    # 🔥 Lazy imports
    from scraper import scrape_product, _fetch_html
    from dark_patterns import detect_dark_patterns

    url = request.url

    html = _fetch_html(url)
    product = scrape_product(url)

    compliance = run_compliance_check(product)
    base_violations = compliance["violations"]

    dark_findings = detect_dark_patterns(product, html)
    dark_violations = [
        Violation(
            rule_id=f.code,
            severity=f.severity,
            description=f.message,
            suggestion="Review pricing/UX for dark patterns.",
        )
        for f in dark_findings
    ]

    all_violations = base_violations + dark_violations

    risk_score = 100
    for v in all_violations:
        risk_score -= {"HIGH": 20, "MEDIUM": 10, "LOW": 5}.get(v.severity.upper(), 0)

    trust_index = compute_trust_index(product, all_violations)

    result = ScanResult(
        timestamp=datetime.utcnow(),
        product=product,
        risk_score=max(0, risk_score),
        violations=all_violations,
        trust_index=trust_index,
    )

    record = ScanRecord(
        url=url,
        risk_score=result.risk_score,
        product_data=product.dict(exclude={"timestamp"}),
        violations_data=[v.dict() for v in result.violations],
    )

    db.add(record)
    db.commit()
    db.refresh(record)
    result.id = record.id

    return result


@app.get("/history")
def scan_history(db: Session = Depends(get_db)):
    return db.query(ScanRecord).order_by(ScanRecord.timestamp.desc()).all()
