from typing import Union
from fastapi import FastAPI, Depends
from sqlmodel import Session, select
from datetime import datetime, timedelta
from fastapi.middleware.cors import CORSMiddleware

from app.db import create_db_and_tables, get_session
from app.models.temperature import Temperature


app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/temperature/")
def select_temperature(session: Session = Depends(get_session)):
    now = datetime.now()
    one_hour_ago = now - timedelta(hours=1)

    statement = select(Temperature).order_by(Temperature.id.desc()).limit(20)
    results = session.exec(statement).all()
    return results


@app.post("/temperature/", response_model=Temperature)
def create_temperature(temperature: Temperature, session=Depends(get_session)):
    session.add(temperature)
    session.commit()
    session.refresh(temperature)
    return temperature
