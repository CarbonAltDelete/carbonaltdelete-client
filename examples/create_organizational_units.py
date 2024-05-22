import logging
import os

import pandas as pd
from dotenv import load_dotenv
from pydantic import BaseModel, field_validator, NonNegativeInt
from rich.logging import RichHandler

from carbon_alt_delete.client.carbon_alt_delete_client import CarbonAltDeleteClient
from carbon_alt_delete.client.connect import connect

logging.basicConfig(level=logging.INFO, handlers=[RichHandler(level="NOTSET")])
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
        logger.info(f"Switching to company {company_name}")
        company = client.accounts.companies.one(name=company_name)
        client.switch(company.id)

        # Build organizational units
        root = client.organizational_units.organizational_units.root_organizational_unit()

        # Loop through organizational units and create new if not existing
        for i, organizational_unit in enumerate(organizational_units):
            org_unit = client.organizational_units.organizational_units.first(
                name=organizational_unit.name,
                position=organizational_unit.position,
            )
            if org_unit is None:
                logger.info(f"[{i+1}] Creating {organizational_unit.name}")
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
                logger.debug(f"[{i+1} Exists {organizational_unit.name}")

        logger.info("\nOrganizational Units:")
        client.organizational_units.organizational_units.print_tree()


if __name__ == "__main__":
    load_dotenv()
    df = pd.read_excel(
        os.getenv("FILE_PATH"),
        sheet_name=os.getenv("SHEET_NAME"),
    )
    list_organizational_units = [
        OrganizationalUnitInput(
            name=row["Name"],
            parent_name=row["Parent"],
            position=row["Position"],
        )
        for _, row in df.iterrows()
    ]

    create_company_structure(
        company_name=os.getenv("COMPANY_NAME"),
        organizational_units=list_organizational_units,
    )
