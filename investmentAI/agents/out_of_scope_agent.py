from google.adk.agents import LlmAgent
from investmentAI.instructions.out_of_scope_agent_instruction import OUT_OF_SCOPE_AGENT_INSTRUCTION

out_of_scope_agent = LlmAgent(
    name="out_of_scope_agent",
    model="gemini-2.5-flash",
    description="Handles queries outside the Investment AI domain.",
    instruction=OUT_OF_SCOPE_AGENT_INSTRUCTION,
)