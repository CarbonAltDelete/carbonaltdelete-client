import logging
from http import HTTPStatus
from uuid import UUID

import requests
from jose import jwt
from requests.models import Response

from carbon_alt_delete.accounts.accounts_module_interface import AccountsModuleInterface
from carbon_alt_delete.accounts.schemas.company import Company
from carbon_alt_delete.accounts.schemas.user import User
from carbon_alt_delete.activities.activities_module_interface import ActivitiesModuleInterface
from carbon_alt_delete.client.exceptions import ClientException
from carbon_alt_delete.emission_factors.emission_factors_module_interface import EmissionFactorsModuleInterface
from carbon_alt_delete.keys.keys_module_interface import KeysModuleInterface
from carbon_alt_delete.measurements.measurements_module_interface import MeasurementsModuleInterface
from carbon_alt_delete.organizational_units.organizational_units_module_interface import (
    OrganizationalUnitsModuleInterface,
)
from carbon_alt_delete.reporting_periods.reporting_periods_module_interface import ReportingPeriodsModuleInterface
from carbon_alt_delete.reports.reports_module_interface import ReportsModuleInterface
from carbon_alt_delete.results.results_module_interface import ResultsModuleInterface

logger = logging.getLogger(__name__)


class CarbonAltDeleteClient:
    def __init__(
        self,
        server: str | None = None,
    ):
        self._server = server

        self.accounts: AccountsModuleInterface = AccountsModuleInterface(self)
        self.activities: ActivitiesModuleInterface = ActivitiesModuleInterface(self)
        self.emission_factors: EmissionFactorsModuleInterface = EmissionFactorsModuleInterface(self)
        self.keys: KeysModuleInterface = KeysModuleInterface(self)
        self.measurements: MeasurementsModuleInterface = MeasurementsModuleInterface(self)
        self.organizational_units: OrganizationalUnitsModuleInterface = OrganizationalUnitsModuleInterface(self)
        self.reporting_periods: ReportingPeriodsModuleInterface = ReportingPeriodsModuleInterface(self)
        self.reports: ReportsModuleInterface = ReportsModuleInterface(self)
        self.results: ResultsModuleInterface = ResultsModuleInterface(self)

        # config
        self.timeout = 15000

        # token info

        self._authentication_token: str | None = None
        self._token_type: str | None = None
        self._user: User | None = None
        self._company: Company | None = None
        self._client_company: Company | None = None

    @property
    def server(self) -> str:
        return self._server

    def authenticate_email_password(self, email: str, password: str):
        url = f"{self.server}/api/auth/token"
        response = requests.post(
            url,
            data={
                "username": email,
                "password": password,
            },
            timeout=self.timeout,
        )
        if response.status_code != HTTPStatus.OK:
            self._authentication_token = None
            raise ClientException(
                response=response,
                method="POST",
            )

        self._authentication_token = response.json().get("access_token", None)
        self._token_type = response.json().get("token_type", None)

        self._get_token_info()
        self.print_authentication_status()

    def authenticate_api_key_secret(self, api_key: str, secret: str):
        url = f"{self.server}/api/keys/v1/api/auth"
        response = requests.post(
            url,
            json={
                "apiKey": api_key,
                "secret": secret,
            },
            timeout=self.timeout,
        )
        if response.status_code != HTTPStatus.OK:
            self._authentication_token = None
            raise ClientException(
                response=response,
                method="POST",
            )

        self._authentication_token = response.json().get("accessToken", None)
        self._token_type = response.json().get("tokenType", None)

        self._get_token_info()
        self.print_authentication_status()

    def disconnect(self):
        self._authentication_token = None

    def switch(self, company_id: UUID):
        url = f"{self.server}/api/auth/token/switch"
        response = requests.post(
            url,
            headers={
                "Authorization": self.authentication_token,
            },
            json={
                "companyId": str(company_id),
            },
            timeout=self.timeout,
        )
        if response.status_code != HTTPStatus.OK:
            self._authentication_token = None
            raise ClientException(
                response=response,
                method="POST",
            )

        self._authentication_token = response.json().get("access_token", None)
        self._token_type = response.json().get("token_type", None)

        self._get_token_info()
        self.print_authentication_status()

    @property
    def authentication_token(self) -> str | None:
        if self._authentication_token is not None:
            return f"{self._token_type} {self._authentication_token}"
        else:
            return None

    # CRUD
    def post(self, url: str, json: dict = None) -> Response:
        logger.debug(f"POST {url}")
        response = requests.post(
            url,
            headers={
                "Authorization": self.authentication_token,
            },
            timeout=self.timeout,
            json=json if json is not None else {},
        )
        if response.status_code != HTTPStatus.OK:
            raise ClientException(
                response=response,
                method="POST",
            )

        return response

    def get(self, url: str, params: dict = None) -> Response:
        logger.debug(f"GET {url}")
        response = requests.get(
            url,
            params=params if params is not None else {},
            headers={
                "Authorization": self.authentication_token,
            },
            timeout=self.timeout,
        )
        if response.status_code != HTTPStatus.OK:
            raise ClientException(response=response)

        return response

    def put(
        self,
        url: str,
        json: dict = None,
    ) -> Response:
        logger.debug(f"PUT {url}")
        response = requests.put(
            url,
            headers={
                "Authorization": self.authentication_token,
            },
            json=json if json is not None else {},
            timeout=self.timeout,
        )
        if response.status_code != HTTPStatus.OK:
            raise ClientException(response=response)

        return response

    def delete(self, url: str, json: dict = None) -> Response:
        logger.debug(f"DELETE {url}")
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

    @property
    def user(self) -> User:
        if self._user:
            return self._user
        raise Exception("User not set")

    @property
    def company(self) -> Company:
        if self._company:
            return self._company
        raise Exception("Company not set")

    @property
    def client_company(self) -> Company | None:
        return self._client_company

    def print_authentication_status(self):
        print("=" * 80)
        print("Carbon+Alt+Delete Client")
        print("-" * 80)
        print(f"Server:     {self.server}")
        print(f"Status:     {'Connected' if self.authentication_token else 'Missing Token'}")
        print("-" * 80)
        print(f"User:       {self.user.first_name} {self.user.last_name} <{self.user.email}>")
        print(f"Company:    {self.company.name}")
        print(f"Client:     {self.client_company.name if self.client_company else '-'}")
        print("=" * 80)

    def _get_token_info(self):
        token_data = jwt.get_unverified_claims(self._authentication_token)
        user_id = token_data.get("userId", None)
        company_id = token_data.get("com", None)

        self._user = self.accounts.users.one(id=UUID(hex=user_id))
        self._company = self.accounts.companies.one(id=self._user.company_id)
        if company_id:
            self._client_company = self.accounts.companies.one(id=UUID(hex=company_id))
