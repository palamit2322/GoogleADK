from google.adk.agents import Agent
from google.adk.tools.google_search_tool import GoogleSearchTool
from market_research_orchrestration.instructions.market_instructions import MARKET_INSTRUCTION
from market_research_orchrestration.schemas.market_schema import MarketInput,MarketOutput

market_agent=Agent(
    name='market_agent',
    model='gemini-2.5-flash',
    description="""
    Performs market analysis for a given industry or domain.
    Returns market size, growth, opportunities, challenges,
    and key insights.
    """,
    instruction=MARKET_INSTRUCTION,
    input_schema=MarketInput,
    output_schema=MarketOutput,
    output_key='market_agent_analysis',
    tools=[GoogleSearchTool]
)