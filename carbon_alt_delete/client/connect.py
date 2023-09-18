from contextlib import contextmanager

from carbon_alt_delete.client.carbon_alt_delete_client import CarbonAltDeleteClient


def connect(
    email: str | None = None,
    password: str | None = None,
    api_key: str | None = None,
    secret: str | None = None,
    server: str | None = None,
) -> CarbonAltDeleteClient:
    if email is not None:
        return _connect_email_password(
            email=email,
            password=password,
            server=server,
        )
    if api_key is not None:
        return _connect_api_key_secret(
            api_key=api_key,
            secret=secret,
            server=server,
        )


@contextmanager
def _connect_email_password(
    email: str,
    password: str,
    server: str | None = None,
) -> CarbonAltDeleteClient:
    client = CarbonAltDeleteClient(
        server=server,
    )
    client.authenticate_email_password(
        email=email,
        password=password,
    )

    yield client

    client.disconnect()


@contextmanager
def _connect_api_key_secret(
    api_key: str,
    secret: str,
    server: str | None = None,
) -> CarbonAltDeleteClient:
    client = CarbonAltDeleteClient(
        server=server,
    )
    client.authenticate_api_key_secret(
        api_key=api_key,
        secret=secret,
    )

    yield client

    client.disconnect()
