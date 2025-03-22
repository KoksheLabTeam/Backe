from fastapi import APIRouter

from .event import router as event_router
from .user import router as user_router

routers = APIRouter(prefix="/api")

routers.include_router(user_router)
routers.include_router(event_router)
