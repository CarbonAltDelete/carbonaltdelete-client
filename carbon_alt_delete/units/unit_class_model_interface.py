from carbon_alt_delete.client.model_interface import ModelInterface
from units.schemas.unit_class import UnitClass


class UnitClassModelInterface(ModelInterface[UnitClass]):
    def __init__(self, client, module):
        super().__init__(client, module, UnitClass)

    def fetch_all(self, url: str | None = None, params: dict = {}, **kwargs):
        url = f"{self.client.server}/api/{self.module.name}/{self.module.version}/unit-classes"
        super().fetch_all(url, **kwargs)
