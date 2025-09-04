from sqlmodel import SQLModel
from typing import Optional
from app.models.model import Hero

class BookBase(SQLModel):
    title: str
    desc: Optional[str] = None
    hero_id: int
    hero: Optional[Hero] = None

class BookCreate(BookBase):
    hero_id: int

class BookRead(BookBase):
    id: int
    hero_id: int

    class Config: 
        orm_mode = True