import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

from carbon_alt_delete.emission_factors.enums.emission_factor_value_stage import EmissionFactorValueStage
from carbon_alt_delete.emission_factors.schemas.greenhouse_gases import GreenhouseGases
from carbon_alt_delete.emission_factors.schemas.supplement_emissions import SupplementEmissions
from carbon_alt_delete.measurements.enums.emission_calculation_type import EmissionCalculationType


class EmissionFactorValueUpdate(BaseModel):
    id: UUID

    greenhouse_gases: GreenhouseGases = Field(alias="greenhouseGases")
    supplement_emissions: SupplementEmissions = Field(alias="supplementEmissions")

    model_config = ConfigDict(
        populate_by_name=True,
        from_attributes=True,
    )


class EmissionFactorValue(EmissionFactorValueUpdate):
    value_co2eq_aggregated: float | None = Field(alias="valueCo2eqAggregated")
    alternative_value_co2eq_aggregated: float | None = Field(alias="alternativeValueCo2eqAggregated", default=None)

    valid_from: datetime.date = Field(alias="validFrom")
    valid_to: datetime.date = Field(alias="validTo")

    unit: str | None
    emission_factor_id: UUID = Field(alias="emissionFactorId")
    referring_emission_factor_id: UUID | None = Field(alias="referringEmissionFactorId")

    stage: EmissionFactorValueStage
    emission_calculation_type: EmissionCalculationType = Field(alias="emissionCalculationType")
