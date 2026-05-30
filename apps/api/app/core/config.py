from pydantic_settings import BaseSettings

class Settings(BaseSettings):

    GOOGLE_CLIENT_ID: str
    GOOGLE_CLIENT_SECRET: str
    GOOGLE_REDIRECT_URI: str
    SESSION_SECRET: str
    FRONTEND_URL: str = "http://localhost:3000"
    DATABASE_URL: str
    class Config:
        env_file = ".env"

settings = Settings()