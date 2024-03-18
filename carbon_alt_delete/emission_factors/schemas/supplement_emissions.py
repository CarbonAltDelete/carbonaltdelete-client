from pydantic import BaseModel, Field


class SupplementEmissions(BaseModel):
    generation: float | None
    transmission_and_distribution: float | None = Field(alias="transmissionAndDistribution")
