"""FastAPI application for the Lore Engine API."""

from datetime import UTC, datetime
from typing import Any

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from lore_engine.core.logging import logger

app = FastAPI(
    title="Lore Engine",
    version="0.1.0",
    description="A worldbuilding lore generation API powered by LLMs and MCP tools. "
    "Generate rich factions and quests for tabletop RPGs and video games.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (configure for production)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health", tags=["health"])
async def health_check() -> dict[str, Any]:
    """Health check endpoint to verify API is running.

    Returns:
        Status information with timestamp
    """
    return {
        "status": "healthy",
        "timestamp": datetime.now(UTC).isoformat(),
        "service": "lore-engine",
        "version": "0.1.0",
    }


from lore_engine.api.routes import factions, quests  # noqa: E402

app.include_router(factions.router)
app.include_router(quests.router)

logger.info("FastAPI application initialized")
