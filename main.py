from fastapi import FastAPI
from app.core.db import create_db_and_tables
from app.routers.hero import router as hero_router
from app.routers.animal import router as animal_router
from app.routers.car import router as car_router

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(hero_router)
app.include_router(animal_router)
app.include_router(car_router)

@app.get("/")
def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
