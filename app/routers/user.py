from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from app.core.db import get_session
from app.schemas.user_schema import UserCreate, UserRead, UserUpdate
from app.utilities.user_utility import UserUtility

router = APIRouter(prefix="/users", tags=["users"])


@router.post(
    "/",
    # response_model=UserRead,
    status_code=status.HTTP_201_CREATED,
)
def create_user(
    user: UserCreate,
    session: Session = Depends(get_session),
):
    db_user = UserUtility.create_user(session, user)
    return db_user


@router.get(
    "/",
    response_model=List[UserRead],
)
def read_users(
    session: Session = Depends(get_session),
):
    users = UserUtility.get_all_users_with_animals(session)
    return users


@router.get(
    "/{user_id}",
    response_model=UserRead,
)
def read_user(
    user_id: int,
    session: Session = Depends(get_session),
):
    user = UserUtility.get_user_with_animals(session, user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user


@router.patch(
    "/{user_id}",
    response_model=UserRead,
)
def update_user(
    user_id: int,
    user: UserUpdate,  # partial updates
    session: Session = Depends(get_session),
):
    updated_user = UserUtility.update_user(session, user_id, user)
    if not updated_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return updated_user


@router.delete(
    "/{user_id}",
    response_model=UserRead,
)
def delete_user(
    user_id: int,
    session: Session = Depends(get_session),
):
    deleted_user = UserUtility.delete_user(session, user_id)
    if not deleted_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return deleted_user
