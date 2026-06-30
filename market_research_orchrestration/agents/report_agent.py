from google.adk.agents import Agent
from market_research_orchrestration.instructions.report_instructions import REPORT_INSTRUCTION
from market_research_orchrestration.schemas.report_schema import ReportInput,ReportOutput

report_agent=Agent(
    name='report_agent',
    model='gemini-2.5-flash',
    description="""
    Generates a comprehensive market research report by combining
    the outputs from the Market, Competitor, and Trend agents.
    """,
    instruction=REPORT_INSTRUCTION,
    input_schema=ReportInput,
    output_schema=ReportOutput,
    output_key='report_agent_analysis'
)