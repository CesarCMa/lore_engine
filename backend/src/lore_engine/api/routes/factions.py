"""Factions API endpoints."""

from fastapi import APIRouter, Depends, HTTPException, Path

from lore_engine.api.dependencies import get_mcp_client
from lore_engine.core.logging import logger
from lore_engine.mcp_client.client import MCPClient
from lore_engine.models.responses import FactionResponse, FactionsResponse
from lore_engine.services import create_lore_generator

router = APIRouter(prefix="/factions", tags=["factions"])


@router.get("/{count}", response_model=FactionsResponse)
async def generate_factions(
    count: int = Path(ge=1, le=10, description="Number of factions to generate (1-10)"),
    mcp_client: MCPClient = Depends(get_mcp_client),
) -> FactionsResponse:
    """Generate multiple factions for worldbuilding.

    Args:
        count: Number of factions to generate (between 1 and 10)
        mcp_client: MCP client instance (injected)

    Returns:
        FactionsResponse containing list of generated factions

    Raises:
        HTTPException: If generation fails
    """
    try:
        logger.info(f"Received request to generate {count} faction(s)")

        lore_generator = await create_lore_generator(mcp_client)

        factions_data = await lore_generator.generate_faction(count=count)

        faction_responses = [FactionResponse(**faction) for faction in factions_data]

        logger.info(f"Successfully generated {len(faction_responses)} faction(s)")
        return FactionsResponse(factions=faction_responses)

    except Exception as e:
        logger.error(f"Failed to generate factions: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Failed to generate factions: {str(e)}") from e
