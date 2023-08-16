from online_logger.client import RemoteLogger
import time

rem_logger = RemoteLogger("http://127.0.0.1:8000")


rem_logger.info("Starting processing")

for i in range(10):
    rem_logger.info(f"Processing {i}")
    time.sleep(1)
