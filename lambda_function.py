import warnings
import asyncio

def suppress_windows_asyncio_pipe_warning():
    if hasattr(asyncio, 'windows_utils'):
        original_fileno = asyncio.windows_utils.PipeHandle.fileno

        def safe_fileno(self):
            try:
                return original_fileno(self)
            except ValueError:
                return -1

        asyncio.windows_utils.PipeHandle.fileno = safe_fileno

suppress_windows_asyncio_pipe_warning()

from mcp import stdio_client, StdioServerParameters
from strands.tools.mcp.mcp_client import MCPClient
from strands import Agent

def lambda_handler(event, context):
    location = event.get("location", "kansas city mo")

    params = StdioServerParameters(command="python", args=["weather.py"])
    mcp_client = MCPClient(lambda: stdio_client(params))

    with mcp_client:
        tools = mcp_client.list_tools_sync()
        agent = Agent(tools=tools, system_prompt="You are a helpful assistant.")
        response = agent(f"Can you get the weather for {location}")

    return {
    "statusCode": 200,
    "body": str(response)
}
