import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    # Application config
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
    APP_HOST: str = os.getenv("APP_HOST")
    APP_PORT: int = os.getenv("APP_PORT")
    APP_RELOAD: bool = ENVIRONMENT == "development"
    APP_WORKERS: int = os.getenv("APP_WORKERS", 1)

    # Database config
    MONGO_URL: str = os.getenv("MONGO_URL")
    DB_NAME: str = os.getenv("DB_NAME")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

# Initialize global settings instance
settings = Settings()