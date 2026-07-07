from google.adk.agents import LlmAgent
from investmentAI.instructions.recommendation_agent_instruction import RECOMMENDATION_AGENT_INSTRUCTION


recommendation_agent = LlmAgent(
    name="recommendation_agent",
    model="gemini-2.5-flash",
    description="Generates personalized investment recommendations.",
    instruction=RECOMMENDATION_AGENT_INSTRUCTION,
)