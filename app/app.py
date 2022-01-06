from fastapi import FastAPI

from controller.driver_controller import driver_route
from database import create_db_and_tables

app = FastAPI(
    title="API Coupon",
    description="API responsável por cadastrar e obter informações de cupons.",
    version="0.1.0",
    root_path="",
)

app.include_router(driver_route, prefix='/drivers', tags=['drivers'])


@app.on_event("startup")
def create_database():
    create_db_and_tables()
