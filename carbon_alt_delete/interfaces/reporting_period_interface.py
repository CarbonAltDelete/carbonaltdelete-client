from http import HTTPStatus

import requests

from carbon_alt_delete.client.abort import abort
from carbon_alt_delete.client.client_interface import ClientInterface


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
            return abort(status_code=response.status_code, detail=response.content)

        return response.json()
