from uuid import UUID

from pydantic import BaseModel


class ActivityGroup(BaseModel):
    id: UUID
    name: str | None
    description: str | None
    position: int


class ActivityGroupCreate(BaseModel):
    name: str | None
    description: str | None
    position: int
