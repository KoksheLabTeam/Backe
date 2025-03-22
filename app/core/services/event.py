from typing import List

from fastapi import HTTPException
from sqlalchemy import not_, select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from app.core.models.event import Event
from app.core.models.user import User
from app.core.schemas.event import EventCreate, EventUpdate


def create_event(
    session: Session,
    data: EventCreate,
    user: User,
) -> Event:
    event_data: dict = data.model_dump()
    event = Event(**event_data, creator_id=user.id)

    session.add(event)
    try:
        session.commit()
        session.refresh(event)
        event.participants.append(user)
        session.commit()

    except SQLAlchemyError as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=f"Не удалось создать событие: {e}")

    return event


def get_all_users_events(
    session: Session,
    creator_id: int,
) -> List[Event]:
    try:
        query = select(Event).filter_by(creator_id=creator_id)
        event = session.execute(query).scalars().all()

    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"Ошибка при получении забега: {e}")

    return event


def get_event_by_id(session: Session, event_id: int) -> Event | None:
    try:
        query = select(Event).filter_by(id=event_id)
        event = session.execute(query).scalar_one_or_none()

        if not event:
            raise HTTPException(status_code=400, detail="Забег не найден.")

    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"Ошибка при получении забега: {e}")

    return event


def get_all_event(session: Session, user: User) -> list[Event]:
    try:
        query = select(Event).where(not_(Event.participants.contains(user)))
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
    creator_id: int,
) -> Event:

    event = get_event_by_id(session, event_id)

    if not event.creator_id == creator_id:
        raise HTTPException(
            status_code=403, detail="Недостаточно прав для изменения забега."
        )

    update_data: dict = data.model_dump(exclude_unset=True, exclude_none=True)

    for key, value in update_data.items():
        setattr(event, key, value)

    try:
        session.commit()
        session.refresh(event)

    except SQLAlchemyError as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=f"Не удалось обновить забег: {e}")

    return event


def delete_event_by_id(session: Session, event_id: int, creator_id: int) -> None:
    event = get_event_by_id(session, event_id)

    if not event.creator_id == creator_id:
        raise HTTPException(
            status_code=403, detail="Недостаточно прав для удаления события."
        )

    try:
        session.delete(event)
        session.commit()
    except SQLAlchemyError as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=f"Не удалось удалить событие: {e}")


def add_user_to_event(session: Session, event_id: int, user: User) -> None:
    event = get_event_by_id(session, event_id)

    try:
        event.participants.append(user)
        session.commit()

    except SQLAlchemyError as e:
        session.rollback()
        raise HTTPException(
            status_code=500, detail=f"Не удалось добавить пользователя к забегу: {e}"
        )


def remove_user_from_event(session: Session, event_id: int, user: User) -> None:
    event = get_event_by_id(session, event_id)

    try:
        event.participants.remove(user)
        session.commit()

    except SQLAlchemyError as e:
        session.rollback()
        raise HTTPException(
            status_code=500, detail=f"Не удалось удалить пользователя из забега: {e}"
        )


def event_all_participants(session: Session, event_id: int) -> List[User]:
    event = get_event_by_id(session, event_id)

    return event.participants if event.participants else []
