import os
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "fm_dashboard"
    mongod_uri: str = "mongodb://localhost:27017/"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
