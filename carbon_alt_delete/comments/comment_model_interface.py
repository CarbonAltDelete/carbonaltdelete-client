from carbon_alt_delete.client.model_interface import ModelInterface
from carbon_alt_delete.comments.schemas.comment import CommentCreate, Comment


class CommentModelInterface(ModelInterface[Comment]):
    def __init__(self, client, module):
        super().__init__(client, module, Comment)

    def create(self, url: str | None = None, **kwargs):
        url = f"{self.client.server}/api/{self.module.name}/{self.module.version}/free-fields"
        return super().create(
            url,
            **CommentCreate.model_validate(kwargs).model_dump(by_alias=True, mode="json"),
        )
