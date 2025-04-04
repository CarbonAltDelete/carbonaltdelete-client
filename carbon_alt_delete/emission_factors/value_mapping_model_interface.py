from carbon_alt_delete.client.model_interface import ModelInterface
from carbon_alt_delete.emission_factors.schemas.value_mapping import ValueMapping


class ValueMappingModelInterface(ModelInterface[ValueMapping]):
    def __init__(self, client, module):
        super().__init__(client, module, ValueMapping)

    def create(self, **kwargs) -> ValueMapping:
        url = f"{self.client.server}/api/{self.module.name}/{self.module.version}/value-mappings"
        return super().create(url=url, **kwargs)

    def update(self, **kwargs) -> ValueMapping:
        url = f"{self.client.server}/api/{self.module.name}/{self.module.version}/value-mappings/{kwargs['id']}"
        return super().update(url=url, **kwargs)
