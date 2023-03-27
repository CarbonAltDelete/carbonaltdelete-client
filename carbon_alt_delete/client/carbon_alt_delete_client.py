from http import HTTPStatus

import requests


class CarbonAltDeleteClient:
    def __init__(
        self,
        email: str,
        password: str,
        company_name: str,
        api_base_url: str = "",
    ):
        self.email = email
        self.password = password
        self.company_name = company_name
        self.api_base_url = api_base_url
        self._authentication_token: str | None = None

    def authenticate(self):
        url = f"{self.api_base_url}"
        response = requests.post(url)
        assert response.status == HTTPStatus.OK
        self._authentication_token = response.json().get("accessToken", None)

    @property
    def authentication_token(self) -> str:
        return self._authentication_token
