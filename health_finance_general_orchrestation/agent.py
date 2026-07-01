from google.adk.agents import Agent,SequentialAgent
from health_finance_general_orchrestation.agents.health_agents.advice_generator_agent import advice_generator_agent
from health_finance_general_orchrestation.agents.health_agents.problem_analyzer_agent import problem_analyzer_agent
from health_finance_general_orchrestation.agents.financial_agent import financial_agent
from health_finance_general_orchrestation.agents.general_agent import general_agent


health_agent=SequentialAgent(
    name="HealthAdvisor",
    sub_agents=[problem_analyzer_agent, advice_generator_agent],
)

root_agent = Agent(
    name="ConsultationRouter",
    model="gemini-2.5-flash",
    instruction="""
    You are a routing agent.

    Select exactly one sub-agent.

    - HealthAdvisor:
      Mental health, anxiety, depression, stress, fitness, diet, therapy.

    - FinancialAdvisor:
      Investment, tax, budgeting, loans, savings, insurance.

    - GeneralHelper:
      Everything else.

    Never answer yourself.
    Always delegate to the correct sub-agent.
    """,
    sub_agents=[
        health_agent,
        financial_agent,
        general_agent,
    ],
)