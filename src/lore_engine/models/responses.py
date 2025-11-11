"""Response models for the Lore Engine API."""

from pydantic import BaseModel, Field


class FactionResponse(BaseModel):
    """Response model for a single faction."""

    name: str = Field(..., description="The faction's name")
    symbol: str = Field(..., description="Description of the faction's symbol or emblem")
    values: str = Field(..., description="Core beliefs and values of the faction")
    soundtrack_vibe: str = Field(..., description="Musical genre/style that represents the faction")


class FactionsResponse(BaseModel):
    """Response model for multiple factions."""

    factions: list[FactionResponse] = Field(..., description="List of generated factions")


class QuestResponse(BaseModel):
    """Response model for a quest."""

    title: str = Field(..., description="The quest title")
    quest_brief: str = Field(..., description="Brief description of the quest")
    npcs: str = Field(..., description="Key NPCs involved in the quest")
    conflict: str = Field(..., description="The main conflict or challenge")
    location: str = Field(..., description="Where the quest takes place")
