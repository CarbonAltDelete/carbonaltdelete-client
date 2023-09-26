import os

from dotenv import load_dotenv

from carbon_alt_delete.activities.schemas.activity_category_type import ActivityCategoryType
from carbon_alt_delete.client.carbon_alt_delete_client import CarbonAltDeleteClient
from carbon_alt_delete.client.connect import connect
from carbon_alt_delete.measurements.schemas.measurement import MeasurementCreate


def create_inventory_entries():
    client: CarbonAltDeleteClient
    with connect(
        email=os.getenv("EMAIL"),
        password=os.getenv("PASSWORD"),
        server=os.getenv("SERVER"),
    ) as client:
        # Select reporting period, eg. by name or latest
        # reporting_period = client.reporting_periods.reporting_periods.one(name="2021")
        reporting_period = sorted(
            client.reporting_periods.reporting_periods.all(),
            key=lambda x: x.start_date,
            reverse=True,
        )[0]
        print(reporting_period)

        # Select organizational unit, eg. by name or root
        # organizational_unit = client.organizational_units.organizational_units.one(name="Carbon+Alt+Delete")
        organizational_unit = client.organizational_units.organizational_units.root_organizational_unit()
        print(organizational_unit)

        ## ELECTRICITY CONSUMPTION
        print("\nELECTRICITY CONSUMPTION")
        print("-" * 80)
        # Select activity category for which to create inventory entries
        electricity = client.activities.activity_categories.one(
            activity_category_type=ActivityCategoryType.PURCHASED_ELECTRICITY,
            is_used=True,
            is_default=True,
        )

        # Create Measurement
        data = MeasurementCreate(
            keyword="Belgium",
            description="Electricity consumption in office Brussels",
            detail="Gray",
            consumption=10000,
            unit="kWh",
            start_date=reporting_period.start_date,
            end_date=reporting_period.end_date,
            activity_category_id=electricity.id,
            reporting_period_id=reporting_period.id,
            organizational_unit_id=organizational_unit.id,
        )
        measurement = client.measurements.measurements.create_entry(data)
        print(measurement)

        ## HEATING CONSUMPTION
        print("\nHEATING CONSUMPTION")
        print("-" * 80)

        # Select activity category for which to create inventory entries
        heating = client.activities.activity_categories.one(
            activity_category_type=ActivityCategoryType.STATIONARY_COMBUSTION,
            is_used=True,
            is_default=True,
        )

        # Create Measurement
        data = MeasurementCreate(
            keyword="Natural gas",
            description="Heating in office Brussels",
            detail=None,
            consumption=10000,
            unit="kWh",
            start_date=reporting_period.start_date,
            end_date=reporting_period.end_date,
            activity_category_id=heating.id,
            reporting_period_id=reporting_period.id,
            organizational_unit_id=organizational_unit.id,
        )

        measurement = client.measurements.measurements.create_entry(data)
        print(measurement)


if __name__ == "__main__":
    load_dotenv()
    create_inventory_entries()
