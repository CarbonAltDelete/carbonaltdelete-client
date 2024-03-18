from carbon_alt_delete.client.model_interface import ModelInterface
from carbon_alt_delete.emission_factors.schemas.emission_factor_custom import (
    EmissionFactorCustom,
)


class EmissionFactorCustomModelInterface(ModelInterface[EmissionFactorCustom]):
    def __init__(self, client, module):
        super().__init__(client, module, EmissionFactorCustom)

    def create(self, url: str = None, **kwargs) -> EmissionFactorCustom:
        url = f"{self.client.server}/api/{self.module.name}/{self.module.version}/emission-factors"
        response = self.client.post(
            url,
            json=kwargs,
        )
        if not kwargs.get("skip_state", False):
            self._upsert_one(response.json()["emissionFactor"], kwargs.get("key_field", "id"))
            return self._select_one(response.json()["emissionFactor"][kwargs.get("key_field", "id")])
        else:
            return self._member_class(**(response.json()["emissionFactor"]))

    def update(self, **kwargs) -> EmissionFactorCustom:
        url = f"{self.client.server}/api/{self.module.name}/{self.module.version}/emission-factors/{kwargs['id']}"
        return super().update(url=url, **kwargs)
