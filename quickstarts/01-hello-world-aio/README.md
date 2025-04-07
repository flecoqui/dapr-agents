# Hello World with Dapr Agents based on Azure Open AI

This quickstart provides a hands-on introduction to Dapr Agents through simple examples. You'll learn the fundamentals of working with LLMs, creating basic agents, implementing the ReAct pattern, and setting up simple workflows - all in less than 20 lines of code per example.
In this quickstart, the Azure Open AI service will be accessible through Azure Entra ID authentication without using api key. 

## Installing the pre-requisites

In order to test the solution, you need first an Azure Subscription, you can get further information about Azure Subscription [here](https://azure.microsoft.com/en-us/free).

You also need to install Git client and Visual Studio Code on your machine, below the links.

|[![Windows](./assets/windows_logo.png)](https://git-scm.com/download/win) |[![Linux](./assets/linux_logo.png)](https://git-scm.com/download/linux)|[![MacOS](./assets/macos_logo.png)](https://git-scm.com/download/mac)|
|:---|:---|:---|
| [Git Client for Windows](https://git-scm.com/download/win) | [Git client for Linux](https://git-scm.com/download/linux)| [Git Client for MacOs](https://git-scm.com/download/mac) |
[Visual Studio Code for Windows](https://code.visualstudio.com/Download)  | [Visual Studio Code for Linux](https://code.visualstudio.com/Download)  &nbsp;| [Visual Studio Code for MacOS](https://code.visualstudio.com/Download) &nbsp; &nbsp;|

Once the Git client is installed you can clone the repository on your machine running the following commands:

1. Create a Git directory on your machine

    ```bash
        c:\> mkdir git
        c:\> cd git
        c:\git>
    ```

2. Clone the repository.  
    For instance:

    ```bash
        c:\git> git clone  https://github.com/flecoqui/dapr-agents.git 
        c:\git> cd ./dapr-agent
        c:\git\dapr-agent> 
    ```

## Using Dev Container

### Installing Dev Container pre-requisites

You need to install the following pre-requisite on your machine

1. Install and configure [Docker](https://www.docker.com/get-started) for your operating system.

   - Windows / macOS:

     1. Install [Docker Desktop](https://www.docker.com/products/docker-desktop) for Windows/Mac.

     2. Right-click on the Docker task bar item, select Settings / Preferences and update Resources > File Sharing with any locations your source code is kept. See [tips and tricks](https://code.visualstudio.com/docs/remote/troubleshooting#_container-tips) for troubleshooting.

     3. If you are using WSL 2 on Windows, to enable the [Windows WSL 2 back-end](https://docs.docker.com/docker-for-windows/wsl/): Right-click on the Docker taskbar item and select Settings. Check Use the WSL 2 based engine and verify your distribution is enabled under Resources > WSL Integration.

   - Linux:

     1. Follow the official install [instructions for Docker CE/EE for your distribution](https://docs.docker.com/get-docker/). If you are using Docker Compose, follow the [Docker Compose directions](https://docs.docker.com/compose/install/) as well.

     2. Add your user to the docker group by using a terminal to run: 'sudo usermod -aG docker $USER'

     3. Sign out and back in again so your changes take effect.

2. Ensure [Visual Studio Code](https://code.visualstudio.com/) is already installed.

3. Install the [Remote Development extension pack](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack)

### Using Visual Studio Code and Dev Container

1. Launch Visual Studio Code in the folder where you cloned the 'ps-data-foundation-imv' repository

    ```bash
        c:\git\dapr-agent> code .
    ```

2. Once Visual Studio Code is launched, you should see the following dialog box:

    ![Visual Studio Code](./assets/reopen-in-container.png)

3. Click on the button 'Reopen in Container'
4. Visual Studio Code opens the Dev Container. If it's the first time you open the project in container mode, it first builds the container, it can take several minutes to build the new container.
5. Once the container is loaded, you can open a new terminal (Terminal -> New Terminal).
6. And from the terminal, you have access to the tools installed in the Dev Container like az client. For instance, you can check the version of Azure CLI installed in your dev container.

    ```bash
        vscode ➜ /workspace/dapr-agents $ az --version
    ```

## Connection to Azure

As the samples in this folder require an Azure Open AI service, you need to establish a connection with your Azure subscription.

1. From the dev container terminal, you can establish a connection to your Azure subscription using Azure CLI with the following command:

    ```bash
        vscode ➜ /workspace/dapr-agents $ az login
    ```
2. Once you are connected to Azure you are ready to run the sample in the folder './quickstarts/01-hello-world-aio'

    ```bash
        vscode ➜ /workspace/dapr-agents $ cd ./quickstarts/01-hello-world-aio
        vscode ➜ /workspace/dapr-agents/quickstarts/01-hello-world-aio $ 
    ```
3. You can check python version

    ```bash
        vscode ➜ /workspace/dapr-agents/quickstarts/01-hello-world-aio $ python --version
    ```

4. And the pip version

    ```bash
        vscode ➜ /workspace/dapr-agents/quickstarts/01-hello-world-aio $ pip --version
    ```
5. Finally, install the dapr agent

    ```bash
        vscode ➜ /workspace/dapr-agents/quickstarts/01-hello-world-aio $ pip install -r requirements.txt
    ```

## Configuration

Now, you need to configure the client to use your Azure Open AI infrastructure in setting the following values:

- Azure Open AI endpoint
- Azure Open AI api version
- Azure Open AI deployment name

1. Create a `.env` file in the project root under '/workspace/dapr-agents':

    ```env
    AZURE_OPENAI_ENDPOINT=https://[your_azure_ai_foundry_project_name_here].openai.azure.com/
    AZURE_OPENAI_API_VERSION="your_azure_open_ai_api_version_here"
    AZURE_OPENAI_DEPLOYMENT="your_azure_ai_foundry_deployment_name_here"
    ```

    Replace `your_azure_ai_foundry_project_name_here` with your actual Azure AI Foundry project name.
    Replace `your_azure_open_ai_api_version_here` with your current Azure Open AI service api version.
    Replace `your_azure_ai_foundry_deployment_name_here` with your model deployment name in your Azure AI Foundry project.

## Examples

### 1. Basic LLM Usage

Run the basic LLM example to see how to interact with OpenAI's language models:

<!-- STEP
name: Run basic LLM example
expected_stdout_lines:
  - "Got response:"
timeout_seconds: 30
output_match_mode: substring
-->
```bash
python 01_ask_llm.py
```
<!-- END_STEP -->

This example demonstrates the simplest way to use Dapr Agents' OpenAIChatClient:

```python
from dapr_agents import OpenAIChatClient
from dotenv import load_dotenv

load_dotenv()
llm = OpenAIChatClient(api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),         
        azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT"))
response = llm.generate("Tell me a joke")
print("Got response:", response.get_content())
```

**Expected output:** The LLM will respond with a joke.

### 2. Simple Agent with Tools

Run the agent example to see how to create an agent with custom tools:

<!-- STEP
name: Run simple agent with tools example
expected_stdout_lines:
  - "user:"
  - "What's the weather?"
  - "assistant:"
  - "Function name: MyWeatherFunc"
  - "MyWeatherFunc(tool)"
  - "It's 72°F and sunny"
  - "assistant:"
  - "The current weather is 72°F and sunny."
timeout_seconds: 30
output_match_mode: substring
-->
```bash
python 02_build_agent.py
```
<!-- END_STEP -->

This example shows how to create a basic agent with a custom tool:

```python
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
```

**Expected output:** The agent will use the weather tool to provide the current weather.

### 3. ReAct Pattern Implementation

Run the ReAct pattern example to see how to create an agent that can reason and act:

<!-- STEP
name: Run simple agent with tools example
expected_stdout_lines:
  - "user:"
  - "What should I do in London today?"
  - "Thought:"
  - 'Action: {"name": "SearchWeather", "arguments": {"city": "London"}}'
  - "Observation: rainy"
  - "Thought:"
  - 'Action: {"name": "GetActivities", "arguments": {"weather": "rainy"}}'
  - "Observation: Visit museums"
  - "Thought:"
  - "assistant:"
  - "Result:"
timeout_seconds: 30
output_match_mode: substring
-->
```bash
python 03_reason_act.py
```
<!-- END_STEP -->

```python
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
    activities = {"rainy": "Visit museums", "Sunny": "Go hiking"}
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

react_agent.run("What should I do in London today?")
```

**Expected output:** The agent will first check the weather in London, find it's rainy, and then recommend visiting museums.

### 4. Simple Workflow

Make sure Dapr is initialized on your system:

```bash
dapr init
```

Run the workflow example to see how to create a multi-step LLM process:

<!-- STEP
name: Run a simple workflow example
expected_stdout_lines:
  - "Outline:"
  - "Blog post:"
  - "Result:"
output_match_mode: substring
-->
```bash
dapr run --app-id dapr-agent-wf -- python 04_chain_tasks.py
```
<!-- END_STEP -->

This example demonstrates how to create a workflow with multiple tasks:

```python
from dapr_agents.workflow import WorkflowApp, workflow, task
from dapr_agents.types import DaprWorkflowContext
from dotenv import load_dotenv
from dapr_agents import OpenAIChatClient
import os

load_dotenv()

@workflow(name='analyze_topic')
def analyze_topic(ctx: DaprWorkflowContext, topic: str):
    # Each step is durable and can be retried
    outline = yield ctx.call_activity(create_outline, input=topic)
    blog_post = yield ctx.call_activity(write_blog, input=outline)
    return blog_post

@task(description="Create a detailed outline about {topic}")
def create_outline(topic: str) -> str:
    pass

@task(description="Write a comprehensive blog post following this outline: {outline}")
def write_blog(outline: str) -> str:
    pass

if __name__ == '__main__':
    wfapp = WorkflowApp(llm=llm)

    results = wfapp.run_and_monitor_workflow(
        analyze_topic,
        input="AI Agents"
    )
    print(f"Result: {results}")
```

**Expected output:** The workflow will create an outline about AI Agents and then generate a blog post based on that outline.

## Key Concepts

- **OpenAIChatClient**: The interface for interacting with OpenAI's LLMs
- **Agent**: A class that combines an LLM with tools and instructions
- **@tool decorator**: A way to create tools that agents can use
- **ReActAgent**: An agent that follows the Reasoning + Action pattern
- **WorkflowApp**: A Dapr-powered way to create stateful, multi-step processes

## Dapr Integration

These examples don't directly expose Dapr building blocks, but they're built on Dapr Agents which behind the scenes leverages the full capabilities of the Dapr runtime:

- **Resilience**: Built-in retry policies, circuit breaking, and timeout handling external systems interactions
- **Orchestration**: Stateful, durable workflows that can survive process restarts and continue execution from where they left off
- **Interoperability**: Pluggable component architecture that works with various backends and cloud services without changing application code
- **Scalability**: Distribute agents across infrastructure, from local development to multi-node Kubernetes clusters
- **Event-Driven**: Pub/Sub messaging for event-driven agent collaboration and coordination
- **Observability**: Integrated distributed tracing, metrics collection, and logging for visibility into agent operations
- **Security**: Protection through scoping, encryption, secret management, and authentication/authorization controls

In the later quickstarts, you'll see explicit Dapr integration through state stores, pub/sub, and workflow services.

## Troubleshooting

1. **API Key Issues**: If you see an authentication error, verify your OpenAI API key in the `.env` file
2. **Python Version**: If you encounter compatibility issues, make sure you're using Python 3.10+
3. **Environment Activation**: Ensure your virtual environment is activated before running examples
4. **Import Errors**: If you see module not found errors, verify that `pip install -r requirements.txt` completed successfully

## Next Steps

After completing these examples, move on to the [LLM Call quickstart](../02_llm_call_open_ai/README.md) to learn more about structured outputs from LLMs.