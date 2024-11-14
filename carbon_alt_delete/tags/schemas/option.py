from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field, NonNegativeInt


class OptionCreate(BaseModel):
    value: str | None
    field_id: UUID = Field(alias="fieldId")
    sibling_position: NonNegativeInt = Field(alias="position")

    model_config = ConfigDict(
        populate_by_name=True,
        from_attributes=True,
    )


class Option(OptionCreate):
    id: UUID
