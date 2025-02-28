from app.core.models.user import User
from app.core.schemas.user import UserCreate
from app.core.repos.user import UserRepo

# API -> Service -> Repo

class UserService:
    def __init__(self, repository: UserRepo) -> None:
        self.repository = repository

    def create(self, data: UserCreate) -> User:

        user = User(
            telegram_id=data.telegram_id,
            first_name=data.first_name,
            last_name=data.last_name,
            date_of_birth=data.date_of_birth,
            height=data.height,
            weight=data.weight,
            is_admin=data.is_admin,
        )