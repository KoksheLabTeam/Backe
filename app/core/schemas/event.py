from datetime import datetime
from typing import Optional

from app.core.schemas.base import BaseSchema


class EventRead(BaseSchema):
    id: int
    creator_id: int
    date: datetime
    location: str
    format: str


class EventCreate(BaseSchema):
    date: datetime
    location: str
    format: str


class EventUpdate(BaseSchema):
    date: Optional[datetime] = None
    location: Optional[str] = None
    format: Optional[str] = None
