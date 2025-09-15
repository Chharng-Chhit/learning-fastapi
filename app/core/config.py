import secrets
from typing import Optional, Dict, Any
from pydantic_settings import BaseSettings
from pydantic import validator
class Settings(BaseSettings):
    API_V1_STR: str = "/api"
    PROJECT_NAME: str = "OUSA BEK BOY"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    ALGORITHM: str = "HS256"
    
    class Config: 
        # Corrected line:
        env_file = ".env"  
        env_file_encoding = "utf-8"

settings = Settings()