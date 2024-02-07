from carbon_alt_delete.client.model_interface import ModelInterface
from carbon_alt_delete.reporting_periods.schemas.reporting_period import ReportingPeriod, ReportingPeriodCreate


class ReportingPeriodModelInterface(ModelInterface[ReportingPeriod]):
    def __init__(self, client, module):
        super().__init__(client, module, ReportingPeriod)

    def fetch_all(self, url: str = None, **kwargs):
        # TODO: replace with FAST API endpoint if refactored
        # url = f"{self.client.server}/api/{self.module.name}/{self.module.version}/reporting-periods"
        url = f"{self.client.server}/api/v1.0/reporting-periods"
        super().fetch_all(url, **kwargs)

    def create(self, url: str = None, **kwargs):
        url = f"{self.client.server}/api/v1.0/reporting-periods"
        return super().create(
            url,
            **ReportingPeriodCreate.model_validate(kwargs).model_dump(by_alias=True, mode="json"),
        )
