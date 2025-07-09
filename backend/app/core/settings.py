from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    database_url: str

    # Core
    frontend_urls: str

    class Config:
        env_file = ".env"

settings = Settings()
