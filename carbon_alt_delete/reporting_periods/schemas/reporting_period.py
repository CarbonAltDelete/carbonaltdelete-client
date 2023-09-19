from datetime import date
from uuid import UUID

from pydantic import BaseModel, Field, ConfigDict


class ReportingPeriod(BaseModel):
    id: UUID
    short_name: str | None = Field(alias="shortName")
    description: str | None
    start_date: date = Field(alias="startDate")
    end_date: date = Field(alias="endDate")
    is_locked: bool = Field(alias="isLocked")


class ReportingPeriodCreate(BaseModel):
    description: str | None = None
    short_name: str = Field(alias="shortName")
    start_date: date = Field(alias="startDate")
    end_date: date = Field(alias="endDate")
    is_locked: bool = Field(alias="isLocked", default=False)

    model_config = ConfigDict(
        populate_by_name=True,
        from_attributes=True,
    )
