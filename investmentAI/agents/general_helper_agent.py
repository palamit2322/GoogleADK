from google.adk.agents import LlmAgent
from investmentAI.instructions.general_helper_agent_instruction import GENERAL_HELPER_AGENT_INSTRUCTION

general_helper_agent = LlmAgent(
    name="general_helper_agent",
    model="gemini-2.5-flash",
    description="Handles greetings and general conversations.",
    instruction=GENERAL_HELPER_AGENT_INSTRUCTION,
)