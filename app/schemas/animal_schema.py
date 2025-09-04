from sqlmodel import SQLModel
from typing import Optional

class AnimalBase(SQLModel):
    name: str
    category: str
    placeOfBirth: Optional[int] = None
    #owner_id: int

class AnimalCreate(AnimalBase):
    #pass is used to indicate an empty block
    pass
class AnimalRead(AnimalBase):
    id: int

    class Config:
        orm_mode = True
        
class AnimalUpdate(SQLModel):
    name: Optional[str] = None
    category: Optional[str] = None
    placeOfBirth: Optional[int] = None
    #owner_id: Optional[int] = None
    
def AnimalDelete(SQLModel):
    id: int 