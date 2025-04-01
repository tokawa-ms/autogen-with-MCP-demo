import asyncio
import os
from dotenv import load_dotenv
from pathlib import Path
from autogen_ext.models.openai import AzureOpenAIChatCompletionClient
from autogen_ext.tools.mcp import StdioServerParams, mcp_server_tools
from autogen_agentchat.agents import AssistantAgent
from autogen_core import CancellationToken

# read environment variables from .env file
load_dotenv()

model_client = AzureOpenAIChatCompletionClient(
    azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    model=os.getenv("AZURE_OPENAI_MODEL"),
)


# main function to run the agent
async def main() -> None:
    # Set up the MCP server parameters
    # mcp/filesystem is a docker image that runs a filesystem server
    # It mounts the D:/mcpdir directory to /projects/mcpdir in the container
    server_params = StdioServerParams(
        command="docker",
        args=[
            "run",
            "-i",
            "--rm",
            "--mount",
            "type=bind,src=D:/mcpdir,dst=/projects/mcpdir",
            "mcp/filesystem",
            "/projects",
        ],
    )

    # Get all available tools from the server
    tools = await mcp_server_tools(server_params)

    # Create an agent that can use all the tools
    agent = AssistantAgent(
        name="file_manager",
        model_client=model_client,
        tools=tools,
    )

    # Output of the agents is printed to the console
    print(
        # The agent can now use any of the filesystem tools
        await agent.run(
            task="Create a file called /projects/mcpdir/test.txt with some content",
            cancellation_token=CancellationToken(),
        )
    )


# must use asyncio.run to run the main function
# because main() is an async function
if __name__ == "__main__":
    asyncio.run(main())
