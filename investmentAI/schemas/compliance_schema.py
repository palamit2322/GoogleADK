from pydantic import BaseModel

class ComplianceResult(BaseModel):

    approved: bool

    violations: list[str]

    disclaimer: str