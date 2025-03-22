from typing import Annotated
from fastapi import APIRouter, Depends, Header, status
from sqlalchemy.orm import Session
from app.core.database.helper import get_session
from app.core.models.user import User
from app.core.services import user as user_service
from app.core.schemas.user import UserRead, UserCreate, UserUpdate
from app.apis.depends.user import get_current_user, get_admin_user

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


@router.patch("/{id}", response_model=UserRead)
def update_user_by_id(
    id: int,
    admin_user: Annotated[User, Depends(get_admin_user)],
    data: UserUpdate,
    session: Annotated[Session, Depends(get_session)],
):
    return user_service.update_user_by_id(session, data, id)


@router.get("/{id}", response_model=UserRead)
def get_user_by_id(
    id: int,
    admin_user: Annotated[User, Depends(get_admin_user)],
    session: Annotated[Session, Depends(get_session)],
):
    return user_service.get_user_by_id(session, id)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user_by_id(
    id: int,
    admin_user: Annotated[User, Depends(get_admin_user)],
    session: Annotated[Session, Depends(get_session)],
):
    return user_service.delete_user_by_id(session, id)
