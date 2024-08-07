from uuid import UUID

from pydantic import Field

from carbon_alt_delete.emission_factors.schemas.emission_factor import (
    EmissionFactor,
    EmissionFactorCreate,
    EmissionFactorUpdate,
)


class EmissionFactorCustomCreate(EmissionFactorCreate):
    dataset_id: UUID = Field(alias="datasetId")
    description: str | None


class EmissionFactorCustomUpdate(EmissionFactorUpdate):
    description: str | None


class EmissionFactorCustom(EmissionFactor):
    description: str | None

    company_id: UUID = Field(alias="companyId")
