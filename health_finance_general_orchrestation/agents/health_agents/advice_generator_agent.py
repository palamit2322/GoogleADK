from google.adk.agents import Agent
from health_finance_general_orchrestation.instructions.health_instructions import ADVICE_GENERATOR_INSTRUCTIONS
from health_finance_general_orchrestation.schemas.health_schema import  ConsultationResp,ProblemAnalysis


advice_generator_agent = Agent(
    name="AdviceGeneratorAgent",
    model="gemini-2.5-flash",
    instruction=ADVICE_GENERATOR_INSTRUCTIONS,
    input_schema=ProblemAnalysis,
    output_schema=ConsultationResp,
    output_key="final_consultation_response",
)