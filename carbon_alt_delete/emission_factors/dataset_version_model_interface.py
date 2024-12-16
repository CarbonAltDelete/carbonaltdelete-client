from carbon_alt_delete.client.model_interface import ModelInterface
from carbon_alt_delete.emission_factors.schemas.dataset_version import DatasetVersion


class DatasetVersionModelInterface(ModelInterface[DatasetVersion]):
    def __init__(self, client, module):
        super().__init__(client, module, DatasetVersion)

    def fetch_all(self, **kwargs):
        url = f"{self.client.server}/api/{self.module.name}/{self.module.version}/dataset-versions"
        super().fetch_all(url, **kwargs)
