from typing import NewType, Optional

from pydantic import BaseModel, Field

AuthCode = NewType("AuthCode", str)
AccessToken = NewType("AccessToken", str)
TokenType = NewType("TokenType", str)
ExpiresIn = NewType("ExpiresIn", int)
RefreshToken = NewType("RefreshToken", str)
Scope = NewType("Scope", str)
IdToken = NewType("IdToken", str)
SubcriberId = NewType("SubcriberId", str)
Name = NewType("Name", str)
Picture = NewType("Picture", str)
FirstName = NewType("FirstName", str)
LastName = NewType("LastName", str)
Email = NewType("Email", str)


class GoogleOAuthTokenResponse(BaseModel):
    access_token: AccessToken = Field(..., alias="access_token")
    id_token: IdToken = Field(..., alias="id_token")
    expires_in: ExpiresIn = Field(..., alias="expires_in")
    token_type: TokenType = Field(..., alias="token_type")
    scope: Scope = Field(..., alias="scope")
    refresh_token: RefreshToken | None = Field(None, alias="refresh_token")


class GoogleProfile(BaseModel):
    id: SubcriberId = Field(..., alias="sub")
    name: Name = Field(..., alias="name")
    email: Email = Field(..., alias="email")
    picture: Picture = Field(..., alias="picture")
    given_name: FirstName = Field(..., alias="given_name")
    family_name: LastName = Field(..., alias="family_name")

    class Config:
        populate_by_name = True