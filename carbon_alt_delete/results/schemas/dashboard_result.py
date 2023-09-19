from uuid import UUID

from pydantic import BaseModel, Field


class DashboardResult(BaseModel):
    activity_category_id: UUID = Field(alias="activityCategoryId")
    activity_group_id: UUID = Field(alias="activityGroupId")
    organization_unit_id: UUID = Field(alias="organizationUnitId")
    reporting_period_id: UUID = Field(alias="reportingPeriodId")

    aggregated_business_metric_value: float | None
    aggregated_emission_value: float
    aggregated_relative_value: float | None
