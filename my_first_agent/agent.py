from google.adk.agents import Agent
from google.adk.tools import google_search_tool


root_agent=Agent(
    name='QA_Agent',
    model='gemini-2.5-flash',
    description='This agent is for generating the response based on your query',
    instruction='You are helpful assistant, Answer the query in polite and in short summary with in points if required',
    #tools=[google_search_tool]
)