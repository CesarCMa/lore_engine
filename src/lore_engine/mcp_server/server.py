"""MCP Server implementation for the Lore Engine."""

import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("lore-engine-mcp")


@mcp.tool()
async def fetch_genre() -> str:
    """Fetches a random genre from the Genrenator API."""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get("https://binaryjazz.us/wp-json/genrenator/v1/genre/")
            response.raise_for_status()
            data = response.json()
            if not data:
                raise ValueError("No genre data found")
            return data
    except (httpx.HTTPError, ValueError) as e:
        return f"Error fetching genre: {str(e)}"


@mcp.tool()
async def fetch_story() -> str:
    """Fetches a random story from the Genrenator API."""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get("https://binaryjazz.us/wp-json/genrenator/v1/story/")
            response.raise_for_status()
            data = response.json()
            if not data:
                raise ValueError("No genre data found")
            return data
    except (httpx.HTTPError, ValueError) as e:
        return f"Error fetching story: {str(e)}"


def main() -> None:
    """Run the MCP server."""
    try:
        mcp.run(transport="stdio")
    except Exception as e:
        print(f"Error running MCP server: {str(e)}", flush=True)
        raise


if __name__ == "__main__":
    main()
