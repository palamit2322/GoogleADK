from google.adk.runners import Runner
from google.genai import types


async def run_agent(
    agent,
    session_service,
    query,
    app_name="InvestmentAI",
    session_id="session01",
    user_id="amit001",
):

    runner = Runner(
        app_name=app_name,
        agent=agent,
        session_service=session_service,
    )

    message = types.Content(
        role="user",
        parts=[types.Part(text=query)],
    )

    events = runner.run_async(
        user_id=user_id,
        session_id=session_id,
        new_message=message,
    )

    response = None

    async for event in events:

        # Debug
        print("=" * 80)
        print(event)

        if not event.is_final_response():
            continue

        if event.content is None:
            continue

        if not event.content.parts:
            continue

        response = event.content.parts[0].text

    return response