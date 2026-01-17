from pydantic import BaseModel,  Field
from typing import List, Optional
from datetime import datetime

# Used by Person 2 (Scraper)
class Price(BaseModel):
    mrp: Optional[float] = None
    deal: Optional[float] = None
    discount: Optional[str] = None

class ProductData(BaseModel):
    url: str
    title: str
    brand: Optional[str] = None
    seller: Optional[str] = None
    price: Price = Price()
    returns: Optional[str] = None
    warranty: Optional[str] = None
    delivery: Optional[str] = None
    technical_details: Optional[str] = None
    timestamp: datetime = Field(default_factory=datetime.now)


# Used by Person 3 (Compliance)
class Violation(BaseModel):
    rule_id: str
    severity: str  # HIGH, MEDIUM, LOW
    description: str
    suggestion: str

if __name__ == "__main__":
    sample = ProductData(
        url="https://example.com/product",
        title="Sample Product",
        seller="Test Seller",
        price=Price(mrp=1299, deal=999, discount="23% off")
    )
    print(sample.model_dump_json(indent=2))

class ScanResult(BaseModel):
    id: int | None = None
    timestamp: datetime
    product: ProductData
    risk_score: int
    violations: list[Violation]
    trust_index: dict  # {"score": int, "reasons": list[str]}


# API Request Model
class ScanRequest(BaseModel):
    url: str
