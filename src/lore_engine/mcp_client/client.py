"""MCP Client wrapper for managing connections to MCP servers."""

from contextlib import AsyncExitStack
from typing import Any

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from tenacity import retry, stop_after_attempt, wait_exponential

from lore_engine.core import logger


class MCPClient:
    """Wrapper class for managing MCP server connections and tool calls."""

    def __init__(self) -> None:
        """Initialize the MCP client."""
        self.session: ClientSession | None = None
        self.exit_stack: AsyncExitStack | None = None
        self.is_connected: bool = False

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=1, max=10))
    async def connect(self, server_script_path: str) -> None:
        """
        Connect to an MCP server using stdio transport.

        Args:
            server_script_path: Path to the MCP server script to execute

        Raises:
            Exception: If connection or initialization fails
        """
        try:
            logger.info(f"Connecting to MCP server at {server_script_path}")

            # Convert file path to module path if needed
            # e.g., "src/lore_engine/mcp_server/server.py" -> "lore_engine.mcp_server.server"
            if server_script_path.endswith(".py"):
                module_path = (
                    server_script_path.replace("/", ".").replace("src.", "").replace(".py", "")
                )
            else:
                module_path = server_script_path

            server_params = StdioServerParameters(
                command="poetry", args=["run", "python", "-m", module_path]
            )
            self.exit_stack = AsyncExitStack()
            stdio_transport = await self.exit_stack.enter_async_context(stdio_client(server_params))
            read_stream, write_stream = stdio_transport
            self.session = await self.exit_stack.enter_async_context(
                ClientSession(read_stream, write_stream)
            )
            await self.session.initialize()

            self.is_connected = True
            logger.info("Successfully connected to MCP server")

        except Exception as e:
            logger.error(f"Failed to connect to MCP server: {e}")
            if self.exit_stack:
                await self.exit_stack.aclose()
            raise

    async def list_tools(self) -> list[dict[str, Any]]:
        """
        List all available tools from the connected MCP server.

        Returns:
            List of tool definitions with names, descriptions, and input schemas

        Raises:
            RuntimeError: If not connected to server
            Exception: If listing tools fails
        """
        if not self.is_connected or not self.session:
            raise RuntimeError("Not connected to MCP server. Call connect() first.")

        try:
            logger.info("Listing available tools from MCP server")
            response = await self.session.list_tools()

            tools = []
            for tool in response.tools:
                tools.append(
                    {
                        "name": tool.name,
                        "description": tool.description,
                        "inputSchema": tool.inputSchema,
                    }
                )

            logger.info(f"Found {len(tools)} available tools")
            return tools

        except Exception as e:
            logger.error(f"Failed to list tools: {e}")
            raise

    async def call_tool(self, tool_name: str, arguments: dict[str, Any] | None = None) -> Any:
        """
        Call a specific tool on the connected MCP server.

        Args:
            tool_name: Name of the tool to call
            arguments: Dictionary of arguments to pass to the tool

        Returns:
            The result content from the tool execution

        Raises:
            RuntimeError: If not connected to server
            Exception: If tool call fails
        """
        if not self.is_connected or not self.session:
            raise RuntimeError("Not connected to MCP server. Call connect() first.")

        try:
            logger.info(f"Calling tool '{tool_name}' with arguments: {arguments}")
            result = await self.session.call_tool(tool_name, arguments or {})

            logger.info(f"Tool '{tool_name}' executed successfully")
            return result.content

        except Exception as e:
            logger.error(f"Failed to call tool '{tool_name}': {e}")
            raise

    async def cleanup(self) -> None:
        """
        Clean up resources and close connections.

        This should be called when the client is no longer needed.
        """
        try:
            if self.exit_stack:
                logger.info("Cleaning up MCP client resources")
                await self.exit_stack.aclose()
                self.is_connected = False
                self.session = None
                self.exit_stack = None
                logger.info("MCP client cleanup complete")
        except Exception as e:
            logger.error(f"Error during cleanup: {e}")
            raise
