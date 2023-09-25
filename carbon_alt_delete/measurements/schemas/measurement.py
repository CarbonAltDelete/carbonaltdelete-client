from datetime import date
from uuid import UUID

from pydantic import BaseModel, Field, ConfigDict

from carbon_alt_delete.measurements.enums.date_granularity import DateGranularity


class Measurement(BaseModel):
    id: UUID


class MeasurementCreate(BaseModel):
    description: str | None = None

    input_type: str | None = None
    keyword: str | None = None
    detail: str | None = Field(alias="attribute")

    consumption: float | None = None
    unit: str | None = None

    activity_category_id: UUID | None = None
    reporting_period_id: UUID
    organizational_unit_id: UUID

    date_granularity: DateGranularity = DateGranularity.YEAR
    show_as_range: bool = False
    start_date: date
    end_date: date

    dataset_id: UUID | None = None

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
    )