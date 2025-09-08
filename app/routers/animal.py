from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.schemas.animal_schema import AnimalCreate, AnimalRead
from app.core.db import get_session
from app.utilities.animal_utility import AnimalUtility

router = APIRouter(prefix="/animals", tags=["animals"])
@router.post("/")
def create_animal_endpoint(animal: AnimalCreate, session: Session = Depends(get_session)):
    db_animal = AnimalUtility.add_animal(session, animal)
    return db_animal

@router.get("/"
            , response_model=List[AnimalRead]
            )
def read_animals(session: Session = Depends(get_session)):
    animals = AnimalUtility.get_all_animals(session)
    return animals

@router.get("/{animal_id}", response_model=AnimalRead)
def read_animal(animal_id: int, session: Session = Depends(get_session)):
    animal = AnimalUtility.get_animal(session, animal_id)
    if not animal:
        raise HTTPException(status_code=404, detail="Animal not found")
    return animal