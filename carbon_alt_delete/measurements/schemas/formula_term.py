from uuid import UUID

from pydantic import BaseModel, Field, ConfigDict


class FormulaTerm(BaseModel):
    id: UUID
    formula_id: UUID = Field(alias="formulaId")
    name: str

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
    )
