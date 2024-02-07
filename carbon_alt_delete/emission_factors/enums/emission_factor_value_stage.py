from enum import Enum
from functools import cached_property


class EmissionFactorValueStage(str, Enum):
    PRINCIPAL = "PRINCIPAL"
    ENERGY_AND_FUEL_GENERATION = "ENERGY_AND_FUEL_GENERATION"
    ENERGY_AND_FUEL_TRANSMISSION_DISTRIBUTION = "ENERGY_AND_FUEL_TRANSMISSION_DISTRIBUTION"

    @cached_property
    def label(self) -> str:
        return {
            EmissionFactorValueStage.PRINCIPAL: "Principal",
            EmissionFactorValueStage.ENERGY_AND_FUEL_GENERATION: "Generation",
            EmissionFactorValueStage.ENERGY_AND_FUEL_TRANSMISSION_DISTRIBUTION: "Transmission & Distribution",
        }[self]
