import asyncio
import os
from dotenv import load_dotenv
from pathlib import Path
from autogen_ext.models.openai import AzureOpenAIChatCompletionClient
from autogen_ext.tools.mcp import StdioServerParams, mcp_server_tools
from autogen_agentchat.agents import AssistantAgent
from autogen_core import CancellationToken

# .env ファイルから環境変数を読み込む
load_dotenv()

model_client = AzureOpenAIChatCompletionClient(
    azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    model=os.getenv("AZURE_OPENAI_MODEL"),
)


async def main() -> None:
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
        tools=tools,  # type: ignore
    )

    # The agent can now use any of the filesystem tools
    print(
        await agent.run(
            task="Create a file called /projects/mcpdir/test.txt with some content",
            cancellation_token=CancellationToken(),
        )
    )


if __name__ == "__main__":
    asyncio.run(main())
