from pydantic import BaseModel

class InvestmentRequest(BaseModel):

    session_id: str

    customer_id: str

    query: str