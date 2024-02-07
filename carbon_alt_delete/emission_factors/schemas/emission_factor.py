from uuid import UUID

from carbon_alt_delete.emission_factors.enums.emission_factor_value_stage_detail import EmissionFactorValueStageDetail
from carbon_alt_delete.emission_factors.enums.emission_factor_value_stage import EmissionFactorValueStage
from carbon_alt_delete.emission_factors.enums.reporting_split import ReportingSplit
from carbon_alt_delete.measurements.enums.emission_calculation_type import EmissionCalculationType
from pydantic import BaseModel, Field


class EmissionFactor(BaseModel):
    id: UUID
    stage_detail: EmissionFactorValueStageDetail = Field(alias="stageDetail")
    reporting_split: ReportingSplit = Field(alias="reportingSplit")
    keyword: str | None
    attribute: str | None
    unit: str | None
    emission_calculation_type: EmissionCalculationType = Field(alias="emissionCalculationType")
    stage: EmissionFactorValueStage
