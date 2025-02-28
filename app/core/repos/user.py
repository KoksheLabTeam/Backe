from Docker_1.app.main import query
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.core.models.user import User

class UserCreateException(Exception):
    """raise exception when is an error during user creation"""

class UserNotFoundException(Exception):
    """raise exception when is no user found"""

class UserRepo:
    def __init__(self, session: Session) -> None:
        self.session = session

    def create(self, instance: User) -> User:
        self.session.add(instance)
        try:
            self.session.commit()
            self.session.refresh(instance)
            return instance

        except Exception as e:
            self.session.rollback()
            raise UserCreateException(str(e))

    def get(self, username: str) -> User:

        query = select(User).where(User.username == username)

        try:
            user = self.session.execute(query)
            return user.scalar_one_or_none()

        except Exception as e:
            self.session.rollback()
            raise UserNotFoundException(str(e))