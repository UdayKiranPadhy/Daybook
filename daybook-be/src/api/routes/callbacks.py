from typing import Annotated, Optional

import pygsheets
from fastapi import APIRouter, Query
from fastapi.responses import RedirectResponse

from src.api.dependencies import container
from src.client.google_oauth import GoogleOAuthClient
from src.models.oauth import AuthCode
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

router = APIRouter(prefix="/callback")


# def create_Account():
#     creds, google_oauth_response = google_oauth_client.exchange_auth_code_for_credentials(code)
#     print(google_oauth_client.get_profile_info_using_id_token(google_oauth_response.id_token).json())
#     gauth = GoogleAuth()
#     gauth.credentials = creds
#     drive = GoogleDrive(gauth)
#     folder_metadata = {
#         "title": "DayPlanner",
#         "mimeType": "application/vnd.google-apps.folder",
#     }
#     folder = drive.CreateFile(folder_metadata)
#     folder.Upload()
#
#     # Step 3: File properties
#     sheet_metadata = {
#         "title": "Tasks",
#         "mimeType": "application/vnd.google-apps.spreadsheet",
#         "parents": [{"id": folder["id"]}],
#     }
#     sheet_file = drive.CreateFile(sheet_metadata)
#     sheet_file.Upload()

@router.get("/google-oauth2")
async def get_profile_info_from_google_oauth(
        google_oauth_client: Annotated[
            GoogleOAuthClient, container.depends(GoogleOAuthClient)
        ],
        code: AuthCode = Query(AuthCode, alias="code"),
        state: Optional[str] = Query(None, alias="state"),
) -> RedirectResponse:
    SERVICE_ACCOUNT_FILE = '../dayplanner_service_account.json'
    gc = pygsheets.authorize(service_account_file='./dayplanner_service_account.json')
    sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1LRxLj-_2LA8Se3z7-5Gu8DNvpUpO6uIwU-BbhtomQoc')
    worksheet = sh.worksheet('title', "User")
    print(worksheet.get_all_records())

    creds, google_oauth_response = google_oauth_client.exchange_auth_code_for_credentials(code)
    profile = google_oauth_client.get_profile_info_using_id_token(google_oauth_response.id_token)

    response = RedirectResponse(url="http://localhost:3000/")
    response.set_cookie(key="session", value="good boy")
    return response
