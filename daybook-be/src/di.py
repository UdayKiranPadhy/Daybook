import logging

import httpx
from lagom import Container, Singleton, dependency_definition
from logtail import LogtailHandler

from src.client.google_oauth import GoogleOAuthClient, ApiGoogleOAuthClient
from src.config import Config


class ContainerBuilder:
    @classmethod
    def get_container(cls) -> Container:
        container = Container()

        container[Config] = Singleton(lambda: Config())

        @dependency_definition(container)  # type: ignore
        def ApiGoogleOAuthClientFactory(c: Container) -> ApiGoogleOAuthClient:
            http_client = httpx.Client()
            logger = c[logging.Logger]
            config = c[Config]
            return ApiGoogleOAuthClient(
                client=http_client, logger=logger, config=config
            )

        container[GoogleOAuthClient] = ApiGoogleOAuthClient  # type: ignore

        @dependency_definition(container, singleton=True)  # type: ignore
        def logger(c: Container) -> logging.Logger:
            handler = LogtailHandler(source_token=c[Config].logging.access_token)
            logger_instance = logging.getLogger(__name__)
            logger_instance.setLevel(logging.INFO)
            logger_instance.handlers = []
            logger_instance.addHandler(handler)
            return logger_instance

        return container
