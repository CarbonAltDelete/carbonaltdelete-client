from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field, NonNegativeInt


class UnitCreate(BaseModel):
    # Fields
    name: str
    sequence: NonNegativeInt
    visible: bool


class UnitUpdate(UnitCreate):
    # Fields
    id: UUID


class Unit(UnitUpdate):
    # Fields
    unit_class_id: UUID = Field(alias="unitClassId")
    company_id: UUID | None = Field(alias="companyId")
    compound_reference: str | None = Field(alias="compoundReference")

    model_config = ConfigDict(
        populate_by_name=True,
        from_attributes=True,
    )
