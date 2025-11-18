"""Response models for the Lore Engine API."""

from typing import Any

from pydantic import BaseModel, Field, field_validator


class FactionResponse(BaseModel):
    """Response model for a single faction."""

    name: str = Field(..., description="The faction's name")
    symbol: str = Field(..., description="Description of the faction's symbol or emblem")
    values: str = Field(..., description="Core beliefs and values of the faction")
    soundtrack_vibe: str = Field(..., description="Musical genre/style that represents the faction")


class FactionsResponse(BaseModel):
    """Response model for multiple factions."""

    factions: list[FactionResponse] = Field(..., description="List of generated factions")


class NPC(BaseModel):
    """Model for an NPC in a quest."""

    name: str = Field(..., description="The NPC's name")
    role: str = Field(..., description="The NPC's role in the quest")
    description: str | None = Field(None, description="Additional description of the NPC")


class QuestResponse(BaseModel):
    """Response model for a quest."""

    title: str = Field(..., description="The quest title")
    quest_brief: str = Field(..., description="Brief description of the quest")
    npcs: list[NPC] | str = Field(..., description="Key NPCs involved in the quest")
    conflict: str = Field(..., description="The main conflict or challenge")
    location: str = Field(..., description="Where the quest takes place")

    @field_validator("npcs", mode="before")
    @classmethod
    def validate_npcs(cls, v: Any) -> list[NPC] | str:
        """Convert NPCs to proper format if needed."""
        if isinstance(v, str):
            return v
        elif isinstance(v, list):
            npcs = []
            for npc in v:
                if isinstance(npc, dict):
                    npcs.append(NPC(**npc))
                elif isinstance(npc, NPC):
                    npcs.append(npc)
                else:
                    return str(v)
            return npcs
        else:
            return str(v)
