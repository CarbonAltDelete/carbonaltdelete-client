from http import HTTPStatus

import requests

from carbon_alt_delete.client.client_interface import ClientInterface
from carbon_alt_delete.client.exceptions import ClientException


class ReportingPeriodInterface(ClientInterface):
    def list(
        self,
    ) -> list[dict]:
        url = f"{self.client.api_base_url}/api/{self.client.api_version}/reporting-periods"
        response = requests.get(
            url,
            headers={
                "Authorization": self.client.authentication_token,
            },
            timeout=self.client.timeout,
        )
        if response.status_code != HTTPStatus.OK:
            raise ClientException(response=response)

        return response.json()
