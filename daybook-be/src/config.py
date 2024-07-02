from pydantic import Field, BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class LoggingConfig(BaseSettings):
    access_token: str
    model_config = SettingsConfigDict(env_file=".env", env_prefix="LOGGING_")


class GoogleOauthConfig(BaseSettings):
    client_id: str
    client_secret: str
    redirect_uri: str
    model_config = SettingsConfigDict(env_file=".env", env_prefix="GOOGLE_OAUTH2_")


class Config(BaseModel):
    """
    Loads application config from the environment using pydantic.BaseSettings, split up
    into different "modules" with different environment variable prefixes.
    """

    logging: LoggingConfig = Field(default_factory=lambda: LoggingConfig())
    google_oauth: GoogleOauthConfig = Field(default_factory=lambda: GoogleOauthConfig())


_config: Config | None = None


class ConfigProvider:
    @classmethod
    def get_config(cls) -> Config:
        global _config
        if _config is None:
            _config = Config()
        return _config


class FakeConfigProvider:
    @classmethod
    def get_config(cls) -> Config:
        logging = LoggingConfig(access_token="fake_token")
        google_oauth = GoogleOauthConfig(
            client_id="fake_client_id",
            client_secret="fake_client_secret",
            redirect_uri="fake_redirect_uri",
        )

        return Config(logging=logging, google_oauth=google_oauth)
