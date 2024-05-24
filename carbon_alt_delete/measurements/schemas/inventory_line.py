from pydantic import BaseModel, Field, ConfigDict

from carbon_alt_delete.measurements.schemas.formula_term import FormulaTerm
from carbon_alt_delete.measurements.schemas.formula_term_value import FormulaTermValue
from carbon_alt_delete.measurements.schemas.measurement import Measurement


class FormulaTermValuesResponse(BaseModel):
    formula_terms: list[FormulaTerm] = Field(alias="formulaTerms", default_factory=list)
    formula_term_values: list[FormulaTermValue] = Field(alias="formulaTermValues", default_factory=list)

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
    )


class InventoryLine(BaseModel):
    measurement: Measurement
    formula_term_values: FormulaTermValuesResponse = Field(alias="formulaTermValues")

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
    )


class InventoryLinePatch(BaseModel):
    measurement: Measurement
    formula_term_values: list[FormulaTermValue] | None = Field(alias="formulaTermValues", default_factory=list)

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
    )
