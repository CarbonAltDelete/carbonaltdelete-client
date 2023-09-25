from carbon_alt_delete.client.module_interface import ModuleInterface
from carbon_alt_delete.reports.report_model_interface import ReportModelInterface


class ReportsModuleInterface(ModuleInterface):
    def __init__(self, client):
        super().__init__("reports", "v1")
        self.reports: ReportModelInterface = ReportModelInterface(
            client=client,
            module=self,
        )
