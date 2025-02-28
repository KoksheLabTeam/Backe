from sqlalchemy.orm import Session
from app.core.models.user import User

class UserCreateException(Exception):
    """ raise exception when is an error during user creation """

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
            raise UserCreateException(e)
