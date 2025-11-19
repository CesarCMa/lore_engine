"""Entry point for lore_engine package."""

import uvicorn


def main():
    """Run the FastAPI application."""
    uvicorn.run(
        "lore_engine.api.app:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info",
    )


if __name__ == "__main__":
    main()
