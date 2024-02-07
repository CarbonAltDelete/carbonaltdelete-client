from carbon_alt_delete.client.model_interface import ModelInterface
from carbon_alt_delete.results.schemas.dashboard_result import DashboardResult


class DashboardModelInterface(ModelInterface[DashboardResult]):
    def __init__(self, client, module):
        super().__init__(client, module, DashboardResult)

    def fetch_all(self, url: str = None, params={}):
        url = f"{self.client.server}/api/{self.module.name}/{self.module.version}/dashboard-data"
        super().fetch_all(url, params=params)
