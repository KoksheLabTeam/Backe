from typing import Annotated, List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.apis.depends.user import get_current_user
from app.core.database.helper import get_session
from app.core.models.user import User
from app.core.schemas.event import EventCreate, EventRead, EventUpdate
from app.core.schemas.user import UserRead
from app.core.services import event as event_service

router = APIRouter(prefix="/event", tags=["Event"])


@router.post(
    "/",
    response_model=EventRead,
    status_code=status.HTTP_201_CREATED,
)
def create_new_event(
    data: EventCreate,
    user: Annotated[User, Depends(get_current_user)],
    session: Annotated[Session, Depends(get_session)],
):
    return event_service.create_event(session, data, user.id)


@router.get("/", response_model=List[EventRead])
def get_all_events(
    user: Annotated[User, Depends(get_current_user)],
    session: Annotated[Session, Depends(get_session)],
):
    return event_service.get_all_event(session)


@router.get("/user", response_model=List[EventRead])
def get_users_events(
    user: Annotated[User, Depends(get_current_user)],
    session: Annotated[Session, Depends(get_session)],
):
    return event_service.get_all_users_events(session, user.id)


@router.get("/{event_id}", response_model=EventRead)
def get_event_by_id(
    event_id: int,
    user: Annotated[User, Depends(get_current_user)],
    session: Annotated[Session, Depends(get_session)],
):
    return event_service.get_event_by_id(session, event_id)


@router.patch("/{event_id}", response_model=EventRead)
def update_event_by_id(
    event_id: int,
    data: EventUpdate,
    user: Annotated[User, Depends(get_current_user)],
    session: Annotated[Session, Depends(get_session)],
):
    return event_service.update_event_by_id(
        session=session,
        data=data,
        event_id=event_id,
        creator_id=user.id,
    )


@router.delete("/{event_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_event_by_id(
    event_id: int,
    user: Annotated[User, Depends(get_current_user)],
    session: Annotated[Session, Depends(get_session)],
):
    event_service.delete_event_by_id(session, event_id, user.id)


@router.patch("/{event_id}/add-user", status_code=status.HTTP_204_NO_CONTENT)
def add_user_to_event(
    event_id: int,
    user: Annotated[User, Depends(get_current_user)],
    session: Annotated[Session, Depends(get_session)],
):
    event_service.add_user_to_event(session, event_id, user)


@router.patch("/{event_id}/rm-user", status_code=status.HTTP_204_NO_CONTENT)
def remove_user_from_event(
    event_id: int,
    user: Annotated[User, Depends(get_current_user)],
    session: Annotated[Session, Depends(get_session)],
):
    event_service.remove_user_from_event(session, event_id, user)


@router.get("/{event_id}/participants", response_model=List[UserRead])
def get_event_participants(
    event_id: int,
    user: Annotated[User, Depends(get_current_user)],
    session: Annotated[Session, Depends(get_session)],
):
    return event_service.event_all_participants(session, event_id)
