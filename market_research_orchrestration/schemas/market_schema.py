from pydantic import BaseModel,Field

class MarketInput(BaseModel):
    topic:str=Field(description='Market to research ')

    country:str=Field(description='Target country')

class MarketOutput(BaseModel):
    market_size: str
    growth_rate: str
    opportunities: list[str]
    challenges: list[str]
    summary: str    