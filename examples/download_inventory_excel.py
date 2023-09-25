import os
import time

from dotenv import load_dotenv

from carbon_alt_delete.client.carbon_alt_delete_client import CarbonAltDeleteClient
from carbon_alt_delete.client.connect import connect
from carbon_alt_delete.reports.enums.report_file_type import ReportFileType
from carbon_alt_delete.reports.enums.report_status import ReportStatus
from carbon_alt_delete.reports.enums.report_type import ReportType


def download_inventory_excel():
    client: CarbonAltDeleteClient
    with connect(
        email=os.getenv("EMAIL"),
        password=os.getenv("PASSWORD"),
        server=os.getenv("SERVER"),
    ) as client:
        # Select reporting period, eg. by name or latest
        # reporting_period = client.reporting_periods.reporting_periods.one(name="2021")
        reporting_period = sorted(
            client.reporting_periods.reporting_periods.all(refresh=True),
            key=lambda x: x.start_date,
            reverse=True,
        )[0]
        print(reporting_period)

        # Select organizational unit, eg. by name or root
        # organizational_unit = client.organizational_units.organizational_units.one(name="Carbon+Alt+Delete")
        organizational_unit = client.organizational_units.organizational_units.root_organizational_unit()
        print(organizational_unit)

        # Initialize report generation
        report = client.reports.reports.create(
            name=f"Inventory [{reporting_period.short_name}] ({organizational_unit.name})",
            reporting_period_id=reporting_period.id,
            organizational_unit_id=organizational_unit.id,
        )

        report.report_file_status = ReportStatus.PROCESSING
        print(report)

        # Wait for report to be generated
        while report.report_file_status == ReportStatus.PROCESSING:
            time.sleep(5)
            report = client.reports.reports.one(id=report.id, refresh=True)
            print("\t", report)

        # Download report(s)
        print("Download Inventory Excel")
        file = client.reports.reports.download(report, file_type=ReportFileType.XLSX, report_type=ReportType.DATA_DUMP)
        # Save report to file
        with open("inventory.xlsx", "wb") as f:
            f.write(file)

        print("Download GHG Protocol Excel")
        file = client.reports.reports.download(
            report,
            file_type=ReportFileType.XLSX,
            report_type=ReportType.GHG_PROTOCOL,
        )
        # Save report to file
        with open("ghg_protocol.xlsx", "wb") as f:
            f.write(file)

        print("Download ISO 14064-1 pdf")
        file = client.reports.reports.download(report, file_type=ReportFileType.PDF, report_type=ReportType.ISO14064)
        # Save report to file
        with open("iso_14064-1.pdf", "wb") as f:
            f.write(file)

        # Clean up report history
        success = client.reports.reports.delete(report.id)
        print(success)


if __name__ == "__main__":
    load_dotenv()
    download_inventory_excel()
