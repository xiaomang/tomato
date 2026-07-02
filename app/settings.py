from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Tomato"
    app_version: str = "0.1.0"
    app_description: str = "A simple tomato app"

    # MongoDB 配置
    mongo_uri: str = "mongodb://localhost:27017/tomato"
    mongo_db_name: str = "tomato"
    
    class Config:
        case_sensitive = True
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()