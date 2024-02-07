from uuid import UUID

from pydantic import BaseModel, Field, ConfigDict


class RedirectKey(BaseModel):
    redirect_key: str = Field(alias="redirectKey")


class RedirectKeyCreate(BaseModel):
    api_key: UUID = Field(alias="apiKey")
    secret: str
    user_id: UUID = Field(alias="userId")

    model_config = ConfigDict(
        populate_by_name=True,
        from_attributes=True,
    )
