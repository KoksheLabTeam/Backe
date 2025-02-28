from fastapi import HTTPException

from app.core.models.user import User
from app.core.schemas.user import UserCreate
from app.core.repos.user import UserRepo, UserCreateException, UserNotFoundException

# API -> Service -> Repo

class UserService:
    def __init__(self, repository: UserRepo) -> None:
        self.repository = repository

    def create(self, data: UserCreate) -> User:

        instance = User(
            telegram_id=data.telegram_id,
            first_name=data.first_name,
            last_name=data.last_name,
            date_of_birth=data.date_of_birth,
            height=data.height,
            weight=data.weight,
            is_admin=data.is_admin,
        )

        try:
            user = self.repository.create(instance)
            return user

        except UserCreateException as e:
            raise HTTPException(
                status_code=500, detail=f"Error while creating user: {e}"
            )

    def get(self, username: str) -> User:
        try:
            user = self.repository.get(username)
            return user

        except UserCreateException as e:
            raise HTTPException(
                status_code=400, detail=f"User Not Found: {e}"
            )