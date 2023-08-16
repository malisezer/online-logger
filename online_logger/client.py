"""Online logger code used for sending requests to a remote server."""

import requests
import warnings


class RemoteLogger:
    """Remote logger class."""

    def __init__(self, target_ip):
        self.target_ip = target_ip

    def _log(self, level, message):
        payload = {"level": level, "message": message}

        try:
            response = requests.post(f"{self.target_ip}/log", json=payload, timeout=1)
            if response.status_code != 200:
                warnings.warn(
                    f"Failed to send log to {self.target_ip}: {response.text}"
                )
        except requests.Timeout:
            warnings.warn(f"Logging timed out")
        except requests.ConnectionError:
            warnings.warn(f"Logging failed to connect to {self.target_ip}")
        except Exception as e:
            warnings.warn(f"Logging failed: {e}")

    def debug(self, message):
        self._log("debug", message)

    def info(self, message):
        self._log("info", message)

    def warning(self, message):
        self._log("warning", message)

    def error(self, message):
        self._log("error", message)

    def critical(self, message):
        self._log("critical", message)
