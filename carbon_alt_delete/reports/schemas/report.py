from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field, ConfigDict

from carbon_alt_delete.reports.enums.report_status import ReportStatus
from carbon_alt_delete.reports.enums.report_type import ReportType


class Report(BaseModel):
    id: UUID
    name: str
    json_version: int = Field(alias="jsonVersion")
    created_on: datetime = Field(alias="createdOn")
    report_status: ReportStatus = Field(alias="reportStatus")
    report_file_status: ReportStatus | None = Field(alias="reportFileStatus", default=None)
    done_report_files: int | None = Field(alias="doneReportFiles", default=None)
    count_report_files: int | None = Field(alias="countReportFiles", default=None)


class ReportCreate(BaseModel):
    name: str
    reporting_period_id: UUID = Field(alias="reportingPeriodId")
    base_reporting_period_id: UUID = Field(alias="baseReportingPeriodId")
    organizational_unit_id: UUID = Field(alias="organizationUnitId")
    report_type: ReportType = Field(alias="reportType")

    model_config = ConfigDict(
        populate_by_name=True,
        from_attributes=True,
    )
