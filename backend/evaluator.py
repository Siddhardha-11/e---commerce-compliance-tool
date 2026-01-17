from typing import List, Dict
from datetime import datetime

from models import ProductData, ScanResult, Violation as ModelViolation
from rules import RULES
from scraper import scrape_product


# =====================================================
# PUBLIC ENTRY POINT
# =====================================================

def evaluate_url(url: str) -> ScanResult:
    """
    Main entry point.
    main.py or API should call ONLY this.
    """
    print(f"🔍 Scraping product: {url}")
    product = scrape_product(url)

    print("⚖️ Evaluating compliance...")
    return evaluate_compliance(product)


# =====================================================
# CORE EVALUATION
# =====================================================

def evaluate_compliance(product: ProductData) -> ScanResult:
    violations_data = []

    relevant_rules = _get_relevant_rules()

    for rule in relevant_rules:
        violation = _check_rule_against_product(rule, product)
        if violation:
            violations_data.append(violation)

    risk_score = _calculate_risk_score(violations_data)

    model_violations = [
        ModelViolation(
            rule_id=v["rule_id"],
            severity=v["severity"],
            description=v["description"],
            suggestion=v["suggestion"]
        )
        for v in violations_data
    ]

    return ScanResult(
        id=None,
        timestamp=datetime.now(),
        product=product,
        risk_score=risk_score,
        violations=model_violations
    )


# =====================================================
# RULE SELECTION
# =====================================================

def _get_relevant_rules() -> List[Dict]:
    """
    For now, apply only GENERAL E-COMMERCE rules.
    (Food / Health / Electronics can be added later)
    """
    return [
        r for r in RULES
        if r["category"] == "all"
    ]


# RULE CHECKING

def _check_rule_against_product(rule: Dict, product: ProductData) -> Dict | None:
    """
    Checks ONE rule against scraped ProductData.
    Only validates fields that scraper actually provides.
    """

    # Map rule keywords → actual ProductData fields
    field_mapping = {
        "title": product.title,
        "seller": product.seller,
        "price": product.price,
        "returns": product.returns,
        "description": product.description,
        "technical_details": product.technical_details,
        "brand": product.brand,
        "delivery": product.delivery,
        "warranty": product.warranty,
    }

    missing_fields = []

    for required_field in rule.get("required_fields", []):

        # If evaluator doesn’t support this field yet, skip it
        if required_field not in field_mapping:
            continue

        value = field_mapping.get(required_field)

        # Missing or empty
        if value is None:
            missing_fields.append(required_field)
        elif isinstance(value, str) and not value.strip():
            missing_fields.append(required_field)

    if missing_fields:
        return {
            "rule_id": rule["id"],
            "severity": rule["severity"],
            "description": f"{rule['title']} [{rule['law']}]",
            "suggestion": (
                f"Ensure {', '.join(missing_fields)} "
                f"is clearly displayed on the product page"
            )
        }

    return None




def _calculate_risk_score(violations_data: List[Dict]) -> int:
    if not violations_data:
        return 1

    severity_weights = {"HIGH": 3, "MEDIUM": 2, "LOW": 1}
    total = sum(severity_weights.get(v["severity"], 1) for v in violations_data)

    avg = total / len(violations_data)
    return min(10, max(1, int(avg * 2.5)))
