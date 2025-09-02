from sqlmodel import SQLModel
from typing import Optional

class BookBase(SQLModel):
    title: str
    desc: Optional[str] = None

class BookCreate(BookBase):
    hero_id: int

class BookRead(BookBase):
    id: int
    hero_id: int

    class Config: 
        orm_mode = True