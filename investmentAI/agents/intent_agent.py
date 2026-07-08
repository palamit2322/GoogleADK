from google.adk.agents import LlmAgent
from investmentAI.instructions.intent_agent_instruction import INTENT_AGENT_INSTRUCTION
from investmentAI.schemas.intent_schema import IntentResult

from investmentAI.agents.investment.investment_agent import investment_agent
from investmentAI.agents.investment.retrieval_agent import retrieval_agent
from investmentAI.agents.general_helper_agent import general_helper_agent
from investmentAI.agents.out_of_scope_agent import out_of_scope_agent
from investmentAI.callbacks.logging.logging_config import ExecutionLogger
execution_logger = ExecutionLogger()

intent_agent = LlmAgent(
    name="intent_agent",
    model="gemini-2.5-flash",
    instruction=INTENT_AGENT_INSTRUCTION,
    description="Detects the intent of the user query.",
    sub_agents=[
        investment_agent,
        general_helper_agent,
        out_of_scope_agent
    ]
)