from functools import lru_cache
import os
from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    # POSTGRES
    REPOSITORY_NAME: str = Field('', description="Nome do repository")
    POSTGRES_URL: str = Field('', description="Nome do repository")
    POSTGRES_USER: str = Field('', description="Usuário de acesso do banco de dados")
    POSTGRES_PORT: int = Field(None, description="Porta de acesso do banco de dados")
    POSTGRES_DATABASE: str = Field('', description="Nome do banco de dados")
    POSTGRES_PASSWORD: str = Field('', description="Senha do banco de dados")

    class Config:
        env_file = os.getenv('ENV_FILE', '../.env')


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()