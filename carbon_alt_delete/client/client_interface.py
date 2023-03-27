import abc
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from carbon_alt_delete.client.carbon_alt_delete_client import CarbonAltDeleteClient


class ClientInterface(abc.ABC):
    def __init__(self, client: "CarbonAltDeleteClient"):
        self._client = client

    @property
    def client(self) -> "CarbonAltDeleteClient":
        return self._client

    def list(
        self,
    ) -> list[dict] | type[NotImplementedError]:
        return NotImplementedError
