"""Handles creation of loggers."""

from __future__ import annotations

import logging
import sys

formatter: logging.Formatter | None = None
console_handler: logging.Handler | None = None
root_logger: logging.Logger | None = None


def _init_root() -> None:
    import your_module

    global formatter
    global console_handler
    global root_logger

    formatter = logging.Formatter(
        fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %I:%M:%S",  # yyyy-MM-dd HH:mm:ss
        style="%",
        validate=True,
    )

    console_handler = logging.StreamHandler(stream=sys.stdout)
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.INFO)

    root_logger = logging.getLogger(your_module.__name__)
    root_logger.propagate = True
    root_logger.setLevel(logging.DEBUG)
    root_logger.handlers = [console_handler]


def get_logger(name: str) -> logging.Logger:
    """Get a logging.Logger object.

    Gets a logging.Logger object whose parent is the root logger for this module.

    This is typically called once per file with the arguments __name__.

    :param name: The name of the logger, usually __name__.
    :return: The logging.Logger object.
    """
    if root_logger is None:
        _init_root()
    logger = logging.getLogger(name)
    logger.parent = root_logger
    return logger
