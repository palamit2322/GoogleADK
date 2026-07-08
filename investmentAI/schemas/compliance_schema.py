from enum import Enum
from pydantic import BaseModel


class ComplianceStatus(str, Enum):
    PASS = "PASS"
    FAIL = "FAIL"


class ComplianceResult(BaseModel):
    status: ComplianceStatus
    feedback: str
    corrected_response: str | None = None