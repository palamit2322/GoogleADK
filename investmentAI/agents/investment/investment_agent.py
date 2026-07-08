from google.adk.agents import SequentialAgent

from investmentAI.agents.investment.retrieval_agent import retrieval_agent
from investmentAI.agents.investment.compliance_agent import compliance_agent

investment_agent = SequentialAgent(
    name="investment_agent",
    description="Generates investment responses using the RAG retrieval pipeline.",
    sub_agents=[
        retrieval_agent
    ],
)
