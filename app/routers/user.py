from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class User(BaseModel):
    id: int
    name: str
    email: str

items = []

@router.post("/users/")
async def create_user(user: User):
    items.append(user)
    return items

@router.put("/users/{id}")
async def update_user(id: int, user: User):
    for idx, u in enumerate(items):
        if u.id == id:
            items[idx] = user
            return items
    raise HTTPException(status_code=404, detail="User not found")

@router.delete("/users/{id}")
async def delete_user(id: int):
    for idx, u in enumerate(items):
        if u.id == id:
            items.pop(idx)
            return items
    raise HTTPException(status_code=404, detail="User not found")

@router.get("/users/{id}")
async def get_user(id: int):
    for u in items:
        if u.id == id:
            return u
    raise HTTPException(status_code=404, detail="User not found")