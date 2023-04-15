from typing import Union
from fastapi import FastAPI
from app.db import create_db_and_tables, Temperature, engine
from sqlmodel import Session, select
from json import JSONEncoder

app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/temperature/")
def select_temperature():
    with Session(engine) as session:
        statement = select(Temperature)
        results = session.exec(statement)
        for temperature in results:
            return temperature


@app.post("/temperature/")
def create_temperature(temperature: Temperature):
    temperature_to_create = Temperature.from_orm(temperature)
    with Session(engine) as session:
        session.add(temperature_to_create)
        session.commit()
        session.refresh(temperature_to_create)
        return temperature_to_create
