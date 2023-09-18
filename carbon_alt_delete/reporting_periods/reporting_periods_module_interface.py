from carbon_alt_delete.client.module_interface import ModuleInterface
from carbon_alt_delete.reporting_periods.reporting_periods_model_interface import ReportingPeriodModelInterface


class ReportingPeriodsModuleInterface(ModuleInterface):
    def __init__(self, client):
        super().__init__("reporting-periods", "v1")
        self.reporting_periods: ReportingPeriodModelInterface = ReportingPeriodModelInterface(
            client=client,
            module=self,
        )
