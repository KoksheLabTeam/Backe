from typing import List
from app.core.models.base import Base

from sqlalchemy import ForeignKey, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

user_to_event = Table(
    "user_to_event",
    Base.metadata,
    Column("event_id", ForeignKey("events.id")),
    Column("user_id", ForeignKey("users.id")),
)

class Event(Base):
    __tablename__ = "events"

    creator_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    date: Mapped[datetime] = mapped_column()
    location: Mapped[str] = mapped_column()
    format: Mapped[str] = mapped_column()

    participants: Mapped[list["User"]] = relationship(secondary=user_to_event)