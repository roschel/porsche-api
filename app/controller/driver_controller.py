from typing import List

from fastapi import APIRouter

from model import Driver
from service.driver_service import get_all_drivers, insert_driver

driver_route = APIRouter()


@driver_route.get(
    '',
    response_model=List[Driver]
)
def get_drivers():
    result = get_all_drivers()
    return result


@driver_route.post(
    '',
    response_model=Driver
)
def create_driver(driver: Driver):
    result = insert_driver(driver)
    return result
