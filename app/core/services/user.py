from fastapi import HTTPException

from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import (
    SQLAlchemyError,
    IntegrityError,
)

from app.core.models.user import User
from app.core.schemas.user import (
    UserCreate,
    UserUpdate,
)

def create_user(session: Session, data: UserCreate, telegram_id: str) -> User:
    """
    Создает нового пользователя в базе данных.

    Аргументы:
    - session: сессия базы данных
    - data: объект UserCreate с данными пользователя
    - telegram_id: идентификатор пользователя в Telegram

    Возвращает:
    - Созданного пользователя
    """
    user_data: dict = data.model_dump()
    user = User(**user_data, telegram_id=telegram_id)

    session.add(user)
    try:
        session.commit()
        session.refresh(user)

    except IntegrityError as e:
        session.rollback()
        raise HTTPException(
            status_code=400,
            detail="Пользователь с введенными данными уже существует.",
        ) from e

    except SQLAlchemyError as e:
        session.rollback()
        raise HTTPException(
            status_code=500, detail=f"Не удалось создать пользователя: {e}"
        )

    return user


def get_user_by_id(session: Session, id: int) -> User | None:
    """
    Получает пользователя по его ID.

    Аргументы:
    - session: сессия базы данных
    - id: идентификатор пользователя

    Возвращает:
    - Объект пользователя или HTTP 404, если пользователь не найден
    """
    try:
        query = select(User).filter_by(id=id)
        user = session.execute(query).scalar_one_or_none()

        if not user:
            raise HTTPException(status_code=400, detail="Пользователь не найден.")

    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=500, detail=f"Ошибка при получении пользователя: {e}"
        )
    return user


def get_all_user(session: Session) -> list[User]:
    """
        Получает список всез пользователеей,

        Аргументы:
        - sesion: сессия базы данных

        Возвращает:
        - Список объектво User
        """
    try:
        query = select(User)
        users = session.execute(query).scalars().all()
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"Error fetching users: {e}")
    return users


def update_user_by_id(
        session: Session,
        data: UserUpdate,
        id: str,
) -> User:

    user = get_user_by_id(session, id)

    update_data = data.model_dump(exclude_unset=True, exclude_none=True)

    for key, value in update_data.items():
        setattr(user, key, value)

    try:
        session.commit()
        session.refresh(user)

    except SQLAlchemyError as e:
        session.rollback()
        raise HTTPException(
            status_code=500, detail=f"Не удалось обновить пользователя: {e}"
        )
    return user


def set_inactivate_by_id(session: Session, id: int) -> None:
    """
    Деактивирует пользователя по его ID.
    Аргументы:
    - session: сессия базы данных
    - id: идентификатор пользователя
    """
    user = get_user_by_id(session, id)

    try:
        user.is_active = False
        session.commit()

    except SQLAlchemyError as e:
        session.rollback()
        raise HTTPException(
            status_code=500,
            detail=f"Не удалось установить пользователя как неактивного{e}"
        )


def delete_user_by_id(session: Session, id: int) -> None:
    """
    Удаляет пользователя по его ID.

    Аргументы:
    - session: сессия базы данных
    - id: идентификатор пользователя
    """

    try:
        session.delete(user)
        session.commit()

    except SQLAlchemyError as e:
        session.rollback()
        raise HTTPException(
            status_code=500, detail=f"Не удалось удалить пользователя: {e}"
        )
