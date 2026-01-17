import re
from typing import Dict, Optional


# --------------------------------------------------
# NORMALIZATION
# --------------------------------------------------

def normalize_text(value: Optional[str]) -> Optional[str]:
    if not value:
        return None
    value = value.lower()
    value = re.sub(r"[^\w\s\-.,]", "", value)  # remove invisible chars
    value = re.sub(r"\s+", " ", value).strip()
    return value


# --------------------------------------------------
# HEURISTIC PARSER (ROBUST & SAFE)
# --------------------------------------------------

def heuristic_parse(text: str) -> Dict[str, Optional[str]]:
    text = text.lower()

    def grab(pattern):
        m = re.search(pattern, text, re.IGNORECASE)
        if not m:
            return None
        for g in m.groups():
            if g:
                return normalize_text(g)
        return None

    parsed = {
        "brand": grab(r"brand\s*:\s*([^|]+)"),
        "manufacturer": grab(r"manufacturer\s*:\s*([^|]+)"),
        "origin_country": grab(
            r"country of origin\s*:\s*([^|]+)|country as labeled\s*:\s*([^|]+)"
        ),
        "usage": grab(r"usage\s*:\s*([^|]+)"),
        "ingredients": grab(r"ingredients\s*:\s*([^|]+)"),
        "expiry": grab(r"(expiry|best before)\s*:\s*([^|]+)"),
        "customer_care_contact": grab(r"(toll free|customer care)[^|]*"),
        "importer": grab(r"importer\s*contact\s*information\s*:\s*([^|]+)"),
        "packer": grab(r"packer\s*contact\s*information\s*:\s*([^|]+)"),
    }

    return parsed


# --------------------------------------------------
# MAIN ENTRY (AI-SAFE)
# --------------------------------------------------

def ai_parse_technical_details(text: str) -> Dict[str, Optional[str]]:
    """
    AI-style structured extraction.
    Currently heuristic-only to avoid API dependency.
    """
    if not text:
        return {}
    return heuristic_parse(text)
