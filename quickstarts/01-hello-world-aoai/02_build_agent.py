from dapr_agents import tool, Agent
from dotenv import load_dotenv
from dapr_agents import OpenAIChatClient
import os

load_dotenv()
@tool
def my_weather_func() -> str:
    """Get current weather."""
    return "It's 72°F and sunny"

llm = OpenAIChatClient(api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),         
        azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT"))

weather_agent = Agent(
    name="WeatherAgent",
    role="Weather Assistant",
    instructions=["Help users with weather information"],
    tools=[my_weather_func],
    llm=llm
)

response = weather_agent.run("What's the weather?")
print(response)