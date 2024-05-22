from carbon_alt_delete.client.model_interface import ModelInterface
from carbon_alt_delete.emission_factors.schemas.emission_factor import EmissionFactor


class EmissionFactorModelInterface(ModelInterface[EmissionFactor]):
    def __init__(self, client, module):
        super().__init__(client, module, EmissionFactor)

    def fetch_one(self, url: str = None, **kwargs):
        url = (
            f"{self.client.server}/api/{self.module.name}/{self.module.version}/"
            f"emission-factors?datasetVersionId_equals={kwargs['dataset_version_id']}"
            f"&emissionFactorId_equals={kwargs['id']}"
        )
        response = self.client.get(url)
        self._upsert_one(response.json()["emissionFactors"][0])
