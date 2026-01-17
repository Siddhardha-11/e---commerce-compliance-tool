import re
from typing import List
from bs4 import BeautifulSoup

from models import ProductData

class DarkPatternFinding:
    def __init__(self, code: str, message: str, severity: str = "medium"):
        self.code = code
        self.message = message
        self.severity = severity

    def as_dict(self):
        return {
            "code": self.code,
            "message": self.message,
            "severity": self.severity,
            "category": "dark_pattern",
        }


def detect_dark_patterns(product: ProductData, html: str) -> List[DarkPatternFinding]:
    findings: List[DarkPatternFinding] = []

    soup = BeautifulSoup(html, "lxml")
    full_text = soup.get_text(separator=" ", strip=True)

    # ---------- 1) Drip pricing keywords ----------
    # Look for extra fees like "convenience fee", "internet handling fee", etc. [web:63]
    drip_keywords = [
        "convenience fee",
        "platform fee",
        "internet handling fee",
        "handling charges",
        "processing fee",
        "service charge",
    ]
    if any(kw.lower() in full_text.lower() for kw in drip_keywords):
        findings.append(
            DarkPatternFinding(
                code="DARK_DRIP_PRICING",
                message=(
                    "Additional charges like convenience/platform/handling fees are mentioned "
                    "separately from the main price, indicating possible drip pricing."
                ),
                severity="high",
            )
        )

    # ---------- 2) Exaggerated 'up to X% off' ----------
    # If text says "up to 80% off" but actual discount is far lower, flag it. [web:61][web:63]
    up_to_match = re.search(r"up to\s+(\d+)%\s*off", full_text, re.I)
    if up_to_match and product.price and product.price.mrp and product.price.deal:
        try:
            claimed = int(up_to_match.group(1))
            mrp = float(product.price.mrp)
            deal = float(product.price.deal)
            if mrp > deal:
                actual_pct = round((mrp - deal) / mrp * 100)
                # If actual is less than half of claimed "up to", mark as exaggerated
                if actual_pct < claimed / 2:
                    findings.append(
                        DarkPatternFinding(
                            code="DARK_EXAGGERATED_DISCOUNT",
                            message=(
                                f"Page claims 'up to {claimed}% off' but this product's "
                                f"actual discount is about {actual_pct}%."
                            ),
                            severity="medium",
                        )
                    )
        except Exception:
            pass

    # OPTIONAL: 3) Pre-selected add-ons (requires HTML)
    # For now, you can skip or leave placeholder.

    return findings

