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

    def _set_all(self, response, key_field: str = "id"):
        self._state.clear()
        self._state.update({r[key_field]: self._member_class(**r) for r in response.json()})

    def _upsert_one(self, response, key_field: str = "id"):
        self._state.update({response.json()[key_field]: self._member_class(**response.json())})

    def _select_one(self, key: UUID) -> T:
        return self._state[key]

    def create(self, url: str, **kwargs) -> T:
        if url is None:
            raise NotImplementedError
        response = self.client.post(
            url,
            json=kwargs,
        )
        if not kwargs.get("skip_state", False):
            self._upsert_one(response, kwargs.get("key_field", "id"))
            return self._select_one(response.json()[kwargs.get("key_field", "id")])
        else:
            return self._member_class(**response.json())

    def all(self, refresh: bool = False, **kwargs) -> list[T]:
        if not self._state or refresh:
            self.fetch_all()
        return list(filter(lambda x: all([getattr(x, k) == v for k, v in kwargs.items()]), self._state.values()))

    def first(self, **kwargs) -> T:
        result = self.all(**kwargs)
        return result[0]

    def last(self, **kwargs) -> T:
        result = self.all(**kwargs)
        return result[0]

    def one(self, **kwargs) -> T:
        result = self.all(**kwargs)
        assert len(result) == 1
        return result[0]
