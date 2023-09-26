from typing import io
from uuid import UUID

import requests

from carbon_alt_delete.client.model_interface import ModelInterface
from carbon_alt_delete.reports.enums.report_file_type import ReportFileType
from carbon_alt_delete.reports.enums.report_type import ReportType
from carbon_alt_delete.reports.schemas.report import Report, ReportCreate


class ReportModelInterface(ModelInterface[Report]):
    def __init__(self, client, module):
        super().__init__(client, module, Report)

    def fetch_all(self, url: str = None):
        url = f"{self.client.server}/api/{self.module.name}/{self.module.version}/reports"
        super().fetch_all(url)

    def fetch_one(
        self,
        id: UUID,
        url: str = None,
        **kwargs,
    ):
        url = f"{self.client.server}/api/{self.module.name}/{self.module.version}/reports/{id}"
        return super().fetch_one(url, **kwargs)

    def create(self, url: str = None, **kwargs):
        url = f"{self.client.server}/api/{self.module.name}/{self.module.version}/reports"
        return super().create(
            url,
            **ReportCreate.model_validate(kwargs).model_dump(by_alias=True, mode="json"),
        )

    def download_url(self, report: Report, file_type: ReportFileType, report_type: ReportType) -> str:
        url = f"{self.client.server}/api/{self.module.name}/{self.module.version}/reports/{report.id}/presigned-url"
        return (
            self.client.get(
                url,
                params={
                    "fileType": file_type,
                    "reportType": report_type,
                },
            )
            .json()
            .get("url")
        )

    def download(self, report: Report, file_type: ReportFileType, report_type: ReportType) -> io:
        url = self.download_url(report, file_type, report_type)
        return requests.get(url).content

    def delete(self, id: UUID, url: str = None, **kwargs):
        url = f"{self.client.server}/api/{self.module.name}/{self.module.version}/reports/{id}"
        return super().delete(url)
