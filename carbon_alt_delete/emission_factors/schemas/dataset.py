from uuid import UUID

from pydantic import BaseModel, Field

from carbon_alt_delete.emission_factors.enums.dataset_type import DatasetType


class Dataset(BaseModel):
    id: UUID
    name: str | None
    short_name: str | None = Field(alias="shortName")
    is_default: bool = Field(alias="isDefault")
    is_selected: bool = Field(alias="isSelected")
    is_integrated: bool = Field(alias="isIntegrated")
    is_shared: bool = Field(alias="isShared")
    dataset_type: DatasetType = Field(alias="datasetType")
    company_id: UUID | None = Field(alias="companyId")
    company_name: str | None = Field(alias="companyName", default=None)

    class Config:
        from_attributes = True
