from google.adk.agents import LlmAgent
from investmentAI.instructions.retrieval_agent_instruction import RETRIEVAL_INSTRUCTIONS
from investmentAI.tools.rag_tool import retrieval_tool
retrieval_agent = LlmAgent(
    name="retrieval_agent",
    model="gemini-2.5-flash",
    description="Handles greetings and general conversations.",
    instruction=RETRIEVAL_INSTRUCTIONS,
    tools=[retrieval_tool]
)