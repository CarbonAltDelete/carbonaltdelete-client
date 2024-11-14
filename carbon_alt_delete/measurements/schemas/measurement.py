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
    parent_activity_category_id: UUID | None = Field(alias="parentActivityCategoryId")
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
    volume_uncertainty_id: UUID | None = Field(alias="volumeUncertaintyId", default=None)

    volume: float | None
    unit: str | None
    emissions: float | None

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
    )


class MeasurementCreate(BaseModel):
    description: str | None = None

    input_type: str | None = Field(alias="inputType", default=None)
    keyword: str | None = None
    detail: str | None = Field(alias="attribute", default=None)

    consumption: float | None = None
    unit: str | None = None

    activity_category_id: UUID | None = Field(alias="activityCategoryId", default=None)
    parent_activity_category_id: UUID | None = Field(alias="parentActivityCategoryId", default=None)
    reporting_period_id: UUID = Field(alias="reportingPeriodId")
    organizational_unit_id: UUID = Field(alias="organizationalUnitId")
    traded_from_organizational_unit_id: UUID | None = Field(alias="tradedFromOrganizationalUnitId", default=None)

    date_granularity: DateGranularity = Field(alias="dateGranularity", default=DateGranularity.YEAR)
    show_as_range: bool = Field(alias="showAsRange", default=False)
    start_date: date = Field(alias="startDate")
    end_date: date = Field(alias="endDate")

    dataset_id: UUID | None = Field(alias="datasetId", default=None)
    dataset_version_id: UUID | None = Field(alias="datasetVersionId", default=None)
    emission_factor_id: UUID | None = Field(alias="emissionFactorId", default=None)
    volume_uncertainty_id: UUID | None = Field(alias="volumeUncertaintyId", default=None)

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
    )


class MeasurementUpdate(MeasurementCreate):
    pass
