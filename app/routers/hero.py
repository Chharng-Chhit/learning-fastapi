from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.schemas.hero_schema import HeroCreate, HeroRead
from app.core.db import get_session
from app.utilities.hero_utility import HeroUtility

router = APIRouter(prefix="/heroes", tags=["heroes"])

@router.post("/", response_model=HeroRead)
def create_hero(hero: HeroCreate, session: Session = Depends(get_session)):
    db_hero = HeroUtility.create_hero(session, hero)
    return db_hero

@router.get("/", response_model=list[HeroRead])
def read_heroes(session: Session = Depends(get_session)):
    print('hello')
    heroes = HeroUtility.get_heroes(session)
    return heroes

@router.get("/{hero_id}", response_model=HeroRead)
def read_hero(hero_id: int, session: Session = Depends(get_session)):
    hero = HeroUtility.get_hero(session, hero_id)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    return hero