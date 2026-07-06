from google.adk.agents import LlmAgent
from investmentAI.agents.intent_agent import intent_agent
from investmentAI.instructions.root_agent_instruction import ROOT_AGENT_INSTRUCTION

root_agent = LlmAgent(
    name="investment_root_agent",
    model="gemini-2.5-flash",
    description="Routes user requests to the appropriate agent.",
    instruction=ROOT_AGENT_INSTRUCTION,
    sub_agents=[
        intent_agent
    ]
)