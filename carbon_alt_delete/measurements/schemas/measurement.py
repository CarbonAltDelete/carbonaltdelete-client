from datetime import date
from uuid import UUID

from pydantic import BaseModel, Field, ConfigDict

from carbon_alt_delete.measurements.enums.date_granularity import DateGranularity


class Measurement(BaseModel):
    id: UUID
    description: str | None

    input_type: str | None = Field(alias="inputType")
    keyword: str | None
    detail: str | None = Field(alias="attribute")

    activity_category_id: UUID | None = Field(alias="activityCategoryId")
    reporting_period_id: UUID = Field(alias="reportingPeriodId")
    organizational_unit_id: UUID = Field(alias="organizationalUnitId")
    traded_from_organizational_unit_id: UUID | None = Field(alias="tradedFromOrganizationalUnitId")

    date_granularity: DateGranularity = DateGranularity.YEAR
    show_as_range: bool = Field(alias="showAsRange")
    start_date: date = Field(alias="startDate")
    end_date: date = Field(alias="endDate")

    dataset_id: UUID | None = Field(alias="datasetId")
    dataset_version_id: UUID | None = Field(alias="datasetVersionId")
    emission_factor_id: UUID | None = Field(alias="emissionFactorId")

    volume: float | None
    unit: str | None
    emissions: float | None


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
    traded_from_organizational_unit_id: UUID | None = Field(alias="tradedFromOrganizationalUnitId")

    date_granularity: DateGranularity = DateGranularity.YEAR
    show_as_range: bool = False
    start_date: date
    end_date: date

    dataset_id: UUID | None = None
    dataset_version_id: UUID | None = None
    emission_factor_id: UUID | None = None

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
    )


class MeasurementUpdate(MeasurementCreate):
    id: UUID
