from uuid import UUID

from carbon_alt_delete.accounts.schemas.user import User, UserCreate
from carbon_alt_delete.client.exceptions import ClientException
from carbon_alt_delete.client.model_interface import ModelInterface


class UserModelInterface(ModelInterface):
    def __init__(self, client, module):
        super().__init__(client, module, User)

    def fetch_all(self, url: str = None):
        url = f"{self.client.server}/api/{self.module.name}/{self.module.version}/users"
        super().fetch_all(url)

    def fetch_one(
        self,
        id: UUID,
        url: str = None,
        **kwargs,
    ):
        url = f"{self.client.server}/api/{self.module.name}/{self.module.version}/users/{id}"
        super().fetch_one(url)

    def create(self, url: str = None, **kwargs):
        url = f"{self.client.server}/api/{self.module.name}/{self.module.version}/users"
        try:
            return super().create(
                url,
                **UserCreate(**kwargs).model_dump(by_alias=True, mode="json"),
            )
        except ClientException as exc:
            if kwargs.get("return_if_exists", False) and exc.response.status_code == 409:
                return self.one(email=kwargs["email"])
            else:
                raise exc

    def activate(self, user_id: UUID):
        url = f"{self.client.server}/api/{self.module.name}/{self.module.version}/users/{user_id}/activate"
        self.client.put(url)
