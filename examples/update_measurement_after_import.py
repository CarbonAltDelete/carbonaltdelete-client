import os
from uuid import UUID

import pandas as pd
from dotenv import load_dotenv

from carbon_alt_delete.client.carbon_alt_delete_client import CarbonAltDeleteClient
from carbon_alt_delete.client.connect import connect


def update_measurement_after_import(trade_file_path: str, sheet_name: str):
    client: CarbonAltDeleteClient
    with connect(
        email=os.getenv("EMAIL"),
        password=os.getenv("PASSWORD"),
        server=os.getenv("SERVER"),
    ) as client:
        # Create Company and switch to it
        company = client.accounts.companies.one(name=os.getenv("COMPANY_NAME"))
        client.switch(company.id)

        organizational_units = client.organizational_units.organizational_units.all()
        org_dict_by_name = {org.name: org for org in organizational_units}

        # Excel file with intercompany trade data
        # id | ... | Traded From | .... | DatasetId | DatasetVersionId | EmissionFactorId

        df = pd.read_excel(trade_file_path, sheet_name=sheet_name)

        for i, row in df.iterrows():
            # Get the organizational units
            org_traded_from = org_dict_by_name[row["Traded from"]]

            # Create the intercompany trade
            measurement = client.measurements.measurements.one(id=UUID(hex=row["Id"]))
            measurement.traded_from_organizational_unit_id = org_traded_from.id

            # Linked an emission factor from a connected dataset
            try:
                measurement.dataset_id = UUID(hex=row["DatasetId"])
                measurement.dataset_version_id = UUID(hex=row["DatasetVersionId"])
                measurement.emission_factor_id = UUID(hex=row["EmissionFactorId"])
            except AttributeError:
                # Ignore empty lines, and only update the intercompany trade
                pass

            client.measurements.measurements.update(**measurement.model_dump())


if __name__ == "__main__":
    load_dotenv()
    update_measurement_after_import(
        trade_file_path="data/data_file_with_mapped_ids.xlsx",
        sheet_name="ICT",
    )
