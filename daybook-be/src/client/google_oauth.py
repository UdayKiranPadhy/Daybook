from abc import ABC, abstractmethod
import datetime
from logging import Logger
import jwt
import json
from oauth2client.client import OAuth2Credentials


import httpx


from src.client.base import HTTPClient
from src.config import Config
from src.models.oauth import (
    AuthCode,
    AccessToken,
    GoogleOAuthTokenResponse,
    IdToken,
    GoogleProfile,
)


class GoogleOAuthClient(HTTPClient, ABC):
    # TOKEN_ENDPOINT = "https://oauth2.googleapis.com/token"
    TOKEN_ENDPOINT = "https://www.googleapis.com/oauth2/v4/token"

    PROFILE_INFO_ENDPOINT = "https://www.googleapis.com/userinfo/v2/me"
    config: Config

    def __init__(self, client: httpx.Client, logger: Logger, config: Config):
        super().__init__(client, logger)
        self.config = config

    @abstractmethod
    def exchange_auth_code_for_access_token(
        self, auth_code: AuthCode
    ) -> GoogleOAuthTokenResponse:
        pass

    @abstractmethod
    def exchange_auth_code_for_credentials(
        self, auth_code: AuthCode
    ) -> (OAuth2Credentials, GoogleOAuthTokenResponse):
        pass

    @abstractmethod
    def get_profile_info_using_access_token(self, data: AccessToken) -> GoogleProfile:
        pass

    @abstractmethod
    def get_profile_info_using_id_token(self, data: IdToken) -> GoogleProfile:
        pass


class ApiGoogleOAuthClient(GoogleOAuthClient):
    def exchange_auth_code_for_access_token(
        self, auth_code: AuthCode
    ) -> GoogleOAuthTokenResponse:
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

    def exchange_auth_code_for_credentials(
        self, auth_code: AuthCode
    ) -> (OAuth2Credentials, GoogleOAuthTokenResponse):
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
            return (
                OAuth2Credentials.from_json(
                    json.dumps(
                        {
                            "access_token": response.json()["access_token"],
                            "client_id": self.config.google_oauth.client_id,
                            "client_secret": self.config.google_oauth.client_secret,
                            "refresh_token": response.json()["refresh_token"],
                            "token_expiry": str(
                                datetime.datetime.utcnow()
                                + datetime.timedelta(
                                    seconds=response.json()["expires_in"]
                                )
                            ),
                            "token_uri": self.TOKEN_ENDPOINT,
                            "user_agent": "MyApp/1.0 (macOS; Python/3.10; httpx/0.20.0)",
                            "invalid": False,
                        }
                    )
                ),
                GoogleOAuthTokenResponse.model_validate(response.json()),
            )
        except httpx.HTTPError as e:
            self.logger.error(
                "Failed to exchange auth code for access token",
                exc_info=e,
            )
            raise

    def get_profile_info_using_access_token(
        self, access_token: AccessToken
    ) -> GoogleProfile:
        try:
            response = self.http_client.get(
                self.PROFILE_INFO_ENDPOINT,
                headers={"Authorization": f"Bearer {access_token}"},
            )
            return GoogleProfile.model_validate(response.json())
        except httpx.HTTPError as e:
            self.logger.error(
                "Failed to get profile info from Google OAuth2",
                exc_info=e,
            )
            raise

    def get_profile_info_using_id_token(self, id_token: IdToken) -> GoogleProfile:
        decoded_token = jwt.decode(id_token, options={"verify_signature": False})
        return GoogleProfile.model_validate(decoded_token)
