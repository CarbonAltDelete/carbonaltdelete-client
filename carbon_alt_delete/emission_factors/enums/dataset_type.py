from enum import Enum


class DatasetType(str, Enum):

    FUELS = "FUELS"
    PROCESS_AND_FUGITIVE_EMISSIONS = "PROCESS_AND_FUGITIVE_EMISSIONS"
    ELECTRICITY = "ELECTRICITY"
    HEAT_AND_STEAM = "HEAT_AND_STEAM"
    TRANSPORT_GOODS = "TRANSPORT_GOODS"
    TRANSPORT_PEOPLE = "TRANSPORT_PEOPLE"
    WASTE = "WASTE"
    GOODS_BY_MASS = "GOODS_BY_MASS"
    GOODS_BY_VALUE = "GOODS_BY_VALUE"
    ASSETS = "ASSETS"

    BASE = "BASE"
    ECOINVENT = "ECOINVENT"
    CUSTOM = "CUSTOM"
