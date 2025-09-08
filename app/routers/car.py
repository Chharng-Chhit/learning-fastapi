from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.core.db import get_session
from app.schemas.car_schema import CarCreate, CarRead
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