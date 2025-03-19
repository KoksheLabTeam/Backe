from typing import Annotated, List
from fastapi import APIRouter, Depends, Header, status
from sqlalchemy.orm import Session

from app.core.database.helper import get_session
from app.core.services.event import create_event, get_all_event
from app.core.schemas.event import EventCreate, EventRead
from app.api.depends.user import get_current_user
from app.core.models.user import User

router = APIRouter(prefix="/event", tags=["Event"])

@router.post("/", response_model=EventRead, status_code=status.HTTP_201_CREATED)
def create_new_event(
    data: EventCreate,
    x_telegram_id: Annotated[str, Header()],
    user: Annotated[User, Depends(get_current_user)],
    session: Annotated[Session, Depends(get_session)]
):
    return create_event(session, data, user.id)


@router.get("/", response_model=List[EventRead])
def get_all_events(
    session: Annotated[Session, Depends(get_session)]
):
    return get_all_event(session)