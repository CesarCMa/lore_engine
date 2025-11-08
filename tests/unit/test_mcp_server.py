"""Tests for MCP server tools."""

from unittest.mock import AsyncMock, patch

import pytest

from lore_engine.mcp_server.server import fetch_genre, fetch_story


@pytest.mark.asyncio
async def test_fetch_genre_returns_string():
    """Test that fetch_genre() returns a string."""
    with patch("lore_engine.mcp_server.server.httpx.AsyncClient") as mock_client:
        mock_response = AsyncMock()
        mock_response.json = lambda: "triangle video game listening"
        mock_response.raise_for_status = lambda: None

        mock_async_client = AsyncMock()
        mock_async_client.__aenter__.return_value = mock_async_client
        mock_async_client.__aexit__.return_value = None
        mock_async_client.get = AsyncMock(return_value=mock_response)

        mock_client.return_value = mock_async_client

        result = await fetch_genre()

        assert isinstance(result, str)
        assert result == "triangle video game listening"


@pytest.mark.asyncio
async def test_fetch_genre_handles_missing_name():
    """Test that fetch_genre() handles missing 'name' key gracefully."""
    with patch("lore_engine.mcp_server.server.httpx.AsyncClient") as mock_client:
        # Mock response without 'name' key
        mock_response = AsyncMock()
        mock_response.json = lambda: {}
        mock_response.raise_for_status = lambda: None

        mock_async_client = AsyncMock()
        mock_async_client.__aenter__.return_value = mock_async_client
        mock_async_client.__aexit__.return_value = None
        mock_async_client.get = AsyncMock(return_value=mock_response)

        mock_client.return_value = mock_async_client

        result = await fetch_genre()

        assert isinstance(result, str)
        assert "Error fetching genre:" in result


@pytest.mark.asyncio
async def test_fetch_genre_handles_http_error():
    """Test that fetch_genre() handles HTTP errors gracefully."""
    import httpx

    with patch("lore_engine.mcp_server.server.httpx.AsyncClient") as mock_client:
        mock_async_client = AsyncMock()
        mock_async_client.__aenter__.return_value = mock_async_client
        mock_async_client.__aexit__.return_value = None
        mock_async_client.get = AsyncMock(side_effect=httpx.ConnectError("Connection failed"))

        mock_client.return_value = mock_async_client

        result = await fetch_genre()

        assert isinstance(result, str)
        assert "Error fetching genre:" in result


@pytest.mark.asyncio
async def test_fetch_story_returns_string():
    """Test that fetch_story() returns a string."""
    with patch("lore_engine.mcp_server.server.httpx.AsyncClient") as mock_client:
        # Mock the async context manager and response
        mock_response = AsyncMock()
        mock_response.json = lambda: "You're never too old to listen to israeli ska."
        mock_response.raise_for_status = lambda: None

        mock_async_client = AsyncMock()
        mock_async_client.__aenter__.return_value = mock_async_client
        mock_async_client.__aexit__.return_value = None
        mock_async_client.get = AsyncMock(return_value=mock_response)

        mock_client.return_value = mock_async_client

        result = await fetch_story()

        assert isinstance(result, str)
        assert result == "You're never too old to listen to israeli ska."


@pytest.mark.asyncio
async def test_fetch_story_handles_missing_name():
    """Test that fetch_story() handles missing 'name' key gracefully."""
    with patch("lore_engine.mcp_server.server.httpx.AsyncClient") as mock_client:
        # Mock response without 'name' key
        mock_response = AsyncMock()
        mock_response.json = lambda: {}
        mock_response.raise_for_status = lambda: None

        mock_async_client = AsyncMock()
        mock_async_client.__aenter__.return_value = mock_async_client
        mock_async_client.__aexit__.return_value = None
        mock_async_client.get = AsyncMock(return_value=mock_response)

        mock_client.return_value = mock_async_client

        result = await fetch_story()

        assert isinstance(result, str)
        assert "Error fetching story:" in result


@pytest.mark.asyncio
async def test_fetch_story_handles_http_error():
    """Test that fetch_story() handles HTTP errors gracefully."""
    import httpx

    with patch("lore_engine.mcp_server.server.httpx.AsyncClient") as mock_client:
        mock_async_client = AsyncMock()
        mock_async_client.__aenter__.return_value = mock_async_client
        mock_async_client.__aexit__.return_value = None
        mock_async_client.get = AsyncMock(side_effect=httpx.ConnectError("Connection failed"))

        mock_client.return_value = mock_async_client

        result = await fetch_story()

        assert isinstance(result, str)
        assert "Error fetching story:" in result
