import abc
from typing import TYPE_CHECKING

from pydantic import BaseModel

from carbon_alt_delete.client.module_interface import ModuleInterface

if TYPE_CHECKING:
    from carbon_alt_delete.client.carbon_alt_delete_client import CarbonAltDeleteClient


class ModelInterface(abc.ABC):
    def __init__(self, client: "CarbonAltDeleteClient", module: ModuleInterface):
        self._client = client
        self._module = module
        self._schema = None

    @property
    def schema(self) -> type[BaseModel]:
        if self._schema:
            return self._schema
        raise NotImplementedError

    @property
    def client(self) -> "CarbonAltDeleteClient":
        return self._client

    @property
    def module(self) -> ModuleInterface:
        return self._module

    def list(
        self,
    ) -> list[dict]:
        raise NotImplementedError
