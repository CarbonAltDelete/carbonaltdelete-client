from carbon_alt_delete.client.model_interface import ModelInterface
from uncertainties.schemas.uncertainty import Uncertainty


class UncertaintyModelInterface(ModelInterface[Uncertainty]):
    def __init__(self, client, module):
        super().__init__(client, module, Uncertainty)

    def fetch_all(self, url: str | None = None, params={}, **kwargs):
        url = f"{self.client.server}/api/{self.module.name}/{self.module.version}/uncertainties"
        super().fetch_all(url, **kwargs)
