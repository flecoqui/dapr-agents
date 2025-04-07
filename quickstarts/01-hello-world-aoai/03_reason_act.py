from dapr_agents import tool, ReActAgent
from dotenv import load_dotenv
from dapr_agents import OpenAIChatClient
import os

load_dotenv()
@tool
def search_weather(city: str) -> str:
    """Get weather information for a city."""
    weather_data = {"london": "rainy", "paris": "sunny"}
    return weather_data.get(city.lower(), "Unknown")

@tool
def get_activities(weather: str) -> str:
    """Get activity recommendations."""
    activities = {"rainy": "Visit museums", "sunny": "Go hiking"}
    return activities.get(weather.lower(), "Stay comfortable")

llm = OpenAIChatClient(api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),         
        azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT"))

react_agent = ReActAgent(
    name="TravelAgent",
    role="Travel Assistant",
    instructions=["Check weather, then suggest activities"],
    tools=[search_weather, get_activities],
    llm=llm
)

result = react_agent.run("What should I do in London today?")

if len(result) > 0:
    print ("Result:", result)