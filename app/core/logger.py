from loguru import logger
import os

LOG_PATH = "logs/system.log"

logger.add(
    LOG_PATH,
    rotation="5 MB",
    retention="10 days",
    level="INFO"
)

def get_logger():
    return logger