from dapr_agents import OpenAIChatClient
from dotenv import load_dotenv
import os

load_dotenv()
llm = OpenAIChatClient(api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),         
        azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT"))
response = llm.generate("Tell me a joke")
if len(response.get_content())>0:
    print("Got response:", response.get_content())
