from http import HTTPStatus

import requests

from carbon_alt_delete.client.model_interface import ModelInterface
from carbon_alt_delete.client.exceptions import ClientException


class ReportingPeriodInterface(ModelInterface):
    def list(
        self,
    ) -> list[dict]:
        url = f"{self.client.server}/api/{self.client.api_version}/reporting-periods"
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
