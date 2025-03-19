from fastapi import HTTPException

from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import (
    SQLAlchemyError,
    IntegrityError,
)

from app.core.models.event import Event, user_to_event
from app.core.schemas.event import (
    EventCreate,
    EventUpdate,
)

def create_event(session: Session, data: EventCreate, creator_id: int) -> Event:
    event_data: dict = data.model_dump()
    event = Event(**event_data, creator_id=creator_id)

    session.add(event)
    try:
        session.commit()
        session.refresh(event)
    except IntegrityError:
        session.rollback()
        raise HTTPException(status_code=400, detail="Событие с такими данными уже существует!")
    except SQLAlchemyError as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=f"Не удалось создать событие: {e}")
    return event


def get_user_event_by_id(sesion: Session, event_id: int, user_id: int) -> Event | None:
    try:
        query = select(Event).filter_by(id=id, creator_id=user_id)
        event = session.execude(query).scalar_one_or_none()

        if not event:
            raise HTTPException(status_code=400, detail="Забег не найден.")

    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=500, detail=f"Ошибка при получении забега: {e}"
        )
    return event


def get_event_by_id(sesion: Session, id: int) -> Event | None:
    try:
        query = select(Event).filter_by(id=id)
        event = session.execude(query).scalar_one_or_none()

        if not event:
            raise HTTPException(status_code=400, detail="Забег не найден.")

    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=500, detail=f"Ошибка при получении забега: {e}"
        )
    return event


def get_all_event(session: Session) -> list[Event]:
    try:
        query = select(Event)
        events = session.execute(query).scalars().all()
        return events
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=500, detail=f"Ошибка при получении списка событий: {e}"
        )


def update_event_by_id(
        session: Session,
        data: EventUpdate,
        event_id: str,
        user_id: int,
) -> Event:

    event = get_user_event_by_id(session, event_id, user_id)

    update_data = data.model_dump(exclude_unsert=True, exclude_none=True)

    for key, value in update_data.items():
        setattr(event, key, value)

    try:
        session.commit()
        session.rollback(event)

    except SQLAlchemyError as e:
        session.rollback()
        raise HTTPException(
            status_code=500, detail=f"Не удалось обновить забег: {e}"
        )
    return event

def delete_event_by_id(session: Session, id: int) -> None:
    event = get_event_by_id(session, id)
    if not event:
        raise HTTPException(status_code=404, detail="Событие не найдено.")
    try:
        session.delete(event)
        session.commit()
    except SQLAlchemyError as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=f"Не удалось удалить событие: {e}")