from google.adk.agents import Agent
from google.adk.tools.google_search_tool import GoogleSearchTool
from market_research_orchrestration.instructions.competitor_instructions import COMPETITOR_INSTRUCTION
from market_research_orchrestration.schemas.competitor_schema import CompetitorInput,CompetitorOutput

competitor_agent=Agent(
    name='competitor_agent',
    model='gemini-2.5-flash',
    description="""
    Performs competitive intelligence and competitor analysis for
    a given company, product, or market.
    """,
    instruction=COMPETITOR_INSTRUCTION,
    input_schema=CompetitorInput,
    output_schema=CompetitorOutput,
    output_key='competitor_agent_analysis',
    tools=[GoogleSearchTool]
)

