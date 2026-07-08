from investmentAI.schemas.intent_schema import (
    Intent,
    IntentResult,
)
from investmentAI.agents.intent_agent import intent_agent
from investmentAI.agents.general_helper_agent import general_helper_agent
from investmentAI.agents.out_of_scope_agent import out_of_scope_agent
from investmentAI.agents.investment.investment_agent import investment_agent

from investmentAI.utils.agent_runner import run_agent


async def route_agent(
    session_service,
    query,
):
    response = await run_agent(
        intent_agent,
        session_service,
        query,
    )

    intent = IntentResult.model_validate_json(response)

    print(intent)

    if intent.intent == Intent.GREETING:
        return general_helper_agent

    elif intent.intent == Intent.INVESTMENT:
        return investment_agent

    elif intent.intent == Intent.OUT_OF_SCOPE:
        return out_of_scope_agent

    raise Exception("Unknown Intent")