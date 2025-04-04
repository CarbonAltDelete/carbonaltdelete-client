import logging
import os

from carbon_alt_delete.client.carbon_alt_delete_client import CarbonAltDeleteClient
from carbon_alt_delete.client.connect import connect

logger = logging.getLogger(__name__)


def list_all_companies():
    client: CarbonAltDeleteClient
    with connect(
        email=os.getenv("EMAIL"),
        password=os.getenv("PASSWORD"),
        server=os.getenv("SERVER"),
    ) as client:
        logger.info("All companies")
        for c in client.accounts.companies.all(refresh=True):
            logger.info(c)

        logger.info("Client companies")
        for c in client.accounts.companies.all(is_consulting_company=False):
            logger.info(c)
            client_company_id = c.id
            client_company_name = c.name

        logger.info("Demo companies")
        for c in client.accounts.companies.all(is_demo_company=True):
            logger.info(c)

        logger.info("One company")
        logger.info(
            client.accounts.companies.one(
                name=client_company_name,
                is_consulting_company=False,
            ),
        )

        client.switch(client_company_id)

        logger.info("Reporting periods")
        for r in client.reporting_periods.reporting_periods.all():
            logger.info(r)

        logger.info("Organizational Units")
        for r in client.organizational_units.organizational_units.all():
            logger.info(r)

        logger.info("Root Organizational Unit")
        logger.info(
            client.organizational_units.organizational_units.root_organizational_unit(),
        )


if __name__ == "__main__":
    list_all_companies()
