from pydantic import BaseModel, Field

from src.models.oauth import SubcriberId, Name, Email, Picture, RefreshToken


class User(BaseModel):
    user_id: SubcriberId = Field(..., alias="id")
    name: Name = Field(..., alias="name")
    email: Email = Field(..., alias="email")
    picture: Picture = Field(..., alias="picture")
    refresh_token: RefreshToken = Field(..., alias="refresh_token")
    tasks_sheet_url: str = Field(..., alias="tasks_sheet_url")
