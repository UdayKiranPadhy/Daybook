from abc import ABC, abstractmethod
from logging import Logger
import jwt


import httpx

from src.client.base import HTTPClient
from src.config import Config
from src.models.oauth import AuthCode, AccessToken, GoogleOAuthTokenResponse, IdToken


class GoogleOAuthClient(HTTPClient, ABC):
    # TOKEN_ENDPOINT = "https://oauth2.googleapis.com/token"
    TOKEN_ENDPOINT = "https://www.googleapis.com/oauth2/v4/token"

    PROFILE_INFO_ENDPOINT = "https://www.googleapis.com/userinfo/v2/me"
    config: Config

    def __init__(self, client: httpx.Client, logger: Logger, config: Config):
        super().__init__(client, logger)
        self.config = config

    @abstractmethod
    def exchange_auth_code_for_access_token(self, auth_code: AuthCode) -> GoogleOAuthTokenResponse:
        pass

    @abstractmethod
    def get_profile_info_using_access_token(self, data:AccessToken) -> None:
        pass

    @abstractmethod
    def get_profile_info_using_id_token(self, data: IdToken) -> None:
        pass


class ApiGoogleOAuthClient(GoogleOAuthClient):
    def exchange_auth_code_for_access_token(self, auth_code: AuthCode) -> GoogleOAuthTokenResponse:
        try:
            response = self.http_client.post(
                self.TOKEN_ENDPOINT,
                data={
                    "code": auth_code,
                    "client_id": self.config.google_oauth.client_id,
                    "client_secret": self.config.google_oauth.client_secret,
                    "redirect_uri": f"http://localhost:8000/{self.config.google_oauth.redirect_uri}",
                    "grant_type": "authorization_code",
                },
            )
            return GoogleOAuthTokenResponse.model_validate(response.json())
        except httpx.HTTPError as e:
            self.logger.error(
                "Failed to exchange auth code for access token",
                exc_info=e,
            )
            raise

    def get_profile_info_using_access_token(self, access_token: AccessToken) -> None:
        try:
            response = self.http_client.get(
                self.PROFILE_INFO_ENDPOINT,
                headers={"Authorization": f"Bearer {access_token}"},
            )
            print(response.json())
        except httpx.HTTPError as e:
            self.logger.error(
                "Failed to get profile info from Google OAuth2",
                exc_info=e,
            )
            raise

    def get_profile_info_using_id_token(self, id_token: IdToken) -> None:
        decoded_token = jwt.decode(id_token, options={"verify_signature": False})
        return decoded_token

