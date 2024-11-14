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
    uncertainty_id: UUID = Field(alias="uncertaintyId")
    company_id: UUID = Field(alias="companyId")
