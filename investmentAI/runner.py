import asyncio

from dotenv import load_dotenv
load_dotenv()
from investmentAI.router.router_agent import route_agent
from investmentAI.services.session_service import create_session

async def main(query):

    session_service = await create_session()

    response = await route_agent(
        session_service,
        query,
    )

    #print(response)

if __name__ == "__main__":
    asyncio.run(
        main("What is SIP?")
    )