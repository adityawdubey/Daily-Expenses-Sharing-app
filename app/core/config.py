# from pydantic import BaseSettings
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgres://aniketdubey:vicky@localhost:5432/postgres"

settings = Settings()
