import uuid

from database import session
from model import Driver
from repository.postgres_repository import PostgresRepository

postgres = PostgresRepository(session=session)


def get_all_drivers():
    result = postgres.get_all(model=Driver)
    return result


def insert_driver(driver: Driver):
    driver.id = uuid.uuid4()
    result = postgres.save(driver)
    return result
