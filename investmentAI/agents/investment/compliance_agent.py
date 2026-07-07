from google.adk.agents import LlmAgent
from investmentAI.instructions.compliance_agent_instruction import COMPLIANCE_AGENT_INSTRUCTION


compliance_agent = LlmAgent(
    name="compliance_agent",
    model="gemini-2.5-flash",
    description="Reviews investment recommendations for regulatory and safety compliance.",
    instruction=COMPLIANCE_AGENT_INSTRUCTION,
)