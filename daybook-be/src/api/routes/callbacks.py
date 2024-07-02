from logging import Logger
from typing import Annotated

from fastapi import APIRouter, Query
from fastapi.responses import RedirectResponse

from src.api.dependencies import container
from src.client.google_oauth import GoogleOAuthClient
from src.models.oauth import AuthCode

router = APIRouter(prefix="/callback")


@router.get("/google-oauth2")
async def get_profile_info_from_google_oauth(
    auth_code: Annotated[AuthCode, Query(alias="code")],
    logger: Annotated[Logger, container.depends(Logger)],
    google_oauth_client: Annotated[
        GoogleOAuthClient, container.depends(GoogleOAuthClient)
    ],
    state: Annotated[str | None, Query(alias="state")] = None,
) -> RedirectResponse:
    access_token = google_oauth_client.exchange_auth_code_for_access_token(auth_code)
    google_oauth_client.get_profile_info(access_token)
    response = RedirectResponse(url="http://localhost:3000/")
    response.set_cookie(key="session", value=access_token)
    return response
