from typing import TYPE_CHECKING, Generic, TypeVar
from uuid import UUID

from pydantic import BaseModel

from carbon_alt_delete.client.module_interface import ModuleInterface

if TYPE_CHECKING:
    from carbon_alt_delete.client.carbon_alt_delete_client import CarbonAltDeleteClient

T = TypeVar("T", bound=BaseModel)


class ModelInterface(Generic[T]):
    def __init__(self, client: "CarbonAltDeleteClient", module: ModuleInterface, member_class: type[T]):
        self._client = client
        self._module = module
        self._state: dict[UUID, T] = {}
        self._member_class: type[T] = member_class

    @property
    def client(self) -> "CarbonAltDeleteClient":
        return self._client

    @property
    def module(self) -> ModuleInterface:
        return self._module

    def fetch_all(self, url: str = None):
        if url is None:
            raise NotImplementedError
        response = self.client.get(url)
        self._set_all(response)

    def _set_all(self, response, key: str = "id"):
        self._state.clear()
        self._state.update({UUID(hex=r[key]): self._member_class(**r) for r in response.json()})

    def all(self, **kwargs) -> list[T]:
        if not self._state:
            self.fetch_all()
        return list(filter(lambda x: all([getattr(x, k) == v for k, v in kwargs.items()]), self._state.values()))

    def one(self, **kwargs) -> T:
        result = self.all(**kwargs)
        assert len(result) == 1
        return result[0]
