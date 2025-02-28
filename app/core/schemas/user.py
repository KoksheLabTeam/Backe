from app.core.schemas.base import BaseSchema
from typing import Optional

class UserLogin(BaseSchema):
    username: str
    password: str

class UserRead(BaseSchema):
    id: int
    telegram_id: str
    first_name: str
    last_name: str

    date_of_birth: date
    height: float
    weight: float

    is_admin: bool


class UserCreate(BaseSchema):
    telegram_id: str
    first_name: str
    last_name: str

    date_of_birth: date
    height: float
    weight: float

    is_admin: Optional[bool] = False


class UserUpdate(BaseSchema):
    telegram_id: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None

    date_of_birth: Optional[date] = None
    height: Optional[float] = None
    weight: Optional[float] = None

    is_admin: Optional[bool] = None
