from typing import NewType

from pydantic import BaseModel, Field

AuthCode = NewType("AuthCode", str)
AccessToken = NewType("AccessToken", str)
TokenType = NewType("TokenType", str)
ExpiresIn = NewType("ExpiresIn", int)
RefreshToken = NewType("RefreshToken", str)
Scope = NewType("Scope", str)
IdToken = NewType("IdToken", str)


class GoogleOAuthTokenResponse(BaseModel):
    access_token: AccessToken = Field(..., alias="access_token")
    id_token: IdToken = Field(..., alias="id_token")
    expires_in: ExpiresIn = Field(..., alias="expires_in")
    token_type: TokenType = Field(..., alias="token_type")
    scope: Scope = Field(..., alias="scope")
    refresh_token: RefreshToken | None = Field(None, alias="refresh_token")
