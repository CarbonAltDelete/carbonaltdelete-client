from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

from carbon_alt_delete.emission_factors.enums.emission_factor_value_stage_detail import EmissionFactorValueStageDetail
from carbon_alt_delete.emission_factors.enums.reporting_split import ReportingSplit


class EmissionFactorCreate(BaseModel):
    description: str
    dataset_id: UUID
    #
    stage_detail: EmissionFactorValueStageDetail = Field(alias="stageDetail")
    reporting_split: ReportingSplit = Field(alias="reportingSplit")
    keyword: str | None
    attribute: str | None
    unit: str | None
    # emission_calculation_type: EmissionCalculationType = Field(alias="emissionCalculationType")
    # stage: EmissionFactorValueStage

    model_config = ConfigDict(
        populate_by_name=True,
        from_attributes=True,
    )


class EmissionFactorUpdate(EmissionFactorCreate):
    id: UUID
    dataset_id: UUID | None = Field(alias="datasetId", default=None)  # type: ignore[assignment]


EmissionFactor = EmissionFactorUpdate
