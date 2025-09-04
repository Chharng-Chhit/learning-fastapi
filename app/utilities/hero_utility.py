from sqlalchemy.orm import Session
from app.models.model import Hero
from app.schemas.hero_schema import HeroCreate

class HeroUtility:
    @staticmethod
    def create_hero(db: Session, hero: HeroCreate) -> Hero:
        db_hero = Hero(**hero.dict()) # {"id": 1, "name": "....."}
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
    
    @staticmethod
    def update_hero(db: Session, hero_id: int, hero_data: HeroCreate) -> Hero:
        hero = db.query(Hero).filter(Hero.id == hero_id).first()
        if hero:
            for key, value in hero_data.dict().items():
                setattr(hero, key, value)
            db.commit()
            db.refresh(hero)
        return hero

    @staticmethod
    def delete_hero(db: Session, hero_id: int) -> Hero | None:
        hero = db.query(Hero).filter(Hero.id == hero_id).first()
        if not hero:
            return None
        db.delete(hero)
        db.commit()
        return hero