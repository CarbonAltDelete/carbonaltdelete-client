import time

from dotenv import load_dotenv

from carbon_alt_delete.client.carbon_alt_delete_client import CarbonAltDeleteClient
from carbon_alt_delete.client.connect import connect
import os


def sleep_refresh_token():
    # Create a client
    client: CarbonAltDeleteClient
    with connect(
        email=os.getenv("EMAIL"),
        password=os.getenv("PASSWORD"),
        server=os.getenv("SERVER"),
    ) as client:
        start_time = time.time()
        while True:
            print(f"\nTime elapsed: {time.time()-start_time:.0f} seconds")
            auth_token = client.authentication_token

            # Get all companies
            client.accounts.companies.all(refresh=True)

            time.sleep(10)

            if auth_token != client.authentication_token:
                print("Token refreshed")
                print(f"\nTime elapsed: {time.time()-start_time:.0f} seconds")
                break


if __name__ == "__main__":
    load_dotenv()
    sleep_refresh_token()
