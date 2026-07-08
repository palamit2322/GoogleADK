from google.adk.agents import LlmAgent
from investmentAI.agents.intent_agent import intent_agent
from investmentAI.instructions.root_agent_instruction import ROOT_AGENT_INSTRUCTION
from google.adk.agents import LlmAgent
from dotenv import load_dotenv
load_dotenv()

root_agent = LlmAgent(
    name="investment_root_agent",
    description="Investment Assistant",
    model="gemini-2.5-flash",
    instruction=ROOT_AGENT_INSTRUCTION,
    sub_agents=[
        intent_agent
    ]
)
