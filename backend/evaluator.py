from typing import List, Dict
from datetime import datetime

from models import ProductData, ScanResult, Violation
from rules import RULES
from scraper import scrape_product


# =====================================================
# CATEGORY INFERENCE
# =====================================================
def infer_product_category(product: ProductData) -> str:
    """
    Priority-based category inference.
    Health & cosmetics override electronics.
    """

    text = " ".join(
        filter(
            None,
            [
                getattr(product, "title", ""),
                getattr(product, "description", ""),
                getattr(product, "technical_details", ""),
            ]
        )
    ).lower()

    CATEGORY_KEYWORDS = {
        "health": [
            "medicine", "tablet", "capsule", "dosage",
            "prescription", "ayurvedic", "supplement"
        ],
        "cosmetics": [
            "sunscreen", "spf", "lotion", "cream",
            "skincare", "skin", "uv", "pa++", "pa+++",
            "dermatologically", "cosmetic"
        ],
        "food": [
            "ingredients", "nutrition", "fssai",
            "expiry", "best before", "calories"
        ],
        "clothing": [
            "fabric", "cotton", "polyester",
            "shirt", "jeans", "dress", "size"
        ],
        "toys": [
            "toy", "kids", "child", "age"
        ],
        "books": [
            "isbn", "author", "publisher", "edition"
        ],
        "electronics": [
            "battery", "charger", "adapter",
            "usb", "bluetooth", "voltage", "watt"
        ],
        "appliances": [
            "refrigerator", "washing machine",
            "microwave", "air conditioner"
        ],
    }

    # 🔥 PRIORITY ORDER (IMPORTANT)
    PRIORITY = [
        "health",
        "cosmetics",
        "food",
        "clothing",
        "toys",
        "books",
        "electronics",
        "appliances",
    ]

    for category in PRIORITY:
        if any(k in text for k in CATEGORY_KEYWORDS[category]):
            return category

    return "all"


# =====================================================
# RULE SELECTION (THIS FIXES YOUR BUG)
# =====================================================

def get_applicable_rules(product_category: str) -> List[Dict]:
    """
    Returns only:
    - 'all' rules
    - rules matching product_category
    """
    return [
        rule for rule in RULES
        if rule["category"] == "all" or rule["category"] == product_category
    ]


# =====================================================
# FIELD INDEX (SAFE ACCESS)
# =====================================================

def build_field_index(product: ProductData) -> Dict[str, bool]:
    """
    Maps all possible rule fields to availability.
    Missing fields = False (never crash).
    """
    fields = {}

    for rule in RULES:
        for field in rule.get("required_fields", []):
            if field not in fields:
                value = getattr(product, field, None)
                fields[field] = bool(value)

    return fields


# =====================================================
# CORE COMPLIANCE ENGINE
# =====================================================

def run_compliance_check(product: ProductData) -> Dict:
    product_category = infer_product_category(product)
    applicable_rules = get_applicable_rules(product_category)
    field_index = build_field_index(product)

    violations = []

    for rule in applicable_rules:
        missing_fields = [
            f for f in rule.get("required_fields", [])
            if not field_index.get(f, False)
        ]

        if missing_fields:
            violations.append(
                Violation(
                    rule_id=rule["id"],
                    severity=rule["severity"],
                    description=f"{rule['title']} [{rule['law']}]",
                    suggestion=(
                        f"Ensure the following field(s) are disclosed: "
                        f"{', '.join(missing_fields)}"
                    )
                )
            )

    # Risk score (simple & consistent)
    score = 100
    for v in violations:
        if v.severity == "HIGH":
            score -= 20
        elif v.severity == "MEDIUM":
            score -= 10
        else:
            score -= 5

    score = max(0, score)

    return {
        "category": product_category,
        "risk_score": score,
        "violations": violations
    }


# =====================================================
# PUBLIC ENTRY POINT
# =====================================================

def evaluate_url(url: str) -> Dict:
    product = scrape_product(url)
    return run_compliance_check(product)
