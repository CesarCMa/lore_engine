"""Quests API endpoints."""

from fastapi import APIRouter, Depends, HTTPException

from lore_engine.api.dependencies import get_mcp_client
from lore_engine.core.logging import logger
from lore_engine.mcp_client.client import MCPClient
from lore_engine.models.responses import QuestResponse
from lore_engine.services import create_lore_generator

router = APIRouter(prefix="/quests", tags=["quests"])


@router.get("/", response_model=QuestResponse)
async def generate_quest(
    mcp_client: MCPClient = Depends(get_mcp_client),
) -> QuestResponse:
    """Generate a quest for worldbuilding.

    Args:
        mcp_client: MCP client instance (injected)

    Returns:
        QuestResponse containing the generated quest

    Raises:
        HTTPException: If generation fails
    """
    try:
        logger.info("Received request to generate quest")

        lore_generator = await create_lore_generator(mcp_client)
        quest_data = await lore_generator.generate_quest()
        quest_response = QuestResponse(**quest_data)

        logger.info("Successfully generated quest")
        return quest_response

    except Exception as e:
        logger.error(f"Failed to generate quest: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Failed to generate quest: {str(e)}") from e
