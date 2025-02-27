from sqlalchemy.orm import DeclarativeBase, Mapped


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)