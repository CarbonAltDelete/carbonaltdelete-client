from contextlib import contextmanager

from carbon_alt_delete.client.carbon_alt_delete_client import CarbonAltDeleteClient


@contextmanager
def connect(
    email: str,
    password: str,
    client_company: str,
    api_base_url: str | None = None,
) -> CarbonAltDeleteClient:
    client = CarbonAltDeleteClient(email, password, client_company, api_base_url)
    client.authenticate()

    yield client

    client.disconnect()
