from carbon_alt_delete.accounts.schemas.company import Company
from carbon_alt_delete.client.model_interface import ModelInterface


class CompanyModelInterface(ModelInterface):
    def __init__(self, client, module):
        super().__init__(client, module, Company)

    def fetch_all(
        self,
        url: str = None,
    ):
        url = f"{self.client.server}/api/{self.module.name}/{self.module.version}/companies"
        super().fetch_all(url)
