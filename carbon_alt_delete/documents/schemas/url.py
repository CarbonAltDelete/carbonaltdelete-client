from uuid import UUID

from pydantic import BaseModel, HttpUrl


class Url(BaseModel):
    url: HttpUrl
    id: UUID
