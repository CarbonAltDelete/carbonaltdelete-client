import logging
import os

import pandas as pd
from dotenv import load_dotenv
from pydantic import BaseModel, field_validator, NonNegativeInt

from carbon_alt_delete.client.carbon_alt_delete_client import CarbonAltDeleteClient
from carbon_alt_delete.client.connect import connect

logger = logging.getLogger(__name__)


class OrganizationalUnitInput(BaseModel):
    name: str
    parent_name: str | None
    position: NonNegativeInt

    @field_validator("parent_name", mode="before")
    @classmethod
    def replace_nan(cls, v):
        return None if pd.isna(v) else v


def create_company_structure(
    company_name: str,
    organizational_units: list[OrganizationalUnitInput],
):
    client: CarbonAltDeleteClient
    with connect(
        email=os.getenv("EMAIL"),
        password=os.getenv("PASSWORD"),
        server=os.getenv("SERVER"),
    ) as client:
        # Switch to company
        company = client.accounts.companies.one(name=company_name)
        client.switch(company.id)

        # Build organizational units
        root = client.organizational_units.organizational_units.root_organizational_unit()

        # Loop through organizational units and create new if not existing
        for organizational_unit in organizational_units:
            logger.info(organizational_unit.name)
            org_unit = client.organizational_units.organizational_units.first(name=organizational_unit.name)
            if org_unit is None:
                parent = (
                    root
                    if organizational_unit.parent_name is None
                    else client.organizational_units.organizational_units.one(name=organizational_unit.parent_name)
                )

                client.organizational_units.organizational_units.create(
                    name=organizational_unit.name,
                    parent_organizational_unit_id=parent.id,
                    position=organizational_unit.position,
                )
            else:
                logger.info(f"Organizational unit {organizational_unit.name} already exists")

        logger.info("\nOrganizational Units:")
        client.organizational_units.organizational_units.print_tree()


if __name__ == "__main__":
    load_dotenv()
    df = pd.read_excel(os.getenv("FILE_PATH"))
    list_organizational_units = [
        OrganizationalUnitInput(
            name=row["Org Unit"],
            parent_name=row["Parent Company"],
            position=row["Position"],
        )
        for _, row in df.iterrows()
    ]

    create_company_structure(
        company_name=os.getenv("COMPANY_NAME"),
        organizational_units=list_organizational_units,
    )
