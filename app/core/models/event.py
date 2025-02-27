from typing import List
from app.core.models.base import Base

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime, date

class Event(Base):
    __tablename__ = "events"

    creator_id: Mapped[int]
    date: Mapped[datetime]
    location: Mapped[str]
    format: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    participants: Mapped[List["Participants"]] = relationship()