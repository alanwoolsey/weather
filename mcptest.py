import warnings
import asyncio

def suppress_windows_asyncio_pipe_warning():
    if hasattr(asyncio, 'windows_utils'):
        original_fileno = asyncio.windows_utils.PipeHandle.fileno

        def safe_fileno(self):
            try:
                return original_fileno(self)
            except ValueError:
                return -1  # Safe fallback if pipe is already closed

        asyncio.windows_utils.PipeHandle.fileno = safe_fileno

suppress_windows_asyncio_pipe_warning()

from mcp import stdio_client, StdioServerParameters
from strands.tools.mcp.mcp_client import MCPClient
from strands import Agent

params = StdioServerParameters(
    command="python",
    args=["weather.py"]
)

mcp_client = MCPClient(lambda: stdio_client(params))

with mcp_client:
    tools = mcp_client.list_tools_sync()
    print("Discovered tools:", [t.tool_name for t in tools])


    agent = Agent(
        tools=tools,
        system_prompt="You are a helpful assistant."
    )

    response = agent("Can you get the weather for kansas city mo")
    print("Agent response:", response)
