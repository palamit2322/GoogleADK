from google.adk.agents import Agent
from health_finance_general_orchrestation.instructions.general_instructions import GENERAL_INSTRUCTIONS

general_agent = Agent(
    name="GeneralHelper",
    model="gemini-2.5-flash",
    instruction=GENERAL_INSTRUCTIONS,
    description="A helpful general agent that will provide you the assitance for general purpose."
)