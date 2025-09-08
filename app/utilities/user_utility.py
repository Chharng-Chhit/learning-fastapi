from typing import List, Optional
from sqlmodel import Session, select
from sqlalchemy.orm import selectinload
from app.models.model import User
from app.schemas.user_schema import UserCreate, UserUpdate  # ensure PascalCase


def _to_dict(model) -> dict:
    """Pydantic v2/v1 compatibility."""
    if hasattr(model, "model_dump"):
        return model.model_dump()
    return model.dict()


def _to_partial_dict(model) -> dict:
    """Only fields the caller actually sent (for PATCH/partial updates)."""
    if hasattr(model, "model_dump"):
        return model.model_dump(exclude_unset=True)
    return model.dict(exclude_unset=True)


class UserUtility:
    @staticmethod
    def create_user(db: Session, user_data: UserCreate) -> User:
        payload = _to_dict(user_data)
        db_user = User(**payload)
        try:
            db.add(db_user)
            db.commit()
            db.refresh(db_user)
            return db_user
        except Exception:
            db.rollback()
            raise

    @staticmethod
    def get_user_with_animals(db: Session, user_id: int) -> Optional[User]:
        stmt = (
            select(User)
            .where(User.id == user_id)
            .options(selectinload(User.animals))
        )
        return db.exec(stmt).first()

    @staticmethod
    def get_all_users_with_animals(db: Session) -> List[User]:
        stmt = select(User)
        return db.exec(stmt).all()

    @staticmethod
    def update_user(db: Session, user_id: int, user_data: UserUpdate) -> Optional[User]:
        # load the user
        stmt = select(User).where(User.id == user_id)
        db_user = db.exec(stmt).first()
        if not db_user:
            return None

        updates = _to_partial_dict(user_data)
        if not updates:
            return db_user  # nothing to update

        for key, value in updates.items():
            setattr(db_user, key, value)

        try:
            db.add(db_user)
            db.commit()
            db.refresh(db_user)
            return db_user
        except Exception:
            db.rollback()
            raise

    @staticmethod
    def delete_user(db: Session, user_id: int) -> Optional[User]:
        stmt = select(User).where(User.id == user_id)
        db_user = db.exec(stmt).first()
        if not db_user:
            return None

        try:
            db.delete(db_user)
            db.commit()
            return db_user
        except Exception:
            db.rollback()
            raise
