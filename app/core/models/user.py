from typing import List, TYPE_CHECKING
from app.core.models.base import Base
from app.core.models.event import Event, user_to_event
from app.core.models.nutrition_plan import Nutrition
from app.core.models.participants import Participants
from app.core.models.training_plan import Training

from sqlalchemy import Date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime, date

class User(Base):
    __tablename__ = "users"

    telegram_id: Mapped[str] = mapped_column(unique=True)
    first_name: Mapped[str]
    last_name: Mapped[str]

    date_of_birth: Mapped[date] = mapped_column(Date)
    height: Mapped[float]
    weight: Mapped[float]
    is_admin: Mapped[bool] = mapped_column(default=False)

    events: Mapped[List["Event"]] = relationship(secondary=user_to_event)