from typing import Optional
from sqlmodel import SQLModel

from app.models.model import Hero

class CarBase(SQLModel):
    name: str
    color: str
    owner_id: int

class CarCreate(CarBase):
    pass

class CarRead(CarBase):
    id: int
    owner: Optional[Hero] = None

    class Config:
        from_attributes = True

class CarUpdate(CarCreate):
    pass

        
# class CarUpdate(CarBase):
#     name: Optional[str] = None
#     color: Optional[str] = None
#     owner_id: Optional[int] = None