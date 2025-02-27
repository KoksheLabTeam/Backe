from app.core.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

class Participants(Base):
    __tablename__ = "event_participants"

    event_id: Mapped[int]
    user_id: Mapped[int]
    user_id: Mapped[int] = mapped_column(ForeignKey("events.id"))