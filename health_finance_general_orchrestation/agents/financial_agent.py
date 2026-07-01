from google.adk.agents import Agent
from health_finance_general_orchrestation.instructions.finance_instructions import FINANACE_INSTRUCTIONS

financial_agent = Agent(
    name="FinancialAdvisor",
    model="gemini-2.5-flash",
    instruction=FINANACE_INSTRUCTIONS,
    description="A helpful financial agent that will provide you the assitance related to finance."
)