from typing import Optional
from datetime import datetime
from sqlmodel import Session, Field, SQLModel, create_engine

from .configs import settings

engine = create_engine(settings.db_url, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        try:
            yield session
        finally:
            session.close()


if __name__ == "__main__":
    create_db_and_tables()
