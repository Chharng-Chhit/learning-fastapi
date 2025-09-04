from sqlmodel import SQLModel
from app.models.model import Book
from app.schemas.book_schema import BookBase

class HeroBase(SQLModel):
    name: str
    age: int
    secret_name: str
    email: str
    # books: list[BookBase]

# id: Optional[int] = Field(default=None, primary_key=True)
# name: str = Field(index=True)
# age: int = Field(default=0, index=True)
# secret_name: str

class HeroCreate(HeroBase):
    pass

class HeroRead(HeroBase):
    id: int

    class Config:
        orm_mode = True
