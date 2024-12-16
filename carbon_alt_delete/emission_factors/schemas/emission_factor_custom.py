from uuid import UUID

from pydantic import Field

from carbon_alt_delete.emission_factors.schemas.emission_factor import (
    EmissionFactor,
    EmissionFactorCreate,
    EmissionFactorUpdate,
)


class EmissionFactorCustomCreate(EmissionFactorCreate):
    dataset_id: UUID = Field(alias="datasetId")
    description: str | None  # type: ignore[assignment]


class EmissionFactorCustomUpdate(EmissionFactorUpdate):
    description: str | None  # type: ignore[assignment]


class EmissionFactorCustom(EmissionFactor):
    description: str | None  # type: ignore[assignment]
    uncertainty_id: UUID | None = Field(alias="uncertaintyId", default=None)
    company_id: UUID = Field(alias="companyId")
