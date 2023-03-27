from carbon_alt_delete.client.carbon_alt_delete_client import CarbonAltDeleteClient


def connect(
    email: str,
    password: str,
    company_name: str,
    api_base_url: str = "",
) -> CarbonAltDeleteClient:
    client = CarbonAltDeleteClient(email, password, company_name, api_base_url)
    client.authenticate()

    yield client

    client.disconnect()
