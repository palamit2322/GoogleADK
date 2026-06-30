from typing import Optional, List

from pydantic import BaseModel, Field


class TrendInput(BaseModel):
    industry: str = Field(
        description="Industry or market for trend analysis."
    )

    country: Optional[str] = Field(
        default="Global",
        description="Country or region."
    )

    include_future_outlook: bool = Field(
        default=True,
        description="Include future outlook and predictions."
    )

    include_technology_trends: bool = Field(
        default=True,
        description="Include technology trends."
    )


class MarketTrend(BaseModel):
    title: str = Field(
        description="Trend title."
    )

    description: str = Field(
        description="Brief explanation of the trend."
    )

    impact: str = Field(
        description="Business impact of the trend."
    )


class Opportunity(BaseModel):
    title: str = Field(
        description="Opportunity title."
    )

    description: str = Field(
        description="Opportunity description."
    )



class TrendOutput(BaseModel):
    industry: str = Field(
        description="Industry analyzed."
    )

    current_trends: List[MarketTrend] = Field(
        description="Current market trends."
    )

    emerging_trends: List[MarketTrend] = Field(
        description="Emerging trends."
    )

    opportunities: List[Opportunity] = Field(
        description="Business opportunities."
    )

    future_outlook: str = Field(
        description="Future market outlook."
    )

    trend_summary: str = Field(
        description="Overall trend analysis summary."
    )