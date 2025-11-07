"""Configuration settings for the Lore Engine application."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    openai_api_key: str
    mcp_server_script_path: str = "src/lore_engine/mcp_server/server.py"
    log_level: str = "INFO"
    openai_model: str = "gpt-4o-mini"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
