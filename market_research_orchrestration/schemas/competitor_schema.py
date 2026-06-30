from pydantic import BaseModel, Field
from typing import Optional, List


class CompetitorInput(BaseModel):
    company_name: Optional[str] = Field(
        default=None,
        description="Company whose competitors should be analyzed."
    )

    industry: str = Field(
        description="Industry or market to analyze."
    )

    country: Optional[str] = Field(
        default="Global",
        description="Country or region for competitor analysis."
    )

    max_competitors: int = Field(
        default=5,
        ge=1,
        le=10,
        description="Maximum number of competitors to return."
    )


class Competitor(BaseModel):
    name: str = Field(
        description="Competitor company name."
    )

    description: str = Field(
        description="Brief description of the competitor."
    )

    products: List[str] = Field(
        default_factory=list,
        description="Major products or services."
    )

    pricing_strategy: Optional[str] = Field(
        default=None,
        description="Pricing strategy if available."
    )

    strengths: List[str] = Field(
        default_factory=list,
        description="Key strengths."
    )

    weaknesses: List[str] = Field(
        default_factory=list,
        description="Key weaknesses."
    )

    market_position: Optional[str] = Field(
        default=None,
        description="Market position such as Leader, Challenger, Niche, etc."
    )

class CompetitorOutput(BaseModel):
    company_name: str = Field(
        description="Company requested by the user."
    )

    competitors: List[Competitor] = Field(
        description="List of competitor analyses."
    )

    competitive_landscape: str = Field(
        description="Summary of the competitive landscape."
    )

    recommendations: List[str] = Field(
        default_factory=list,
        description="Strategic recommendations based on the analysis."
    )