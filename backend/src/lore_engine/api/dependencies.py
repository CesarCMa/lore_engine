"""Dependency injection functions for FastAPI."""

from lore_engine.core.config import settings
from lore_engine.core.logging import logger
from lore_engine.mcp_client import get_mcp_client as create_mcp_client
from lore_engine.mcp_client.client import MCPClient


async def get_mcp_client() -> MCPClient:
    """Get or create an MCP client instance.

    Yields:
        Connected MCP client instance
    """
    logger.info("Creating MCP client for request")
    mcp_client = await create_mcp_client(settings.mcp_server_script_path)
    try:
        yield mcp_client
    finally:
        # Cleanup after request
        await mcp_client.cleanup()
        logger.info("Cleaned up MCP client after request")
