from typing import Annotated, Optional

from fastapi import APIRouter, Query
from fastapi.responses import RedirectResponse

from src.api.dependencies import container
from src.client.google_oauth import GoogleOAuthClient
from src.models.oauth import AuthCode

router = APIRouter(prefix="/callback")


@router.get("/google-oauth2")
async def get_profile_info_from_google_oauth(
    google_oauth_client: Annotated[
        GoogleOAuthClient, container.depends(GoogleOAuthClient)
    ],
    code: AuthCode = Query(AuthCode, alias="code"),
    scope: str = Query(..., alias="scope"),
    state: Optional[str] = Query(None, alias="state"),
):
    access_token_response = google_oauth_client.exchange_auth_code_for_access_token(code)
    # if len(access_token_response.scope.split(" ")) != 3:
    #     return RedirectResponse(url="http://localhost:3000/")
    print(access_token_response.json())

    data2 = google_oauth_client.get_profile_info_using_id_token(access_token_response.id_token)
    print(data2)
    response = RedirectResponse(url="http://localhost:3000/")
    response.set_cookie(key="session", value=access_token_response.access_token)
    return response
