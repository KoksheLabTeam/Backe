from app.core.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column

class Training(Base):
    __tablename__ = "training_plans"

    user_id: Mapped[int]
    plan_details: Mapped[str]
