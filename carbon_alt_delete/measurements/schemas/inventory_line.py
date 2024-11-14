from uuid import UUID

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


class CustomField(BaseModel):
    field_id: UUID = Field(alias="fieldId")
    option_id: UUID | None = Field(alias="optionId")
    measurement_id: UUID = Field(alias="measurementId")

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
    )


class InventoryLine(BaseModel):
    measurement: Measurement
    formula_term_values: FormulaTermValuesResponse = Field(alias="formulaTermValues")
    custom_fields: list[CustomField] = Field(alias="customFields", default_factory=list)

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
    )


class InventoryLinePatch(BaseModel):
    measurement: Measurement | None = None
    formula_term_values: list[FormulaTermValue] | None = Field(alias="formulaTermValues", default_factory=list)
    custom_fields: list[CustomField] | None = Field(alias="customFields", default_factory=list)

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
    )
