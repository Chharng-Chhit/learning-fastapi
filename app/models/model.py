from typing import Optional, List
from sqlmodel import Field, SQLModel, Relationship

class Book(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(index=True)
    desc: Optional[str] = Field(default=None)
    hero_id: int = Field(foreign_key="hero.id")
    hero: Optional["Hero"] = Relationship(back_populates="books")

class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    age: int = Field(default=0, index=True)
    secret_name: str
    email: str = Field(index=True, unique=True)
    books: List[Book] = Relationship(back_populates="hero")
    cars: List["Cars"] = Relationship(back_populates="owner")

class Animal(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    category: str = Field(index=True)
    placeOfBirth: int = Field(default=0, index=True)
    # hero_id: int = Field(foreign_key="owner.id")
    # Hero: Optional["Hero"] = Relationship(back_populates="animals")
    
class Cars(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    name: str
    color: str
    owner_id: int = Field(foreign_key="hero.id")
    owner: Optional["Hero"] = Relationship(back_populates="cars")
    
    # class Animal(SQLModel, table=True):
    #     id: Optional[int] = Field(default=None, primary_key=True)
    #     name: str
    #     # category: str
    #     place_of_birth: str
    #     owner_id: Optional[int] = Field(default=None, foreign_key="user.id")
    #     owner: Optional["User"] = Relationship(back_populates="animals")