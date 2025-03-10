"""
 Зачем этот routers.py нужен?
- Собирает все роутеры (маршруты API) в один главный роутер `routers`.
- Позволяет импортировать `routers` в `main.py`, вместо импорта каждого роутера отдельно.
- Добавляет префикс `/api`, чтобы все API-маршруты имели общий префикс (например, `/api/user`).
"""

# Импортируем APIRouter, который используется для объединения маршрутов
from fastapi import APIRouter

# Импортируем роутер пользователей из модуля user.py, переименовывая его для удобства как user_router
from .user import router as user_router
from .todo import router as todo_router

# Создаем главный роутер, который объединит все API-маршруты приложения
# Добавляем префикс `/api`, чтобы все эндпойнты начинались с `/api`
routers = APIRouter(prefix="/api")

# Подключаем роутер пользователей к главному роутеру
# Теперь все маршруты из `user.py` станут доступными под `/api/user`
routers.include_router(user_router)
routers.include_router(todo_router)