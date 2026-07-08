from google.adk.sessions import InMemorySessionService


async def create_session():

    session_service = InMemorySessionService()

    await session_service.create_session(
        app_name="InvestmentAI",
        user_id="amit001",
        session_id="session01",
        state={},
    )

    return session_service