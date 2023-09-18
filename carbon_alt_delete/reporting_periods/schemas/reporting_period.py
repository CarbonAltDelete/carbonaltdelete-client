from datetime import date
from uuid import UUID

from pydantic import BaseModel, Field


class ReportingPeriod(BaseModel):
    id: UUID
    short_name: str | None = Field(alias="shortName")
    description: str | None
    start_date: date = Field(alias="startDate")
    end_date: date = Field(alias="endDate")
    is_locked: bool = Field(alias="isLocked")
