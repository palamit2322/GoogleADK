from google.adk.agents import Agent
from health_finance_general_orchrestation.instructions.health_instructions import PROBLEM_ANALYSER_INSTRUCTIONS
from health_finance_general_orchrestation.schemas.health_schema import  ProblemAnalysis


problem_analyzer_agent = Agent(
    name="ProblemAnalyzerAgent",
    model="gemini-2.5-flash",
    instruction=PROBLEM_ANALYSER_INSTRUCTIONS,
    output_schema=ProblemAnalysis,
    output_key="problem_analysis_result",
)