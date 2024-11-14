from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field as FieldPydantic, NonNegativeInt


class FieldCreate(BaseModel):
    name: str | None
    sibling_position: NonNegativeInt = FieldPydantic(alias="position")


class Field(FieldCreate):
    id: UUID

    model_config = ConfigDict(
        populate_by_name=True,
        from_attributes=True,
    )
