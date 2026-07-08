from investmentAI.schemas.intent_schema import (
    Intent,
    IntentResult,
)

from investmentAI.agents.intent_agent import intent_agent
from investmentAI.agents.general_helper_agent import general_helper_agent
from investmentAI.agents.out_of_scope_agent import out_of_scope_agent
from investmentAI.agents.investment.investment_agent import investment_agent
from investmentAI.agents.investment.compliance_agent import compliance_agent

from investmentAI.utils.agent_runner import run_agent

MAX_RETRIES = 2


async def route_agent(session_service, query):

    # Step 1 : Detect Intent
    intent_response = await run_agent(
        intent_agent,
        session_service,
        query,
    )

    intent = IntentResult.model_validate_json(intent_response)

    print(intent)

    # Step 2 : Greeting
    if intent.intent == Intent.GREETING:
        return await run_agent(
            general_helper_agent,
            session_service,
            query,
        )

    # Step 3 : Out Of Scope
    if intent.intent == Intent.OUT_OF_SCOPE:
        return await run_agent(
            out_of_scope_agent,
            session_service,
            query,
        )

    # Step 4 : Investment
    if intent.intent == Intent.INVESTMENT:

        current_query = query

        for attempt in range(MAX_RETRIES):

            print(f"Investment Attempt : {attempt + 1}")

            # Generate recommendation
            recommendation = await run_agent(
                investment_agent,
                session_service,
                current_query,
            )

            print("Recommendation:")
            print(recommendation)

            # Review recommendation
            compliance_result = await run_agent(
                compliance_agent,
                session_service,
                recommendation,
            )

            print("Compliance Result:")
            print(compliance_result)

            # Approved
            if compliance_result and "APPROVED" in compliance_result.upper():
                return recommendation

            # Prepare retry prompt
            current_query = f"""
User Question:
{query}

Previous Recommendation:
{recommendation}

Compliance Feedback:
{compliance_result}

Please regenerate the response by fixing ALL compliance issues.
Return ONLY the corrected recommendation.
"""

        return (
            "I'm sorry, but I couldn't generate a compliant investment response. "
            "Please try again later."
        )

    raise Exception("Unknown Intent")