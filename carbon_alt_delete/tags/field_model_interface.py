from carbon_alt_delete.client.model_interface import ModelInterface
from carbon_alt_delete.tags.schemas.field import Field, FieldCreate


class FieldModelInterface(ModelInterface[Field]):
    def __init__(self, client, module):
        super().__init__(client, module, Field)

    def fetch_all(self, url: str | None = None, **kwargs):
        url = f"{self.client.server}/api/{self.module.name}/{self.module.version}/fields"
        super().fetch_all(url, **kwargs)

    def create(self, url: str | None = None, **kwargs):
        url = f"{self.client.server}/api/{self.module.name}/{self.module.version}/fields"
        return super().create(
            url,
            **FieldCreate.model_validate(kwargs).model_dump(by_alias=True, mode="json"),
        )
