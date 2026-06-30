from google.adk.agents import Agent
from market_research_orchrestration.agents.market_agent import market_agent
from market_research_orchrestration.agents.competitor_agent import competitor_agent
from market_research_orchrestration.agents.trend_agent import trend_agent
from market_research_orchrestration.agents.report_agent import report_agent
from market_research_orchrestration.instructions.router_instructions import ROUTER_INSTRUCTION




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