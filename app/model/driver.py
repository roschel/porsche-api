from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import validator
from sqlmodel import SQLModel, Field


class Driver(SQLModel, table=True):
    id: Optional[UUID] = Field(default=None, primary_key=True)
    name: str = Field(nullable=False)
    email: str = Field(default=None, index=True, nullable=False, sa_column_kwargs={"unique": True})
    cpf: str = Field(default=None, index=True, nullable=False, sa_column_kwargs={"unique": True})
    rg: str = Field(default=None, nullable=False, sa_column_kwargs={"unique": True})
    is_active: bool = Field(default=False)
    created_at: datetime = Field(default=datetime.now())
    updated_at: datetime = Field(default=datetime.now())

    @validator("cpf", "rg")
    def remove_special_characters(cls, v):
        if "." in v or "-" in v:
            return v.replace(".", "").replace("-", "")
        return v
