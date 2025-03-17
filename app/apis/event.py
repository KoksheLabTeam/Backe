from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database.helper import get_session
from app.core.services.event import create_event, get_event_by_id
from app.core.schemas.event import EventCreate, EventRead
from app.api.depends.user import get_current_user
from app.core.models.user import User

router = APIRouter(prefix="/event", tags=["Event"])

@router.post("/", response_model=EventRead)
def create_new_event(
    data: EventCreate,
    user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    return create_event(session, data, user.id)