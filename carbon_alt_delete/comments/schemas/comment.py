from uuid import UUID

from pydantic import BaseModel, Field, ConfigDict


class CommentCreate(BaseModel):
    content: str | None
    commented_entity_id: UUID | None = Field(alias="commentedEntityId")
    emission_factor_id: UUID | None = Field(alias="emissionFactorId", default=None)
    is_free_field: bool = Field(alias="isFreeField", default=True)
    parent_comment_id: UUID | None = Field(alias="parentCommentId", default=None)

    model_config = ConfigDict(
        populate_by_name=True,
    )


class Comment(CommentCreate):
    content: str | None
    commented_entity_id: UUID | None = Field(alias="commentedEntityId")
    emission_factor_id: UUID | None = Field(alias="emissionFactorId")
    is_free_field: bool = Field(alias="isFreeField")
    parent_comment_id: UUID | None = Field(alias="parentCommentId")
