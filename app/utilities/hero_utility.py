from sqlalchemy.orm import Session
from app.models.model import Hero
from app.schemas.hero_schema import HeroCreate

class HeroUtility:
    @staticmethod
    def create_hero(db: Session, hero: HeroCreate) -> Hero:
        db_hero = Hero(**hero.dict())
        db.add(db_hero)
        db.commit()
        db.refresh(db_hero)
        return db_hero

    @staticmethod
    def get_heroes(db: Session, skip: int = 0, limit: int = 100):
        return db.query(Hero).offset(skip).limit(limit).all()

    @staticmethod
    def get_hero(db: Session, hero_id: int):
        return db.query(Hero).filter(Hero.id == hero_id).first()
