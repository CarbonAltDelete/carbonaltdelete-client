from uuid import UUID

from pydantic import BaseModel, Field, ConfigDict


class FormulaTermValue(BaseModel):
    id: UUID
    formula_term_id: UUID = Field(alias="formulaTermId")
    value: float | str | None = None
    unit: str | None = None
    measurement_id: UUID = Field(alias="measurementId")

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
    )
