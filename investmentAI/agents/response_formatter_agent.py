from google.adk.agents import Agent
from investmentAI.instructions.response_formatter_instruction import RESPONSE_FORMATTER_INSTRUCTION

response_formatter_agent = Agent(
    name="response_formatter_agent",
    model="gemini-2.5-flash",
    description="""
    Formats the final response before it is returned to the user.
    Ensures consistency, readability, and proper structure.
    """,
    instruction=RESPONSE_FORMATTER_INSTRUCTION
    )