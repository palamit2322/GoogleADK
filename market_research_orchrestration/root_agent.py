from google.adk.agents import Agent
from agents.market_agent import 

from instructions.router_instructions import ROUTER_INSTRUCTION



root_agent=Agent(
    name='root_agent',
    model='gemini-2.5-flash',
    instruction=ROUTER_INSTRUCTION,
    sub_agents=[]
)