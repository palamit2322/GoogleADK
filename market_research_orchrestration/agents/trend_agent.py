from google.adk.agents import Agent
from google.adk.tools.google_search_tool import GoogleSearchTool
from instructions.trend_instructions import TREND_INSTRUCTION
from schemas.trend_schema import TrendInput,TrendOutput

trend_agent=Agent(
    name='trend_agent',
    model='gemini-2.5-flash',
    description="""
    Identifies and analyzes current and emerging market trends,
    technologies, consumer behavior, opportunities, and future outlook
    for a given industry or market.
    """,
    instruction=TREND_INSTRUCTION,
    input_schema=TrendInput,
    output_schema=TrendOutput,
    output_key='trend_agent_analysis',
    tools=[GoogleSearchTool]
)