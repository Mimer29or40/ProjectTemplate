"""Entry point when executing this your_module."""

from __future__ import annotations

import your_module
from your_module.log import get_logger

logger = get_logger(__name__)

if __name__ == "__main__":
    logger.info("Running Package:\n\t%s", your_module.__name__)
