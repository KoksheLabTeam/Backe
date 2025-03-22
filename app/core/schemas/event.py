from datetime import datetime
from typing import Optional

from app.core.schemas.base import BaseSchema


class EventRead(BaseSchema):
    id: int
    creator_id: int
    title: str
    description: Optional[str] = None
    date: datetime
    location: str
    format: str


class EventCreate(BaseSchema):
    title: str
    description: Optional[str] = None
    date: datetime
    location: str
    format: str


class EventUpdate(BaseSchema):
    title: Optional[str] = None
    description: Optional[str] = None
    date: Optional[datetime] = None
    location: Optional[str] = None
    format: Optional[str] = None
