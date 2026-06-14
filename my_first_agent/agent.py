from google.adk.agents import Agent

def get_weather_tool(city:str)->dict:
    """
    Description:
    'This fucntion tool retrieves the weather details of the particular city'

    Args:
        city: It takes input as city of type string to get weather for.
    Returns:
        It returns a dictionary conatining the weather status and temperature    
    
    """
    return {
        "status":"success",
        "Temperature":" The temperature is not available for the current city"
    }

root_agent=Agent(
    name='QA_Agent',
    model='gemini-2.5-flash',
    description='This agent is for generating the response based on your query',
    instruction='You are helpful assistant, Answer the query in polite and in short summary with in points if required',
    tools=[get_weather_tool]
)