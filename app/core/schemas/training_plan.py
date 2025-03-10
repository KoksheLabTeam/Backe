from datetime import datetime

from app.core.schemas.base import BaseSchema
from typing import Optional


class UserRead(BaseSchema):
    id: int
    user_id: int
    plan_details: str


class UserCreate(BaseSchema):
    user_id: int
    plan_details: str

    model_config = {"str_strip_whitespace": True}


class UserUpdate(BaseSchema):
    user_id: Optional[int] = None
    plan_details: Optional[str] = None

    model_config = {"str_strip_whitespace": True}