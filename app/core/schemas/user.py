from app.core.schemas.base import BaseSchema
from typing import Optional
from datetime import datetime

class UserRead(BaseSchema):
    id: int
    telegram_id: str
    first_name: str
    last_name: str

    date_of_birth: datetime
    height: float
    weight: float

    is_admin: bool


class UserCreate(BaseSchema):
    first_name: str
    last_name: str

    model_config = {"str_strip_whitespace": True}


class UserUpdate(BaseSchema):
    telegram_id: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None

    date_of_birth: Optional[datetime] = None
    height: Optional[float] = None
    weight: Optional[float] = None

    is_admin: Optional[bool] = None

    model_config = {"str_strip_whitespace": True}