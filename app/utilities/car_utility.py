from sqlalchemy.orm import Session
from app.models.model import Cars
from app.schemas.car_schema import CarCreate, CarRead, CarUpdate

class CarUtility:
    @staticmethod
    def create_car(db: Session, car: CarCreate) -> Cars:
        data = Cars(**car.dict())
        db.add(data)
        db.commit()
        db.refresh(data)
        return data
        
    def get_car(db: Session, car_id: int) -> CarRead:
        return db.query(Cars).filter(Cars.id == car_id).first()
    def get_all_cars(db: Session) -> list[CarRead]:
        return db.query(Cars).all()
    
    def update_car(db: Session, id: int, car: CarUpdate) -> CarRead:
        data = db.query(Cars).filter(Cars.id == id).first()
        if not data:
            return None
        for key, value in car.dict(exclude_unset=True).items():
            setattr(data, key, value)
        db.commit()
        db.refresh(data)
        return data
    
    def delete_car(db: Session, car_id: int) -> Cars:
        car = db.query(Cars).filter(Cars.id == car_id).first()
        if car:
            db.delete(car)
            db.commit()
        return car
    
        
    