from app.core.models.base import Base

from sqlalchemy import Date
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime, date

class Event(Base):
    __tablename__ = "events"

    creator_id: Mapped[int]
    date: Mapped[datetime]
    location: Mapped[str]
    format: Mapped[str]