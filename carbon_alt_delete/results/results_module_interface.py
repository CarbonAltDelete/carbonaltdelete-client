from carbon_alt_delete.client.module_interface import ModuleInterface
from carbon_alt_delete.results.dashboard_model_interface import DashboardModelInterface


class ResultsModuleInterface(ModuleInterface):
    def __init__(self, client):
        super().__init__("results", "v1")
        self.dashboard: DashboardModelInterface = DashboardModelInterface(
            client=client,
            module=self,
        )
