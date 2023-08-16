"""Creates system wide client and file loggers."""

# Standard Imports
from logging.handlers import RotatingFileHandler
from logging import StreamHandler
import logging.config
import logging

# External Imports
import os

# Internal Imports
from online_logger.utils.paths import LOGS_FOLDER


def activate_logger():
    """
    Activates loggers in the desired format

    Will start a client logger with INFO level, and file logger with DEBUG level
    File logger will save files in the logs folder (top level)
    """

    # Silence Requests logger
    logging.getLogger("requests").setLevel(60)

    log_file_path = os.path.join(LOGS_FOLDER, "log.log")
    log_format = "[%(asctime)s] [%(levelname)s] - %(message)s"
    logger_formatter = logging.Formatter(log_format)

    # Sets up rotating file handler for file output
    file_logger = RotatingFileHandler(
        log_file_path, maxBytes=1024 * 1024 * 10, backupCount=10
    )
    file_logger.setLevel(logging.DEBUG)
    file_logger.setFormatter(logger_formatter)

    # Set up stream handler for client output
    client_logger = StreamHandler()
    client_logger.setLevel(logging.INFO)
    client_logger.setFormatter(logger_formatter)

    logger = logging.getLogger()
    logger.setLevel("DEBUG")
    logger.addHandler(client_logger)
    logger.addHandler(file_logger)
