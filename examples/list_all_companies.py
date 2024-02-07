import os

from dotenv import load_dotenv

from carbon_alt_delete.client.carbon_alt_delete_client import CarbonAltDeleteClient
from carbon_alt_delete.client.connect import connect


def list_all_companies():
    client: CarbonAltDeleteClient
    with connect(
        email=os.getenv("EMAIL"),
        password=os.getenv("PASSWORD"),
        server=os.getenv("SERVER"),
    ) as client:
        print("\nAll companies")
        for c in client.accounts.companies.all(refresh=True):
            print(c)

        print("\nClient companies")
        for c in client.accounts.companies.all(is_consulting_company=False):
            print(c)
            client_company_id = c.id
            client_company_name = c.name

        print("\nDemo companies")
        for c in client.accounts.companies.all(is_demo_company=True):
            print(c)

        print("\nOne company")
        print(client.accounts.companies.one(name=client_company_name, is_consulting_company=False))

        client.switch(client_company_id)

        print("\nReporting periods")
        for r in client.reporting_periods.reporting_periods.all():
            print(r)

        print("\nOrganizational Units")
        for r in client.organizational_units.organizational_units.all():
            print(r)

        print("\nRoot Organizational Unit")
        print(client.organizational_units.organizational_units.root_organizational_unit())


if __name__ == "__main__":
    load_dotenv()
    list_all_companies()
