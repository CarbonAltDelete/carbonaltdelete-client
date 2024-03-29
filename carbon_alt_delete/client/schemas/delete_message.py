from uuid import UUID

from pydantic import BaseModel


class DeleteMessage(BaseModel):
    id: UUID
    msg: str
