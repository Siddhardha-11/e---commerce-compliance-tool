from typing import List, Dict
from datetime import datetime

from models import ProductData, ScanResult, Violation as ModelViolation
from rules import RULES
from scraper import scrape_product


# 🔹 PUBLIC ENTRY POINT
def evaluate_url(url: str) -> ScanResult:
    """
    SINGLE ENTRY POINT
    main.py should call ONLY this
    """
    print(f"🔍 Scraping product from URL: {url}")
    product = scrape_product(url)

    print("⚖️ Running compliance evaluation...")
    return evaluate_compliance(product)


def evaluate_compliance(product: ProductData) -> ScanResult:
    """
    MAIN FUNCTION – evaluates scraped ProductData
    """
    violations_data = []

    relevant_rules = _get_relevant_rules(product)

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


def _get_relevant_rules(product: ProductData) -> List[Dict]:
    """
    Filter rules to general e-commerce rules only
    """
    core_rule_ids = ["EC-01", "EC-04", "EC-06", "EC-07", "EC-09"]
    selected = []

    for rule in RULES:
        if rule["id"] in core_rule_ids or rule["category"] == "all":
            selected.append(rule)

    return selected[:8]


def _check_rule_against_product(rule: Dict, product: ProductData) -> Dict | None:
    """
    Maps ProductData → rule required_fields
    ONLY uses fields that scraper actually provides
    """

    field_mapping = {
        "seller": product.seller,
        "price": product.price,
        "description": product.description,
        "returns": product.returns,
        "technical_details": getattr(product, "technical_details", None),
    }

    missing_fields = []

    for required_field in rule.get("required_fields", []):
        value = field_mapping.get(required_field)

        if value is None:
            missing_fields.append(required_field)
        elif isinstance(value, str) and not value.strip():
            missing_fields.append(required_field)

    if missing_fields:
        return {
            "rule_id": rule["id"],
            "severity": rule["severity"],
            "description": f"{rule['title']} [{rule['law']}]",
            "suggestion": f"Display {', '.join(missing_fields)} clearly on product page"
        }

    return None


def _calculate_risk_score(violations_data: List[Dict]) -> int:
    """
    Maps violations → risk score (1–10)
    """
    if not violations_data:
        return 1

    weights = {"HIGH": 3, "MEDIUM": 2, "LOW": 1}
    total = sum(weights.get(v["severity"], 1) for v in violations_data)

    avg = total / len(violations_data)
    return min(10, max(1, int(avg * 2.5)))
