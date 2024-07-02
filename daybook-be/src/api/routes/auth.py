from logging import Logger
from typing import Annotated

from fastapi import APIRouter, Request
from fastapi.responses import Response as FastAPIResponse

from src.api.dependencies import container
from src.config import Config

router = APIRouter(prefix="/oauth")


@router.get("/google")
async def read_root(
    request: Request,
    logger: Annotated[Logger, container.depends(Logger)],
    config: Annotated[Config, container.depends(Config)],
) -> FastAPIResponse:
    domain = request.base_url
    return FastAPIResponse(
        status_code=302,
        headers={
            "Location": f"https://accounts.google.com/o/oauth2/v2/auth?client_id={config.google_oauth.client_id}&redirect_uri={domain}{config.google_oauth.redirect_uri}&response_type=code&scope=profile&state=1234567890"
        },
    )
