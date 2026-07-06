from enum import Enum as PyEnum
from pydantic import BaseModel, Field

class IntentType(str, PyEnum):
    INVESTMENT_ADVICE = "INVESTMENT_ADVICE"
    PRODUCT_INFORMATION = "PRODUCT_INFORMATION"
    GENERAL_GREETING = "GENERAL_HELPER"
    UNKNOWN = "UNKNOWN"
    OUT_OF_SCOPE = "OUT_OF_SCOPE"

class IntentResult(BaseModel):
    intent: IntentType
    confidence: float= Field(description="Confidence score between 0 and 1")

