from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from datetime import datetime

from models import ScanRequest, ScanResult, ProductData, Violation
from database import get_db, init_db, ScanRecord

# IMPORTANT: evaluator is now the ONLY compliance engine
from evaluator import evaluate_compliance, infer_product_category
from fastapi.responses import StreamingResponse
from report_generator import generate_pdf_report

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

@app.post("/download-report")
def download_report(result: dict):
    pdf = generate_pdf_report(result)

    return StreamingResponse(
        pdf,
        media_type="application/pdf",
        headers={
            "Content-Disposition": "attachment; filename=safebuy_report.pdf"
        }
    )
# -------------------------------------------------
# Trust Index (kept simple & realistic)
# -------------------------------------------------
def compute_trust_index(product: ProductData, violations: list[Violation]) -> dict:
    score = 100
    reasons = []

    if not product.seller:
        score -= 10
        reasons.append("Seller information missing.")

    if not product.returns:
        score -= 10
        reasons.append("Returns policy unclear.")

    if not product.origin_country:
        score -= 10
        reasons.append("Country of origin not disclosed.")

    for v in violations:
        score -= {"HIGH": 5, "MEDIUM": 3}.get(v.severity.upper(), 0)

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
    # Lazy imports (avoid circular deps)
    from scraper import scrape_product, _fetch_html
    from dark_patterns import detect_dark_patterns

    url = request.url

    # 1️⃣ Fetch & scrape
    html = _fetch_html(url)
    product = scrape_product(url)

    # 2️⃣ Category inference (lightweight)
    product.category = infer_product_category(product)

    # 3️⃣ Compliance evaluation (ONLY evaluator.py)
    compliance_result = evaluate_compliance(product)
    base_violations = [
        Violation(**v) for v in compliance_result["violations"]
    ]

    # 4️⃣ Dark pattern detection (separate system)
    dark_findings = detect_dark_patterns(product, html)
    dark_violations = [
        Violation(
            rule_id=f.code,
            severity=f.severity,
            description=f.message,
            suggestion="Review pricing/UX for potential dark patterns.",
        )
        for f in dark_findings
    ]

    # 5️⃣ Merge violations
    all_violations = base_violations + dark_violations

    # 6️⃣ Risk score (single source)
    risk_score = compliance_result["risk_score"]
    for v in dark_violations:
        risk_score -= {"HIGH": 20, "MEDIUM": 10, "LOW": 5}.get(v.severity.upper(), 0)

    risk_score = max(0, risk_score)

    # 7️⃣ Trust index
    trust_index = compute_trust_index(product, all_violations)

    # 8️⃣ Build response
    result = ScanResult(
        timestamp=datetime.utcnow(),
        product=product,
        risk_score=risk_score,
        violations=all_violations,
        trust_index=trust_index,
    )

    # 9️⃣ Persist to DB
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
