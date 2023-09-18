import os

from dotenv import load_dotenv

from carbon_alt_delete.accounts.schemas.user_status import UserStatus
from carbon_alt_delete.client.carbon_alt_delete_client import CarbonAltDeleteClient
from carbon_alt_delete.client.connect import connect


def redirect_client_user():
    client: CarbonAltDeleteClient
    with connect(
        api_key=os.getenv("API_KEY"),
        secret=os.getenv("SECRET"),
        server=os.getenv("SERVER"),
    ) as client:
        print("\nClient users", len(client.accounts.users.all(is_consultant=False, status=UserStatus.ACTIVE)))
        for c in client.accounts.users.all(is_consultant=False, status=UserStatus.ACTIVE):
            print(c)

        print("\nFirst client user")
        client_user = client.accounts.users.first(is_consultant=False, status=UserStatus.ACTIVE)
        print("\t", client_user.email)

        redirect_key = client.keys.redirect.create(
            user_id=client_user.id,
            api_key=os.getenv("API_KEY"),
            secret=os.getenv("SECRET"),
        )

        print("\t", f"{os.getenv('FRONTEND', os.getenv('SERVER'))}/redirect?key={redirect_key.redirect_key}")


if __name__ == "__main__":
    load_dotenv()
    redirect_client_user()
