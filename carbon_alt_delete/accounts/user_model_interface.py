import logging


from carbon_alt_delete.accounts.schemas.user import User
from carbon_alt_delete.client.model_interface import ModelInterface

logger = logging.getLogger(__name__)


class UserModelInterface(ModelInterface):
    def __init__(self, client, module):
        super().__init__(client, module)
        self._schema = User
        self._all: list[User] = []

    def fetch_all(
        self,
    ) -> list[User]:
        url = f"{self.client.server}/api/{self.module.name}/{self.module.version}/users"
        response = self.client.get(url)
        self._all = [User(**r) for r in response.json()]
        return self._all

    def all(self, **kwargs) -> list[User]:
        if not self._all:
            self.fetch_all()
        return list(filter(lambda x: all([getattr(x, k) == v for k, v in kwargs.items()]), self._all))

    def one(self, **kwargs) -> User:
        result = self.all(**kwargs)
        assert len(result) == 1
        return result[0]
