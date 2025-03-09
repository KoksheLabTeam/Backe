from typing import Annotated  # Импорт Annotated для аннотации зависимостей
from sqlalchemy.orm import Session  # Импорт сессии SQLAlchemy для работы с БД
from fastapi.exceptions import HTTPException  # Исключение для HTTP-ошибок
from fastapi import Depends, Header, status  # Импорт FastAPI-зависимостей

from app.core.models.user import User  # Импорт модели пользователя
from app.core.database.helper import get_session  # Функция получения сессии БД


def get_current_user(
    x_telegram_id: Annotated[
        str, Header()
    ],  # Получаем заголовок x-telegram-id из запроса
    session: Annotated[
        Session, Depends(get_session)
    ],  # Получаем сессию БД через Depends
) -> User:

    # Проверяем, что заголовок x-telegram-id присутствует
    if not x_telegram_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,  # Ошибка 400, если заголовок отсутствует
            detail="x-telegram-id is missing",
        )

    # Ищем пользователя по telegram_id и проверяем, что он активен
    user = (
        session.query(User)
        .filter(User.telegram_id == x_telegram_id, User.is_active == True)
        .first()
    )

    # Если пользователь не найден или неактивен, возвращаем ошибку 404
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found or inactive.",
        )

    return user  # Возвращаем найденного пользователя


def get_admin_user(current_user: Annotated[User, Depends(get_current_user)]) -> User:
    # Проверяем, является ли пользователь суперпользователем
    if not current_user.is_superuser:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,  # Ошибка 403, если нет прав администратора
            detail="Permission denied.",
        )

    return current_user  # Возвращаем текущего пользователя, если он администратор