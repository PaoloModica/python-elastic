import json
import logging
from logging import Logger

from config import Settings


class JSONFormatter(logging.Formatter):
    def __init__(self):
        super.__init__()

    def format(self, record):
        record.msg = json.dumps(record.msg)
        return super.format(record.msg)


def create_logger(settings: Settings) -> Logger:
    # == logging configuration ==
    logging_config = settings.dict(include={"logger_level", "datefmt"})
    logging.basicConfig(**logging_config)
    # == logging stream handler ==
    json_handler = logging.StreamHandler()
    json_handler.setFormatter(JSONFormatter())
    # == logger object ==
    logger = logging.getLogger(__name__)
    logger.addHandler(json_handler)
    return logger
