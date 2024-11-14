from carbon_alt_delete.client.model_interface import ModelInterface
from tags.schemas.option import Option, OptionCreate


class OptionModelInterface(ModelInterface[Option]):
    def __init__(self, client, module):
        super().__init__(client, module, Option)

    def fetch_all(self, url: str = None, **kwargs):
        url = f"{self.client.server}/api/{self.module.name}/{self.module.version}/options"
        super().fetch_all(url, **kwargs)

    def create(self, url: str = None, **kwargs):
        url = f"{self.client.server}/api/{self.module.name}/{self.module.version}/options"
        return super().create(
            url,
            **OptionCreate.model_validate(kwargs).model_dump(by_alias=True, mode="json"),
        )

    def update(self, **kwargs):
        url = f"{self.client.server}/api/{self.module.name}/{self.module.version}/options/{kwargs['id']}"
        return super().update(url=url, **kwargs)
