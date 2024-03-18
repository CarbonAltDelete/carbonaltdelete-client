from pydantic import BaseModel


class GreenhouseGasSplit(BaseModel):
    factor: float | None = None
    value: float | None = None


class GreenhouseGases(BaseModel):
    CO2EQ: GreenhouseGasSplit
    CO2: GreenhouseGasSplit
    CH4: GreenhouseGasSplit
    N2O: GreenhouseGasSplit
    HFCS: GreenhouseGasSplit
    PFCS: GreenhouseGasSplit
    SF6: GreenhouseGasSplit
    NF3: GreenhouseGasSplit
    OTHERS: GreenhouseGasSplit
    BIOGENIC: GreenhouseGasSplit
