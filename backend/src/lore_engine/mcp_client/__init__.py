"""MCP Client module for connecting to and interacting with MCP servers."""

from lore_engine.core import logger, settings
from lore_engine.mcp_client.client import MCPClient


async def get_mcp_client(server_script_path: str | None = None) -> MCPClient:
    """
    Factory function to create and connect an MCP client.

    Args:
        server_script_path: Optional path to the MCP server script.
                          If not provided, uses the path from settings.

    Returns:
        A connected MCPClient instance

    Raises:
        Exception: If connection fails after retries
    """
    script_path = server_script_path or settings.mcp_server_script_path

    logger.info(f"Creating MCP client for server: {script_path}")

    client = MCPClient()
    await client.connect(script_path)

    return client


__all__ = ["MCPClient", "get_mcp_client"]
