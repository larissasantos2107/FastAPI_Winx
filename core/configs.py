from pydantic.v1 import BaseSettings
from sqlalchemy.orm import declarative_base

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    DB_URL: str = "mysql+asyncy://root@127.0.0.1:3306/winx"
    DBBaseModel = declarative_base()
    
    class Config:
        case_Sensitive = False
        env_file = "env"
        
settings = Settings()

# começa por essa 1