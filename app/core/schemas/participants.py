from datetime import datetime

from app.core.schemas.base import BaseSchema
from typing import Optional


class UserRead(BaseSchema):
    id: int
    event_id: int
    user_id: str


class UserCreate(BaseSchema):
    event_id: int
    user_id: str

    model_config = {"str_strip_whitespace": True}


class UserUpdate(BaseSchema):
    event_id: Optional[int] = None
    user_id: Optional[str] = None

    model_config = {"str_strip_whitespace": True}
