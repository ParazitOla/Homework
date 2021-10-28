"""Setup setting for logging."""
import logging
import sys

logger = logging

log_format = "%(levelname)s %(asctime)s %(name)s - %(message)s"
logger.basicConfig(stream=sys.stdout, format=log_format, level=logging.INFO)




