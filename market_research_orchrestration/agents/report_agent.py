from google.adk.agents import Agent
from google.adk.tools.google_search_tool import GoogleSearchTool
from instructions.report_instructions import REPORT_INSTRUCTION
from schemas.report_schema import ReportInput,ReportOutput

report_agent=Agent(
    name='market_agent',
    model='gemini-2.5-flash',
    description="""
    Generates a comprehensive market research report by combining
    the outputs from the Market, Competitor, and Trend agents.
    """,
    instruction=REPORT_INSTRUCTION,
    input_schema=ReportInput,
    output_schema=ReportOutput,
    output_key='report_agent_analysis',
    tools=[GoogleSearchTool]
)