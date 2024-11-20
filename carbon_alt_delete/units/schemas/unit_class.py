from uuid import UUID

from pydantic import BaseModel, ConfigDict, NonNegativeFloat


class UnitClassCreate(BaseModel):
    name: str
    sequence: NonNegativeFloat

    model_config = ConfigDict(
        populate_by_name=True,
        from_attributes=True,
    )


class UnitClass(UnitClassCreate):
    id: UUID
