from pydantic import BaseSettings

class Settings(BaseSettings):
    email_address: str
    email_password: str

    class Config:
        env_file = ".env"

settings = Settings()