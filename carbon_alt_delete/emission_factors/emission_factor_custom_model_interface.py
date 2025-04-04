from uuid import UUID

from carbon_alt_delete.client.model_interface import ModelInterface
from carbon_alt_delete.emission_factors.schemas.emission_factor_custom import (
    EmissionFactorCustom,
)


class EmissionFactorCustomModelInterface(ModelInterface[EmissionFactorCustom]):
    def __init__(self, client, module):
        super().__init__(client, module, EmissionFactorCustom)

    def create(self, url: str | None = None, **kwargs) -> EmissionFactorCustom:
        url = f"{self.client.server}/api/{self.module.name}/{self.module.version}/emission-factors"
        response = self.client.post(
            url,
            json=kwargs,
        )
        if not kwargs.get("skip_state", False):
            self._upsert_one(
                response.json()["emissionFactor"],
                kwargs.get("key_field", "id"),
            )
            return self._select_one(
                response.json()["emissionFactor"][kwargs.get("key_field", "id")],
            )
        else:
            return self._member_class(**(response.json()["emissionFactor"]))

    def update(self, **kwargs) -> EmissionFactorCustom:
        url = f"{self.client.server}/api/{self.module.name}/{self.module.version}/emission-factors/{kwargs['id']}"
        return super().update(url=url, **kwargs)

    def update_uncertainty(
        self,
        emission_factor_id: UUID,
        uncertainty_id: UUID,
    ) -> EmissionFactorCustom:
        url = f"{self.client.server}/api/{self.module.name}/{self.module.version}/emission-factors/{emission_factor_id}/uncertainty"
        response = self.client.patch(
            url,
            json={
                "uncertaintyId": str(uncertainty_id),
            },
        )

        return response.json()

    def regenerate_fingerprint(self, emission_factor_id: UUID) -> str:
        url = f"{self.client.server}/api/{self.module.name}/{self.module.version}/emission-factors/{emission_factor_id}/regenerate-fingerprint"
        response = self.client.put(
            url,
        )

        return response.json()["fingerprint"]

    def find_by_fingerprint(
        self,
        dataset_version_id: UUID,
        fingerprint: str,
    ) -> EmissionFactorCustom | None:
        url = f"{self.client.server}/api/{self.module.name}/{self.module.version}/emission-factors"
        response = self.client.get(
            url,
            params={
                "datasetVersionId_equals": dataset_version_id,
                "fingerprint_contains": fingerprint,
            },
        )
        if response.status_code == 200:
            return self._member_class(**response.json()["emissionFactors"][0])
        else:
            return None
