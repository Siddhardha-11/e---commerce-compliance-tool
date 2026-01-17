from typing import List, Dict, Any
import re

from rules import RULES
from models import ProductData
from ai_extractor import ai_parse_technical_details


# --------------------------------------------------
# RULE CONTROL
# --------------------------------------------------

SKIPPED_RULE_IDS = {
    "EC-02", "EC-03", "EC-05", "EC-07", "EC-09",
    "EC-11", "EC-12", "EC-15", "EC-ENV-01",
    "EC-08-AMEND",
    "CS-07", "CS-08",
}

ADVISORY_RULE_IDS = {
    "EC-10", "CS-05", "CS-06",
}

UNVERIFIABLE_FIELDS = {
    "ingredients", "expiry", "batch_no",
    "cruelty_free_cert", "epr_registration_no",
}


# --------------------------------------------------
# FIELD ALIASES
# --------------------------------------------------

FIELD_ALIASES = {
    "brand": ["brand"],
    "manufacturer": ["manufacturer"],
    "origin": ["origin_country"],
    "origin_country": ["origin_country"],
    "usage": ["usage"],
    "description": ["description"],
    "returns": ["returns"],
    "delivery": ["delivery"],
    "price": ["price"],
}


# --------------------------------------------------
# HELPERS
# --------------------------------------------------

def _field_exists(product: ProductData, field: str) -> bool:
    # 🔹 Special case: quantity inferred from title
    if field == "quantity":
        title = (product.title or "").lower()
        return bool(re.search(r"\d+\s?(ml|l|g|kg)", title))

    for attr in FIELD_ALIASES.get(field, [field]):
        val = getattr(product, attr, None)
        if val not in (None, "", [], {}):
            return True

    return False


def _infer_from_title(product: ProductData) -> None:
    title = (product.title or "").lower()

    # Brand inference
    if not product.brand and title:
        product.brand = title.split()[0]

    # Usage inference
    if not product.usage:
        if any(k in title for k in ["lotion", "cream", "moistur"]):
            product.usage = "skin application"


def _enrich_product_with_ai(product: ProductData) -> None:
    if not product.technical_details:
        _infer_from_title(product)
        return

    parsed = ai_parse_technical_details(product.technical_details)

    for k, v in parsed.items():
        if hasattr(product, k) and getattr(product, k) in (None, "", []):
            setattr(product, k, v)

    _infer_from_title(product)


# --------------------------------------------------
# MAIN ENGINE
# --------------------------------------------------

def evaluate_compliance(product: ProductData) -> Dict[str, Any]:
    _enrich_product_with_ai(product)

    violations: List[Dict[str, Any]] = []
    risk_score = 100

    for rule in RULES:
        rule_id = rule["id"]

        if rule_id in SKIPPED_RULE_IDS:
            continue

        rule_category = rule.get("category", "all")
        if rule_category not in ("all", None, product.category):
            continue

        missing = []
        for field in rule.get("required_fields", []):
            if field in UNVERIFIABLE_FIELDS:
                continue
            if not _field_exists(product, field):
                missing.append(field)

        if not missing:
            continue

        if rule_id in ADVISORY_RULE_IDS:
            violations.append({
                "rule_id": rule_id,
                "severity": "LOW",
                "description": f"{rule['title']} (advisory)",
                "suggestion": rule.get("suggestion", ""),
            })
            continue

        violations.append({
            "rule_id": rule_id,
            "severity": rule["severity"],
            "description": f"{rule['title']} – missing: {', '.join(missing)}",
            "suggestion": rule.get("suggestion", ""),
        })

        risk_score -= {"HIGH": 20, "MEDIUM": 10, "LOW": 5}.get(
            rule["severity"], 0
        )

    return {
        "risk_score": max(0, risk_score),
        "violations": violations,
    }


# --------------------------------------------------
# BACKWARD COMPATIBILITY
# --------------------------------------------------

def infer_product_category(product: ProductData) -> str:
    text = f"{product.title or ''} {product.usage or ''}".lower()
    if any(k in text for k in ["lotion", "cream", "cosmetic", "skin"]):
        return "cosmetics"
    return "general"
