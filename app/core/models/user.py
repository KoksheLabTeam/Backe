from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column

from app.core.models.base import Base


class User(Base):
    __tablename__ = "users"

    telegram_id: Mapped[str] = mapped_column(unique=True)
    first_name: Mapped[str]
    last_name: Mapped[str]

    height: Mapped[str]
    weight: Mapped[str]
    dob: Mapped[datetime]

    # events: Mapped[List["Event"]] = relationship(secondary=user_to_event)
