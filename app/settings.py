from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Tomato"
    app_version: str = "0.1.0"
    app_description: str = "A simple tomato app"

    class Config:
        case_sensitive = True
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()