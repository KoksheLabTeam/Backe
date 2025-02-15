from app.core.models.base import Base

from sqlalchemy import Date
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime, date

class User(Base):
    __tablename__ = "users"

    telegram_id: Mapped[str] = mapped_column(unique=True)
    first_name: Mapped[str]
    last_name: Mapped[str]

    data_of_birth: Mapped[date] = mapped_column(Date)
    height: Mapped[float]
    weight: Mapped[float]