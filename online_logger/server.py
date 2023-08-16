"""Server for logging messages"""

from fastapi import FastAPI
from pydantic import BaseModel
import logging
from online_logger.utils.logging import activate_logger


app = FastAPI()

# Configuring the logging
activate_logger()


class LogItem(BaseModel):
    level: str
    message: str


@app.post("/log")
def log_item(item: LogItem):
    log_method = getattr(
        logging, item.level, logging.info
    )  # Default to INFO if level is unknown
    log_method(item.message)
    return {"status": "success"}
