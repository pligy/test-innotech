from pydantic import BaseSettings

class Settings(BaseSettings):
    admin_username: str
    admin_password: str

    class Config:
        env_file = ".env"

settings = Settings()
