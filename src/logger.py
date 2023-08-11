import json
import logging

from src.config import Settings


class JSONFormatter(logging.Formatter):
    def __init__(self):
        super().__init__()

    def format(self, record):
        record.msg = json.dumps(record.msg)
        return super.format(record.msg)


def create_logger(settings: Settings) -> logging.Logger:
    # == logging configuration ==
    logging.basicConfig(
        datefmt=settings.datefmt,
        level=getattr(logging, settings.logger_level, logging.INFO),
    )
    # == logging stream handler ==
    json_handler = logging.StreamHandler()
    json_handler.setFormatter(JSONFormatter())
    # == logger object ==
    logger = logging.getLogger(__name__)
    logger.addHandler(json_handler)
    return logger
