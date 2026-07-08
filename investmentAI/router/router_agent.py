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
from investmentAI.utils.logger import (
    print_header,
    print_block,
    print_success,
    print_error,
)
MAX_RETRIES = 2

DISCLAIMER = """
------------------------------------------------------------------

Disclaimer:
This information is for educational purposes only and should not be considered personalized financial advice. Please consult a qualified financial advisor before making investment decisions.
"""

async def route_agent(session_service, query):

    print_header("User Request")
    print_block("Query", query)

    # Step 1 : Detect Intent
    intent_response = await run_agent(
        intent_agent,
        session_service,
        query,
    )

    intent = IntentResult.model_validate_json(intent_response)

    print_header("Intent Detection")

    print_block(
        "Detected Intent",
        f"""
Intent      : {intent.intent.value}
Confidence  : {intent.confidence}
Reason      : {intent.reason}
"""
    )

    # Step 2 : Greeting
    if intent.intent == Intent.GREETING:

        print_success("Routing to General Helper Agent")

        return await run_agent(
            general_helper_agent,
            session_service,
            query,
        )

    # Step 3 : Out Of Scope
    if intent.intent == Intent.OUT_OF_SCOPE:

        print_success("Routing to Out Of Scope Agent")

        return await run_agent(
            out_of_scope_agent,
            session_service,
            query,
        )

    # Step 4 : Investment
    if intent.intent in (
        Intent.INVESTMENT,
        Intent.PRODUCT_INFORMATION,
    ):

        current_query = query

        for attempt in range(MAX_RETRIES):

            print_header(f"Investment Workflow - Attempt {attempt + 1}")

            # Generate Recommendation
            recommendation = await run_agent(
                investment_agent,
                session_service,
                current_query,
            )

            print_block(
                "Generated Recommendation",
                recommendation,
            )

            # Compliance Review
            compliance_result = await run_agent(
                compliance_agent,
                session_service,
                recommendation,
            )

            compliance_status = compliance_result.strip().upper()

            print_header("Compliance Review")

            if compliance_status.startswith("APPROVED"):
                print_success("Compliance Status : APPROVED")
            else:
                print_error("Compliance Status : REJECTED")

            print_block(
                "Compliance Output",
                compliance_result,
            )

            # Approved
            if compliance_status.startswith("APPROVED"):

                final_response = (
                    recommendation.strip()
                    + DISCLAIMER
                )

                print_header("Final Response")

                print_block(
                    "Response",
                    final_response,
                )

                return final_response

            print_error("Retrying Investment Agent...")

            # Retry Prompt
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

        print_error("Maximum retries reached.")

        return (
            "I'm sorry, but I couldn't generate a compliant investment response "
            "after multiple attempts. Please try again later."
        )

    raise Exception("Unknown Intent")