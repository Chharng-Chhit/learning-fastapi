from typing import List, Optional
from sqlmodel import Session, select
from sqlalchemy.orm import Session, selectinload

from app.models.model import Animal
from app.schemas.animal_schema import AnimalCreate
from app.schemas.animal_schema import AnimalUpdate


class AnimalUtility:
    @staticmethod
    def add_animal(db: Session, animal: AnimalCreate) -> Animal:
        db_animal = Animal(**animal.dict())
        db.add(db_animal)
        db.commit()
        db.refresh(db_animal)
        return db_animal
    @staticmethod
    def get_all_animals(db: Session) -> List[Animal]:
        stmt = select(Animal)
        return db.exec(stmt).all()

