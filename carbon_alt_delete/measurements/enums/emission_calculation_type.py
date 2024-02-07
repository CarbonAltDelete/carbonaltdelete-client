from enum import Enum


class EmissionCalculationType(str, Enum):
    DEFAULT = "DEFAULT"
    WITH_RADIATIVE_FORCING = "WITH_RADIATIVE_FORCING"
    WITHOUT_RADIATIVE_FORCING = "WITHOUT_RADIATIVE_FORCING"
    MARKET_BASED = "MARKET_BASED"
    LOCATION_BASED = "LOCATION_BASED"

    def __lt__(self, other: "EmissionCalculationType"):
        order = {
            EmissionCalculationType.DEFAULT: 0,
            EmissionCalculationType.MARKET_BASED: 1,
            EmissionCalculationType.LOCATION_BASED: 2,
            EmissionCalculationType.WITH_RADIATIVE_FORCING: 3,
            EmissionCalculationType.WITHOUT_RADIATIVE_FORCING: 4,
        }
        return order[self] < order[other]
