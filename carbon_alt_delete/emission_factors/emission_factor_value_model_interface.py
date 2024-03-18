from uuid import UUID

from carbon_alt_delete.client.model_interface import ModelInterface
from carbon_alt_delete.emission_factors.schemas.emission_factor_value import EmissionFactorValue


class EmissionFactorValueModelInterface(ModelInterface[EmissionFactorValue]):
    def __init__(self, client, module):
        super().__init__(client, module, EmissionFactorValue)

    def latest_set(
            self,
            emission_factor_id: UUID,
            dataset_version_id: UUID | None = None,
            split_set: bool = True,
            **kwargs,
    ) -> list[EmissionFactorValue]:
        url = f"{self.client.server}/api/{self.module.name}/{self.module.version}/emission-factor-values"
        params = {
            "emissionFactorId_equals": emission_factor_id,
            "validTo_latest": True,
            "splitSet_equals": split_set,
        }
        if dataset_version_id:
            params["datasetVersionId_equals"] = dataset_version_id
        response = self.client.get(url, params=params)
        self._upsert_many(response.json())
        return [self._select_one(r["id"]) for r in response.json()]


    def latest(
            self,
            emission_factor_id: UUID,
            dataset_version_id: UUID | None = None,
            **kwargs,
    ) -> EmissionFactorValue:
        result = self.latest_set(
            emission_factor_id=emission_factor_id,
            dataset_version_id=dataset_version_id,
            split_set=False,
            **kwargs,
        )
        assert len(result) == 1
        return result[0]

    def update(self, **kwargs) -> EmissionFactorValue:
        url = f"{self.client.server}/api/{self.module.name}/{self.module.version}/emission-factor-values/{kwargs['id']}"
        return super().update(url=url, **kwargs)
