import os

from dotenv import load_dotenv

from carbon_alt_delete.client import connect
from carbon_alt_delete.client.carbon_alt_delete_client import CarbonAltDeleteClient


def create_company(client_company: str):
    client: CarbonAltDeleteClient
    with connect(email=os.getenv("EMAIL"), password=os.getenv("PASSWORD"), client_company=client_company) as client:
        companies = client.companies.list()
        for company in companies:
            print(company)

        reporting_periods = client.reporting_periods.list()
        for reporting_period in reporting_periods:
            print(reporting_period)


if __name__ == "__main__":
    load_dotenv()
    create_company(client_company="Carbon+Alt+Delete")
