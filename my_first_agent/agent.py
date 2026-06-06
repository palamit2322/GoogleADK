from google.adk.agents import Agent
from google.adk.tools import google_search_tool
# from dotenv import load_dotenv

#load_dotenv()

root_agent=Agent(
    name='QA_agent',
    model='gpt-4o-mini',
    description='This agent is for generating the response based on your query',
    instruction='You are helpful assistant, Answer the query in polite and in short summary with in points if required',
    tools=[google_search_tool]
)