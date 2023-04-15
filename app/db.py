from typing import Optional
from datetime import datetime

from sqlmodel import Field, SQLModel, create_engine, func

from .configs import settings


class Temperature(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    temperature_value: float = Field(nullable=False)
    created_at: datetime = Field(default=datetime.now, nullable=False)


engine = create_engine(settings.db_url, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


if __name__ == "__main__":
    create_db_and_tables()
