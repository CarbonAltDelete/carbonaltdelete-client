import os
from uuid import UUID

import pandas as pd
from dotenv import load_dotenv

from carbon_alt_delete.client.carbon_alt_delete_client import CarbonAltDeleteClient
from carbon_alt_delete.client.connect import connect


def update_emission_factor_after_import(file_path: str, sheet_name: str):
    client: CarbonAltDeleteClient
    with connect(
        email=os.getenv("EMAIL"),
        password=os.getenv("PASSWORD"),
        server=os.getenv("SERVER"),
    ) as client:

        # Switch to the company
        company = client.accounts.companies.one(name=os.getenv("COMPANY_NAME"))
        client.switch(company.id)

        # Excel file with emission factor mapping -> Inventory + mapped emission factor ids
        # id | ... | ... | DatasetId | DatasetVersionId | EmissionFactorId

        df = pd.read_excel(file_path, sheet_name=sheet_name)

        for i, row in df.iterrows():
            try:
                dataset_id = UUID(hex=row["DatasetId"])

                measurement = client.measurements.measurements.one(id=UUID(hex=row["Id"]))
                measurement.dataset_id = dataset_id
                measurement.dataset_version_id = UUID(hex=row["DatasetVersionId"])
                measurement.emission_factor_id = UUID(hex=row["EmissionFactorId"])

                client.measurements.measurements.update(**measurement.model_dump())
                print(f"Updated measurement {measurement.id}")
            except AttributeError:
                # Ignore empty lines, and only update the measurement
                # if an emission factor (DatasetId, DatasetVersionId, EmissionFactorId) is provided
                pass


if __name__ == "__main__":
    load_dotenv()
    update_emission_factor_after_import(
        file_path="data/data_file_with_mapped_ids.xlsx",
        sheet_name="Inventory",
    )
