from sqlmodel import SQLModel
from typing import Optional
from pydantic import BaseModel
from app.models.model import User

class AnimalBase(SQLModel):
    name: str
    # category: str
    place_of_birth: Optional[str] = None
    owner_id: int

class AnimalCreate(AnimalBase):
    #pass is used to indicate an empty block
    pass
class AnimalRead(AnimalBase):
    id: int
    owner: Optional[User] = None

    class Config:
        from_attributes = True
        
class AnimalUpdate(SQLModel):
    name: Optional[str] = None
    category: Optional[str] = None
    placeOfBirth: Optional[str] = None
    owner_id: Optional[int] = None
    
def AnimalDelete(SQLModel):
    id: int

class UserOut(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True

class AnimalOut(BaseModel):
    id: int
    name: str
    category: str
    placeOfBirth: str
    owner: UserOut | None

    class Config:
        from_attributes = True