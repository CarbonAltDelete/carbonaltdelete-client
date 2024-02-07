from typing import TYPE_CHECKING, Generic, TypeVar
from uuid import UUID

from pydantic import BaseModel

from carbon_alt_delete.client.module_interface import ModuleInterface
from carbon_alt_delete.client.schemas.delete_message import DeleteMessage

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

    def fetch_all(self, url: str = None, params={}, **kwargs):
        if url is None:
            raise NotImplementedError
        response = self.client.get(url, params=params, **kwargs)
        self._set_all(response.json())

    def fetch_one(self, url: str = None, **kwargs):
        if url is None:
            raise NotImplementedError
        response = self.client.get(url, **kwargs)
        self._upsert_one(response.json())

    def _set_all(self, response: list[dict], key_field: str = "id"):
        self._state.clear()
        self._state.update({r.get(key_field): self._member_class(**r) for r in response})

    def _upsert_one(self, response: dict, key_field: str = "id"):
        self._state.update({response.get(key_field): self._member_class(**response)})

    def _select_one(self, key: UUID) -> T:
        return self._state[key]

    def _delete_one(self, key: UUID):
        del self._state[key]

    def create(self, url: str, **kwargs) -> T:
        if url is None:
            raise NotImplementedError
        response = self.client.post(
            url,
            json=kwargs,
        )
        if not kwargs.get("skip_state", False):
            self._upsert_one(response.json(), kwargs.get("key_field", "id"))
            return self._select_one(response.json()[kwargs.get("key_field", "id")])
        else:
            return self._member_class(**response.json())

    def all(self, refresh: bool = False, **kwargs) -> list[T]:
        if not self._state or refresh:
            self.fetch_all(**kwargs)
        return list(
            filter(
                lambda x: all([getattr(x, k) == v for k, v in kwargs.items() if hasattr(x, k)]),
                self._state.values(),
            ),
        )

    def first(self, **kwargs) -> T | None:
        try:
            result = self.all(**kwargs)
            return result[0]
        except IndexError:
            return None

    def last(self, **kwargs) -> T:
        result = self.all(**kwargs)
        return result[0]

    def one(self, key_field: str = "id", **kwargs) -> T:
        key = kwargs.get(key_field)
        if key and self._state.get(key) is None:
            self.fetch_one(**kwargs)
            kwargs["refresh"] = False

        result = self.all(**kwargs)
        assert len(result) == 1, f"Expected 1 result, got {len(result)}"
        return result[0]

    def update(self, url: str = None, **kwargs) -> T:
        if url is None:
            raise NotImplementedError
        response = self.client.put(
            url,
            json=kwargs,
        )
        self._upsert_one(response.json(), kwargs.get("key_field", "id"))
        return self._state[response.json().get(kwargs.get("key_field", "id"))]

    def delete(self, url: str, **kwargs) -> DeleteMessage:
        if url is None:
            raise NotImplementedError
        response = self.client.delete(
            url,
            json=kwargs,
        )
        delete_message = DeleteMessage(**response.json())
        self._delete_one(response.json().get(kwargs.get("key_field", "id")))
        return delete_message
