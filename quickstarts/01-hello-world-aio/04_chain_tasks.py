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
    if len(outline) > 0:
        print("Outline:", outline)
    blog_post = yield ctx.call_activity(write_blog, input=outline)
    if len(blog_post) > 0:
        print("Blog post:", blog_post)
    return blog_post

@task(description="Create a short outline about {topic}")
def create_outline(topic: str) -> str:
    pass

@task(description="Write a short blog post following this outline: {outline}")
def write_blog(outline: str) -> str:
    pass

llm = OpenAIChatClient(api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),         
        azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT"))

if __name__ == '__main__':
    wfapp = WorkflowApp(llm=llm)

    results = wfapp.run_and_monitor_workflow(
        analyze_topic,
        input="AI Agents"
    )
    if len(results) > 0:
        print(f"Result: {results}")
