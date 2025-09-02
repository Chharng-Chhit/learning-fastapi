from sqlmodel import SQLModel

class HeroBase(SQLModel):
    name: str
    age: int
    secret_name: str
    email: str

class HeroCreate(HeroBase):
    pass

class HeroRead(HeroBase):
    id: int

    class Config:
        orm_mode = True
