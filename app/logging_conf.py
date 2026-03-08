import logging
from pythonjsonlogger.json import JsonFormatter


def setup_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    if logger.handlers:
        logger.handlers.clear()

    handler = logging.StreamHandler()
    formatter = JsonFormatter()

    handler.setFormatter(formatter)
    logger.addHandler(handler)