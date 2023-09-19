from uuid import UUID

from pydantic import BaseModel, Field

from carbon_alt_delete.activities.schemas.activity_category_type import ActivityCategoryType


class ActivityCategory(BaseModel):
    id: UUID
    name: str | None
    activity_group_id: UUID = Field(alias="activityGroupId")
    is_used: bool = Field(alias="isUsed")
    is_default: bool = Field(alias="isDefault")
    activity_category_type: ActivityCategoryType = Field(alias="activityCategoryType")
    description: str | None
    position: int | None


class ActivityCategoryCreate(BaseModel):
    name: str | None = None
    activity_group_id: UUID = Field(alias="activityGroupId")
    is_used: bool = Field(alias="isUsed")
    is_default: bool = Field(alias="isDefault")
    activity_category_type: ActivityCategoryType = Field(alias="activityCategoryType")
    description: str | None = None
    position: int | None = None
