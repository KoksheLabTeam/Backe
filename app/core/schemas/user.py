from datetime import datetime
from typing import Optional

from app.core.schemas.base import BaseSchema


class UserRead(BaseSchema):
    id: int
    telegram_id: str
    first_name: str
    last_name: str

    height: str
    weight: str
    dob: datetime


class UserCreate(BaseSchema):
    first_name: str
    last_name: str

    height: str
    weight: str
    dob: datetime


class UserUpdate(BaseSchema):
    telegram_id: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None

    dob: Optional[datetime] = None
    height: Optional[str] = None
    weight: Optional[str] = None
