from carbon_alt_delete.client.model_interface import ModelInterface
from carbon_alt_delete.units.schemas.unit import Unit


class UnitModelInterface(ModelInterface[Unit]):
    def __init__(self, client, module):
        super().__init__(client, module, Unit)

    def fetch_all(self, url: str | None = None, params: dict = {}, **kwargs):
        url = f"{self.client.server}/api/{self.module.name}/{self.module.version}/units"
        super().fetch_all(url, **kwargs)
