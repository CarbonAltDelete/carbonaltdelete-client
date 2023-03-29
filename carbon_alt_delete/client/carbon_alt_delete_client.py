from http import HTTPStatus

import requests
from requests.models import Response

from carbon_alt_delete.client.exceptions import ClientException
from carbon_alt_delete.interfaces.company_interface import CompanyInterface
from carbon_alt_delete.interfaces.measurement_interface import MeasurementInterface
from carbon_alt_delete.interfaces.reporting_period_interface import ReportingPeriodInterface


class CarbonAltDeleteClient:
    def __init__(
        self,
        email: str,
        password: str,
        client_company: str,
        api_base_url: str | None = None,
    ):
        self.email = email
        self.password = password
        self.client_company = client_company
        if api_base_url is None:
            self.api_base_url = "https://cad-backend-production.herokuapp.com"
        else:
            self.api_base_url = api_base_url

        self._api_version = "v1.0"
        self._authentication_token: str | None = None

        self.companies: CompanyInterface = CompanyInterface(self)
        self.measurements: MeasurementInterface = MeasurementInterface(self)
        self.reporting_periods: ReportingPeriodInterface = ReportingPeriodInterface(self)

        # config
        self.timeout = 15000

    def authenticate(self):
        url = f"{self.api_base_url}/api/{self.api_version}/accounts/auth"
        response = requests.post(
            url,
            json={
                "email": self.email,
                "password": self.password,
            },
            timeout=self.timeout,
        )
        if response.status_code != HTTPStatus.OK:
            self._authentication_token = None
            raise ClientException(response=response)

        self._authentication_token = response.json().get("accessToken", None)

        companies = self.companies.list()
        company = [c for c in companies if c["name"] == self.client_company][0]

        self._switch(company_id=company["id"])

    def disconnect(self):
        self._authentication_token = None

    def _switch(self, company_id: str):
        url = f"{self.api_base_url}/api/{self.api_version}/accounts/companies/switch"
        response = requests.post(
            url,
            headers={
                "Authorization": self.authentication_token,
            },
            json={
                "companyId": company_id,
            },
            timeout=self.timeout,
        )
        if response.status_code != HTTPStatus.OK:
            self._authentication_token = None
            raise ClientException(response=response)

        self._authentication_token = response.json().get("accessToken", None)

    @property
    def authentication_token(self) -> str | None:
        if self._authentication_token is not None:
            return f"Bearer {self._authentication_token}"
        else:
            return None

    @property
    def api_version(self) -> str:
        return self._api_version

    # CRUD
    def delete(self, url_suffix: str, json: dict = None) -> Response:
        url = f"{self.api_base_url}/api/{self.api_version}/{url_suffix}"
        response = requests.delete(
            url,
            headers={
                "Authorization": self.authentication_token,
            },
            timeout=self.timeout,
            json=json if json is not None else {},
        )
        if response.status_code != HTTPStatus.OK:
            raise ClientException(response=response)

        return response
