from app.core.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column

class Nutrition(Base):
    __tablename__ = "nutrition_plans"

    user_id: Mapped[int]
    plan_details: Mapped[str]