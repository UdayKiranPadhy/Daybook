from abc import ABC
from logging import Logger

import httpx


class HTTPClient(ABC):
    http_client: httpx.Client
    logger: Logger

    def __init__(self, http_client: httpx.Client, logger: Logger):
        self.http_client = http_client
        self.logger = logger

        if len(self.http_client.event_hooks["response"]) == 0:
            # enforce a hook that makes sure we always raise on 4xx and 5xx errors
            # but don't overwrite user settings if hooks already exist
            def log_and_raise_error(response: httpx.Response) -> None:
                if not response.is_success:
                    self.logger.error(
                        "HTTP error:\n\nURL: %s\n\nrequest:\n%s\n\nresponse:\n%s",
                        response.request.url,
                        response.request.read(),
                        response.read(),
                    )
                    response.raise_for_status()

            self.http_client.event_hooks["response"] = [
                log_and_raise_error,
            ]
