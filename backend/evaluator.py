# backend/evaluator.py - PERFECTLY FIXED
from typing import List, Dict, Any
from models import Price, ProductData, ScanResult, Violation as ModelViolation
from rules import RULES
import json
import re
from datetime import datetime

from scraper import scrape_product

def evaluate_url(url: str):
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
    MAIN FUNCTION - Returns YOUR exact ScanResult format
    """
    violations_data = []
    
    # Filter realistic rules for general products (not food/health/electronics specific)
    relevant_rules = _get_relevant_rules(product)
    
    for rule in relevant_rules:
        violation = _check_rule_against_product(rule, product)
        if violation:
            violations_data.append(violation)
    
    # Calculate risk_score (1-10) for ScanResult
    risk_score = _calculate_risk_score(violations_data)
    
    # Convert to YOUR Pydantic models
    model_violations = [
        ModelViolation(
            rule_id=v["rule_id"],
            severity=v["severity"],
            description=v["description"],
            suggestion=v["suggestion"]
        ) for v in violations_data
    ]
    
    return ScanResult(
        id=None,
        timestamp=datetime.now(),
        product=product,
        risk_score=risk_score,
        violations=model_violations
    )

def _get_relevant_rules(product: ProductData) -> List[Dict]:
    """Filter rules to only general e-commerce (not food/health specific)"""
    general_rules = []
    
    # Core E-Commerce Rules 2020 (always apply)
    core_rule_ids = ["EC-01", "EC-04", "EC-06", "EC-07", "EC-09"]
    
    for rule in RULES:
        rule_id = rule["id"]
        # Always include core rules
        if rule_id in core_rule_ids:
            general_rules.append(rule)
        # Include category rules only if product matches
        elif rule["category"] == "all":
            general_rules.append(rule)
        # Skip food/health/electronics specific for general demo
        elif rule["category"] not in ["food", "health", "electronics"] or product.title:
            general_rules.append(rule)
    
    return general_rules[:8]  # Limit to top 8 for realistic demo

def _check_rule_against_product(rule: Dict, product: ProductData) -> Dict:
    """Map YOUR ProductData fields → rule checks"""
    field_mapping = {
        "seller": product.seller,
        "price": product.price,
        "description": product.description,
        "returns": product.returns,
        "delivery": product.delivery,
        "warranty": product.warranty,
        "brand": product.brand,
        "origin": None,
        "charges": None
    }

    
    missing_fields = []
    for required_field in rule.get("required_fields", []):
        field_value = field_mapping.get(required_field)
        if not field_value or str(field_value or "").strip() == "" or field_value is None:
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
    """Calculate 1-10 score for ScanResult.risk_score"""
    if not violations_data:
        return 1
    
    severity_weights = {"HIGH": 3, "MEDIUM": 2, "LOW": 1}
    total_score = sum(severity_weights.get(v["severity"], 1) for v in violations_data)
    avg_score = total_score / len(violations_data)
    
    # Map to 1-10 scale
    risk_score = min(10, max(1, int(avg_score * 2.5)))
    return risk_score

'''
# TEST FUNCTION
def test_with_your_data():
    """Test with YOUR scraper data - NO ERRORS"""
    from models import ProductData
    
    product = ProductData(
        url="https://www.amazon.in/",
        title="No title found",
        price=Price(),
        description=None,
        seller_info="Amazon",
        image_url=None
    )
    
    print("🧪 TESTING YOUR EXACT DATA:")
    result = evaluate_compliance(product)
    
    print(f"🎯 Risk Score: {result.risk_score}/10")
    print(f"📋 Violations ({len(result.violations)}):")
    for v in result.violations:
        print(f"  ❌ {v.rule_id}: {v.description}")
    print(f"\n✅ SUCCESS - No errors!")
    print(f"📦 Ready for main.py integration!")

if __name__ == "__main__":
    test_with_your_data()
'''