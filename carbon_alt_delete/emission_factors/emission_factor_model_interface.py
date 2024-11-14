from carbon_alt_delete.client.model_interface import ModelInterface
from carbon_alt_delete.emission_factors.schemas.emission_factor import EmissionFactor, EmissionFactorCreate
from carbon_alt_delete.emission_factors.schemas.emission_factor_value import EmissionFactorValue


class EmissionFactorModelInterface(ModelInterface[EmissionFactor]):
    def __init__(self, client, module):
        super().__init__(client, module, EmissionFactor)

    def fetch_one(self, url: str | None = None, **kwargs):
        url = (
            f"{self.client.server}/api/{self.module.name}/{self.module.version}/"
            f"emission-factors?datasetVersionId_equals={kwargs['dataset_version_id']}"
            f"&emissionFactorId_equals={kwargs['id']}"
        )
        response = self.client.get(url)
        self._upsert_one(response.json()["emissionFactors"][0])

    def create(self, **kwargs) -> tuple[EmissionFactor, EmissionFactorValue]:
        url = f"{self.client.server}/api/{self.module.name}/{self.module.version}/emission-factors"
        response = self.client.post(
            url=url,
            json=EmissionFactorCreate(**kwargs).model_dump(by_alias=True, mode="json"),
        )
        emission_factor = EmissionFactor(**response.json()["emissionFactor"])
        emission_factor_value = EmissionFactorValue(**response.json()["latestEmissionFactorValue"])
        self._upsert_one(response.json()["emissionFactor"])
        return emission_factor, emission_factor_value
