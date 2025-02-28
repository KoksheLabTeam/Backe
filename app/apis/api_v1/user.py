from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException

from app.core.services.user import UserService
from app.apis.depends.user import get_user_service
from app.core.schemas.user import UserCreate, UserRead, UserLogin

router = APIRouter(prefix="/user", tags=["User"])

@router.post("/create", response_model=UserRead)
def user_create(
    data: UserCreate,
    service: Annotated[UserService, Depends(get_user_service())],
):
    new_user = service.create(data)
    return new_user

@router.post("/login", response_model=UserRead)
def user_login(
    data: UserLogin,
    service: Annotated[UserService, Depends(get_user_service())],
):
    user = service.get(data.username)

    if not user.password == data.password:
        raise HTTPException(
            status_code=400, detail="Логин или пароль не верны!"
        )

    return user