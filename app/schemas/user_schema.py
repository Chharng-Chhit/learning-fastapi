from typing import List, Optional
from sqlmodel import SQLModel
from app.models.model import Animal


# ---------- Base ----------
class UserBase(SQLModel):
    name: str
    age: int
    secret_name: str
    email: str


# ---------- Create ----------
class UserCreate(UserBase):
    """Schema for creating a user (input)."""
    pass


# ---------- Read ----------
class UserRead(UserBase):
    """Schema for returning a user (output)."""
    id: int
    animals: List[Animal] = []

    class Config:
        from_attributes = True


# ---------- Update ----------
class UserUpdate(SQLModel):
    """Schema for updating a user (PATCH)."""
    name: Optional[str] = None
    age: Optional[int] = None
    secret_name: Optional[str] = None
    email: Optional[str] = None
