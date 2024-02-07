from enum import Enum


class ReportingSplit(str, Enum):
    DEFAULT = "DEFAULT"
    MARKET_LOCATION_BASED = "MARKET_LOCATION_BASED"
    RADIATIVE_FORCING = "RADIATIVE_FORCING"
