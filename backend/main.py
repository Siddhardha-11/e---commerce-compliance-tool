from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from scraper import scrape_product, _fetch_html
from dark_patterns import detect_dark_patterns
from datetime import datetime

from models import ScanRequest, ScanResult, ProductData, Violation
from database import get_db, init_db, ScanRecord
from rules import RULES  # your RULES list


app = FastAPI(title="Compliance API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup():
    init_db()


def build_field_index(product: ProductData) -> dict:
    """
    Build a flat field index so rules like required_fields=["warranty","origin"]
    can be checked against product + technical_details text.
    """
    tech = (product.technical_details or "").lower()

    # Base mapping from rule field keys to data
    field_values: dict[str, bool] = {
        "seller": bool(product.seller),
        "seller_contact": False,         # you can extend when you parse these
        "seller_address": False,         # from technical_details or extra fields
        "price": bool(product.price),
        "charges": "convenience fee" in tech or "handling fee" in tech,
        "returns": bool(product.returns),
        "delivery": bool(product.delivery),
        "origin": "country of origin" in tech,
        "grievance": "grievance" in tech,
        "description": bool(getattr(product, "description", None) or tech),
        "reviews": "reviews" in tech or "rating" in tech,
        "title": bool(product.title),
        "brand": bool(product.brand) or "brand name" in tech,
        "quantity": "net quantity" in tech or "unit count" in tech,
        "images": True,  # assume True unless you explicitly track images
        # electronics
        "warranty": bool(product.warranty) or "warranty" in tech,
        "specifications": bool(product.technical_details),
        "voltage": "volt" in tech or "w" in tech,
        "safety": "safety" in tech or "warning" in tech,
        "energy_rating": "star" in tech or "energy" in tech,
        "model_number": "model" in tech,
        "compatibility": "compatible" in tech,
        # food
        "expiry": "expiry" in tech or "best before" in tech,
        "ingredients": "ingredients" in tech,
        "fssai": "fssai" in tech,
        "allergen": "allergen" in tech,
        "veg_nonveg": "vegetarian" in tech or "non-vegetarian" in tech,
        "storage": "store in" in tech or "storage" in tech,
        "manufacturer": "manufacturer" in tech,
        "nutrition": "nutrition" in tech or "nutritional" in tech,
        # health
        "disclaimer": "disclaimer" in tech,
        "dosage": "dosage" in tech or "dose" in tech,
        "guaranteed": "guaranteed" in tech,
        "100%": "100%" in tech,
        "usage": "usage" in tech or "use:" in tech,
        "warning": "warning" in tech,
        "age_limit": "age" in tech,
        "prescription_required": "prescription" in tech,
    }

    return field_values


def run_compliance_check(product: ProductData) -> dict:
    """
    Apply RULES from rules.py to the product.
    A rule is violated if any of its required_fields is missing/False.
    """
    field_values = build_field_index(product)
    violations: list[Violation] = []

    for rule in RULES:
        rule_id = rule["id"]
        severity = rule["severity"]
        title = rule["title"]
        required_fields = rule.get("required_fields", [])

        # Check if all required fields are satisfied
        missing = []
        for f in required_fields:
            if not field_values.get(f, False):
                missing.append(f)

        if missing:
            description = f"{title} – missing or unclear: {', '.join(missing)}"
            suggestion = f"Ensure the following field(s) are clearly disclosed: {', '.join(missing)}."
            violations.append(
                Violation(
                    rule_id=rule_id,
                    severity=severity,
                    description=description,
                    suggestion=suggestion,
                )
            )

    # Compute score from rule-based violations
    score = 100
    for v in violations:
        if v.severity.upper() == "HIGH":
            score -= 20
        elif v.severity.upper() == "MEDIUM":
            score -= 10
        elif v.severity.upper() == "LOW":
            score -= 5

    score = max(0, score)
    return {"score": score, "violations": violations}


def compute_trust_index(product: ProductData, violations: list[Violation]) -> dict:
    score = 100
    reasons: list[str] = []

    tech = (product.technical_details or "").lower()

    # Basic transparency signals
    if "country of origin" not in tech:
        score -= 15
        reasons.append("Country of origin not found in technical details.")

    if not product.seller:
        score -= 10
        reasons.append("Seller name missing.")

    if not product.returns:
        score -= 15
        reasons.append("No returns information visible.")

    if not product.warranty and "warranty" not in tech:
        score -= 10
        reasons.append("Warranty not specified.")

    if not product.price or getattr(product.price, "deal", None) is None:
        score -= 20
        reasons.append("Deal price not clearly extracted.")

    # Penalize based on violations
    for v in violations:
        if v.severity.upper() == "HIGH":
            score -= 10
        elif v.severity.upper() == "MEDIUM":
            score -= 5

    score = max(0, min(score, 100))
    return {"score": score, "reasons": reasons}


@app.post("/scan", response_model=ScanResult)
def scan_endpoint(request: ScanRequest, db: Session = Depends(get_db)):
    url = request.url

    # 1. Scrape real product data
    html = _fetch_html(url)
    product = scrape_product(url)

    # 2. Rule-based compliance using rules.py
    compliance_result = run_compliance_check(product)
    base_violations = compliance_result["violations"]

    # 3. Dark-pattern detection
    dark_findings = detect_dark_patterns(product, html)
    dark_violations: list[Violation] = [
        Violation(
            rule_id=f.code,
            severity=f.severity,
            description=f.message,
            suggestion="Review pricing/UX for potential dark pattern.",
        )
        for f in dark_findings
    ]

    # 4. Merge violations
    all_violations = base_violations + dark_violations

    # 4.1 Recompute risk score from all violations (rules + dark patterns)
    risk = 100
    for v in all_violations:
        if v.severity.upper() == "HIGH":
            risk -= 20
        elif v.severity.upper() == "MEDIUM":
            risk -= 10
        elif v.severity.upper() == "LOW":
            risk -= 5
    risk = max(0, risk)

    # 4.5 Compute trust index
    trust_index = compute_trust_index(product, all_violations)

    # 5. Build result
    result = ScanResult(
        timestamp=datetime.utcnow(),
        product=product,
        risk_score=risk,
        violations=all_violations,
        trust_index=trust_index,
    )

    # 6. Save to DB (avoid datetime in JSON)
    product_dict = product.dict()
    product_dict.pop("timestamp", None)

    db_record = ScanRecord(
        url=url,
        risk_score=result.risk_score,
        product_data=product_dict,
        violations_data=[v.dict() for v in result.violations],
    )
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    result.id = db_record.id

    return result


@app.get("/history")
def get_history(db: Session = Depends(get_db)):
    return db.query(ScanRecord).order_by(ScanRecord.timestamp.desc()).all()
