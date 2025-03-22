from datetime import datetime
from typing import TYPE_CHECKING, List

from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.models.base import Base

if TYPE_CHECKING:
    from app.core.models.user import User

user_to_event = Table(
    "user_to_event",
    Base.metadata,
    Column("event_id", ForeignKey("events.id")),
    Column("user_id", ForeignKey("users.id")),
)


class Event(Base):
    __tablename__ = "events"

    creator_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    date: Mapped[datetime]
    location: Mapped[str]
    format: Mapped[str]

    participants: Mapped[List["User"]] = relationship(secondary=user_to_event)
