from google.adk.agents import SequentialAgent

from investmentAI.agents.investment.retrieval_agent import retrieval_agent
from investmentAI.agents.investment.recommendation_agent import recommendation_agent
from investmentAI.agents.investment.compliance_agent import compliance_agent

investment_agent = SequentialAgent(
    name="investment_agent",
    description="Handles investment advice workflow.",
    sub_agents=[
        retrieval_agent,
        recommendation_agent,
        compliance_agent,
    ],
)