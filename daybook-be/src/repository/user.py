from pygsheets.worksheet import Worksheet

from src.models.oauth import SubcriberId
from src.models.user import User
from src.repository.base import Repository


class UserRepository(Repository):

    def __init__(self, client: Worksheet):
        self.client = client

    def get_user(self, user_id: SubcriberId) -> User:
        self.client.find(user_id,matchEntireCell=True,matchCase=True,cols=(1,1))
