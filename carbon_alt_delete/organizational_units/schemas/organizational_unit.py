from uuid import UUID

from pydantic import BaseModel, NonNegativeInt, Field


class OrganizationalUnit(BaseModel):
    id: UUID
    name: str | None
    position: NonNegativeInt
    parent_organizational_unit_id: UUID | None = Field(alias="parentId")
