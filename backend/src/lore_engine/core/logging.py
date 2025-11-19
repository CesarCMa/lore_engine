"""Logging configuration for the Lore Engine application."""

import logging

from lore_engine.core.config import settings

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=settings.log_level,
)

logger = logging.getLogger("lore_engine")
