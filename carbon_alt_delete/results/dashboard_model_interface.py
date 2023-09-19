from carbon_alt_delete.client.model_interface import ModelInterface
from carbon_alt_delete.results.schemas.dashboard_result import DashboardResult


class DashboardModelInterface(ModelInterface[DashboardResult]):
    def __init__(self, client, module):
        super().__init__(client, module, DashboardResult)

    def fetch_all(self, url: str = None):
        # TODO: replace with FAST API endpoint if refactored
        # url = f"{self.client.server}/api/{self.module.name}/{self.module.version}/..."
        url = f"{self.client.server}/api/v1.0/dashboard/v2"
        super().fetch_all(url)
