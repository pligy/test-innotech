from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    default_port: int
    admin_username: str
    admin_password: str

    class Config:
        env_file = ".env"


settings = Settings()
