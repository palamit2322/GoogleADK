from google.adk.agents import Agent
from agents.market_agent import market_agent
from agents.competitor_agent import competitor_agent
from agents.trend_agent import trend_agent
from agents.report_agent import report_agent
from instructions.router_instructions import ROUTER_INSTRUCTION



root_agent=Agent(
    name='root_agent',
    model='gemini-2.5-flash',
    instruction=ROUTER_INSTRUCTION,
    description="""
    Root orchestrator responsible for intent classification, task routing,
    and delegation to specialized agents including market analysis,
    competitor analysis, trend analysis, and report generation workflows.
    """,
    sub_agents=[market_agent,competitor_agent,trend_agent,report_agent]
)