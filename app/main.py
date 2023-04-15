from typing import Union
from fastapi import FastAPI, Depends
from sqlmodel import Session, select

from app.db import create_db_and_tables, get_session
from app.models.temperature import Temperature


app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/temperature/")
def select_temperature(session: Session = Depends(get_session)):
    statement = select(Temperature)
    results = session.exec(statement).all()
    return results


@app.post("/temperature/", response_model=Temperature)
def create_temperature(temperature: Temperature, session=Depends(get_session)):
    session.add(temperature)
    session.commit()
    session.refresh(temperature)
    return temperature
