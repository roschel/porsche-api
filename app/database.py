from sqlmodel import SQLModel, create_engine, Session

from config import settings
from model import *

SQLALCHEMY_DATABASE_URL = f"{settings.REPOSITORY_NAME}://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_URL}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DATABASE}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

session = Session(engine)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
