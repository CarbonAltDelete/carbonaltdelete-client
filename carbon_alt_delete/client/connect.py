from contextlib import contextmanager

from carbon_alt_delete.client.carbon_alt_delete_client import CarbonAltDeleteClient


@contextmanager
def connect(
    email: str,
    password: str,
    server: str | None = None,
) -> CarbonAltDeleteClient:
    client = CarbonAltDeleteClient(
        email=email,
        password=password,
        server=server,
    )
    client.authenticate()

    yield client

    client.disconnect()
