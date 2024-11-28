from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

from uncertainties.enums.model_type import ModelType


class UncertaintyCreate(BaseModel):
    name: str
    lower_bound_percentage: int = Field(alias="lowerBoundPercentage")
    upper_bound_percentage: int = Field(alias="upperBoundPercentage")
    ln_sq_gsd: float = Field(alias="lnSqGsd")

    field: str
    model_type: ModelType = Field(alias="modelType")
    model_config = ConfigDict(
        populate_by_name=True,
        protected_namespaces=("_",),
    )


class Uncertainty(UncertaintyCreate):
    id: UUID
