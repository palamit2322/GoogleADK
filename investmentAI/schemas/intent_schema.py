from enum import Enum as PyEnum
from pydantic import BaseModel, Field

class Intent(str, PyEnum):
    PRODUCT_INFORMATION = "PRODUCT_INFORMATION"
    UNKNOWN = "UNKNOWN"
    GREETING = "GREETING"
    INVESTMENT = "INVESTMENT"
    OUT_OF_SCOPE = "OUT_OF_SCOPE"

class IntentResult(BaseModel):
    intent: Intent
    confidence: float= Field(description="Confidence score between 0 and 1")
    reason: str

