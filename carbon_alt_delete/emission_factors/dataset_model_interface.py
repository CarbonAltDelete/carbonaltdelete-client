from carbon_alt_delete.client.model_interface import ModelInterface
from carbon_alt_delete.emission_factors.schemas.dataset import Dataset


class DatasetModelInterface(ModelInterface[Dataset]):
    def __init__(self, client, module):
        super().__init__(client, module, Dataset)

    def fetch_all(self, **kwargs):
        url = f"{self.client.server}/api/{self.module.name}/{self.module.version}/datasets"
        super().fetch_all(url, **kwargs)

    def fetch_one(self, url: str = None, **kwargs):
        url = (
            f"{self.client.server}/api/{self.module.name}/{self.module.version}/"
            f"emission-factors?datasetVersionId_eq={kwargs['dataset_version_id']}"
            f"&emissionFactorId_eq={kwargs['id']}"
        )
        response = self.client.get(url)
        self._upsert_one(response.json()["emissionFactors"][0])
