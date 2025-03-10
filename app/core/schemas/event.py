from datetime import datetime

from app.core.schemas.base import BaseSchema
from typing import Optional


class UserRead(BaseSchema):
    id: int
    creator_id: int
    date: datetime
    location: str
    format: str


class UserCreate(BaseSchema):
    creator_id: int
    date: datetime
    location: str
    format: str

    model_config = {"str_strip_whitespace": True}


class UserUpdate(BaseSchema):
    creator_id: Optional[int] = None
    date: Optional[datetime] = None
    location: Optional[str] = None
    format: Optional[str] = None

    model_config = {"str_strip_whitespace": True}
