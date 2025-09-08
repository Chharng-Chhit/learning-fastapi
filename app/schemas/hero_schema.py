from typing import List
from sqlmodel import SQLModel

from app.models.model import Cars

class HeroBase(SQLModel):
    name: str
    age: int
    secret_name: str
    email: str
    # animals: List[Animal] = []
   

class HeroCreate(HeroBase):
    pass

class HeroRead(HeroBase):
    id: int
    cars: List[Cars] = []
    class Config:
        from_attributes = True
