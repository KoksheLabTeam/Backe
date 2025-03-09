from typing import Annotated  # Используется для аннотирования зависимостей
from fastapi import (
    APIRouter,  # Класс для создания маршрутизатора
    Depends,  # Функция для внедрения зависимостей
    Header,  # Используется для получения заголовков HTTP-запросов
    status,  # Код статуса HTTP-ответов
)

from sqlalchemy.orm import Session  # Импорт объекта сессии SQLAlchemy
from app.core.database.helper import get_session  # Функция получения сессии БД

from app.core.models.user import User  # Импорт модели пользователя
from app.core.services import (
    user as user_service,  # Импорт сервиса управления пользователями
)
from app.core.schemas.user import (
    UserRead,  # Схема для чтения пользователя (ответ API)
    UserCreate,  # Схема для создания пользователя
    UserUpdate,  # Схема для обновления пользователя
)
from app.api.depends.user import (
    get_current_user,  # Зависимость для получения текущего пользователя
    get_admin_user,  # Зависимость для проверки роли администратора
)

# Создаем объект роутера с префиксом "/user" и тегом "User"
router = APIRouter(prefix="/user", tags=["User"])


@router.get("/", response_model=UserRead)
def get_me(user: Annotated[User, Depends(get_current_user)]):
    """
    Получение текущего пользователя.
    Доступен только для аутентифицированных пользователей.
    Возвращает объект пользователя.
    """
    return user


@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
def delete_me(
    user: Annotated[User, Depends(get_current_user)],  # Получение текущего пользователя
    session: Annotated[Session, Depends(get_session)],  # Получение сессии БД
):
    """
    Удаление текущего пользователя.
    Возвращает статус 204 (No Content), если успешно.
    """
    return user_service.delete_user_by_id(session, user.id)


@router.patch("/", response_model=UserRead)
def update_me(
    data: UserUpdate,  # Данные для обновления пользователя
    user: Annotated[User, Depends(get_current_user)],  # Получение текущего пользователя
    session: Annotated[Session, Depends(get_session)],  # Получение сессии БД
):
    """
    Обновление данных текущего пользователя.
    """
    return user_service.update_user_by_id(session, data, user.id)


# С этого места начинается CRUD для пользователя


@router.post("/", response_model=UserRead)
def create_user(
    x_telegram_id: Annotated[
        str, Header()
    ],  # Получение Telegram ID из заголовков запроса
    data: UserCreate,  # Данные для создания пользователя
    session: Annotated[Session, Depends(get_session)],  # Получение сессии БД
):
    """
    Создание нового пользователя.
    Требуется заголовок `x-telegram-id` (идентификатор Telegram).
    """
    return user_service.create_user(session, data, x_telegram_id)


@router.patch("/{id}", response_model=UserRead)
def update_user_by_id(
    id: int,  # ID пользователя для обновления
    admin_user: Annotated[
        User, Depends(get_admin_user)
    ],  # Проверка, что вызывающий пользователь - админ
    data: UserUpdate,  # Данные для обновления пользователя
    session: Annotated[Session, Depends(get_session)],  # Получение сессии БД
):
    """
    Обновление данных пользователя по ID. Доступно только администраторам.
    """
    return user_service.update_user_by_id(session, data, id)


@router.get("/{id}", response_model=UserRead)
def get_user_by_id(
    id: int,  # ID пользователя
    admin_user: Annotated[
        User, Depends(get_admin_user)
    ],  # Проверка прав администратора
    session: Annotated[Session, Depends(get_session)],  # Получение сессии БД
):
    """
    Получение пользователя по ID. Доступно только администраторам.
    """
    return user_service.get_user_by_id(session, id)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user_by_id(
    id: int,  # ID пользователя
    admin_user: Annotated[
        User, Depends(get_admin_user)
    ],  # Проверка прав администратора
    session: Annotated[Session, Depends(get_session)],  # Получение сессии БД
):
    """
    Удаление пользователя по ID. Доступно только администраторам.
    """
    return user_service.delete_user_by_id(session, id)