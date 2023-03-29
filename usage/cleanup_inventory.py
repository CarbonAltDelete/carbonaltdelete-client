import os

from dotenv import load_dotenv

from carbon_alt_delete.client import connect
from carbon_alt_delete.client.carbon_alt_delete_client import CarbonAltDeleteClient


def cleanup_inventory(client_company: str):
    client: CarbonAltDeleteClient
    with connect(
        email=os.getenv("EMAIL"),
        password=os.getenv("PASSWORD"),
        client_company=client_company,
    ) as client:
        with open("measurements.txt", "r") as f:
            measurement_ids = f.readlines()
            measurement_ids = [m.replace("\n", "") for m in measurement_ids]

        for measurement_id in measurement_ids:
            response = client.measurements.delete(measurement_id)
            print(response["msg"])


if __name__ == "__main__":
    load_dotenv()
    cleanup_inventory(client_company="Talking Tables")
