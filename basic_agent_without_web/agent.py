from google.adk.agents import LlmAgent
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.genai import types
import asyncio
from dotenv import load_dotenv
load_dotenv()

async def create_session():
    session_service=InMemorySessionService()
    await session_service.create_session(
        app_name="Agent_Without_ADK_Web",
        user_id='amit001',
        session_id='session01',
        state={"name":"Amit Pal"},       
    )
    return session_service

async def get_agent():
    root_agent=LlmAgent(
    name="Basic_Agent",
    model="gemini-2.5-flash",
    description="This agent will run without adk web",
    instruction="""
You are heplful assistant give the answer to the query. Be polite and humantic while answering the query""",
    )
    return root_agent

async def main(query):
    session_service= await create_session()
    agent= await get_agent()
    formatted_query=types.Content(role='user',parts=[types.Part(text=query)])
    runner=Runner(
        app_name='Agent_Without_ADK_Web',
        agent=agent,
        session_service=session_service,
    )

    #Run the agent
    events=runner.run_async(
        new_message=formatted_query,
        session_id='session01',
        user_id='amit001'
    )

    async for event in events:
        if event.is_final_response() and event.content:
            print(event.content.parts[0].text)
if __name__=="__main__":
    asyncio.run(main("What is the advantage of using mullti agent frameworks?"))

