from uuid import UUID

from pydantic import BaseModel, Field


class FormulaTerm(BaseModel):
    id: UUID
    formula_id: UUID = Field(alias="formulaId")
    name: str
