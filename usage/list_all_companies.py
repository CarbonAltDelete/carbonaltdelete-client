import os

from dotenv import load_dotenv

from carbon_alt_delete.client import connect
from carbon_alt_delete.client.carbon_alt_delete_client import CarbonAltDeleteClient


def list_all_companies():
    client: CarbonAltDeleteClient
    with connect(
        email=os.getenv("EMAIL"),
        password=os.getenv("PASSWORD"),
        server=os.getenv("SERVER"),
    ) as client:
        print("\nAll companies")
        for c in client.accounts.companies.all():
            print(c)

        print("\nClient companies")
        for c in client.accounts.companies.all(is_consulting_company=False):
            print(c)
            client_company_id = c.id

        print("\nDemo companies")
        for c in client.accounts.companies.all(is_demo_company=True):
            print(c)

        print("\nOne company")
        print(client.accounts.companies.one(name="Carbon+Alt+Delete"))

        client.switch(client_company_id)


if __name__ == "__main__":
    load_dotenv()
    list_all_companies()
