from app.core.models.user import User
from app.core.schemas.user import UserCreate
from app.core.repos.user import UserRepo

# API -> Service -> Repo

class UserService:
    def __init__(self, repository: UserRepo) -> None:
        self.repository = repository

    def create(self, data: UserCreate) -> User:

        user = User(
            username=data.username,
            password=data.password,
        )