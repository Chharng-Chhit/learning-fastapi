from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from app.schemas.user_schema import User

class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str
    
class TokenPayload(BaseModel):
    sub: Optional[str] = None
    exp: Optional[int] = None
    roles: List[str]
    
class TokenData(BaseModel):
    username: Optional[str] = None
    roles: List[str] = ["User"]