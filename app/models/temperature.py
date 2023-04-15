from sqlmodel import Field, SQLModel
from typing import Optional
from datetime import datetime


class Temperature(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    temperature_value: float = Field(nullable=False)
    created_at: datetime = Field(default=datetime.now(), nullable=False)
