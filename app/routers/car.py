from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.core.db import get_session
from app.schemas.car_schema import CarCreate, CarRead, CarUpdate
from app.utilities.car_utility import CarUtility

router = APIRouter(prefix="/cars", tags=["cars"])
@router.post('/', )
def create_car(car: CarCreate, session: Session = Depends(get_session)):
    data = CarUtility.create_car(session, car)
    return data

@router.get('/{id}', response_model=CarRead)
def find_car(id: int, session: Session=Depends(get_session)):
    car = CarUtility.get_car(session, id)
    return car

@router.get('/', response_model=list[CarRead])
def get_all_cars(session: Session = Depends(get_session)):
    car = CarUtility.get_all_cars(session)
    return car

@router.put('/{id}')
def update_car(id: int, car: CarUpdate, session: Session = Depends(get_session)):
    updated_car = CarUtility.update_car(session, id, car)
    if not updated_car:
        raise HTTPException(status_code=404, detail="Car not found")
    return updated_car
@router.delete('/{id}')
def delete_car(id: int, session: Session = Depends(get_session)):
    deleted_car = CarUtility.delete_car(session, id)
    return deleted_car
