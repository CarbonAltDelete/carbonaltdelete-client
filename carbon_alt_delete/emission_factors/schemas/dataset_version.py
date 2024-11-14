from datetime import date
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class DatasetVersion(BaseModel):
    id: UUID
    dataset_id: UUID = Field(alias="datasetId")
    version: str
    description: str | None
    created_on: date = Field(alias="createdOn")

    model_config = ConfigDict(
        populate_by_name=True,
    )
