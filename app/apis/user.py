from typing import Annotated

from fastapi import APIRouter, Depends, Header, status
from sqlalchemy.orm import Session

from app.apis.depends.user import get_current_user
from app.core.database.helper import get_session
from app.core.models.user import User
from app.core.schemas.user import UserCreate, UserRead, UserUpdate
from app.core.services import user as user_service

router = APIRouter(prefix="/user", tags=["User"])


@router.get("/", response_model=UserRead)
def get_me(user: Annotated[User, Depends(get_current_user)]):
    return user


@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
def delete_me(
    user: Annotated[User, Depends(get_current_user)],
    session: Annotated[Session, Depends(get_session)],
):
    return user_service.delete_user_by_id(session, user.id)


@router.patch("/", response_model=UserRead)
def update_me(
    data: UserUpdate,
    user: Annotated[User, Depends(get_current_user)],
    session: Annotated[Session, Depends(get_session)],
):
    return user_service.update_user_by_id(session, data, user.id)


@router.post("/", response_model=UserRead)
def create_user(
    x_telegram_id: Annotated[str, Header()],
    data: UserCreate,
    session: Annotated[Session, Depends(get_session)],
):
    return user_service.create_user(session, data, x_telegram_id)
