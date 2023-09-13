from carbon_alt_delete.accounts.schemas.company import Company
from carbon_alt_delete.client.model_interface import ModelInterface


class CompanyModelInterface(ModelInterface):
    def __init__(self, client, module):
        super().__init__(client, module)
        self._schema = Company
        self._all: list[Company] = []

    def fetch_all(
        self,
    ) -> list[Company]:
        url = f"{self.client.server}/api/{self.module.name}/{self.module.version}/companies"
        response = self.client.get(url)
        self._all = [Company(**r) for r in response.json()]
        return self._all

    def all(self, **kwargs) -> list[Company]:
        if not self._all:
            self.fetch_all()
        return list(filter(lambda x: all([getattr(x, k) == v for k, v in kwargs.items()]), self._all))

    def one(self, **kwargs) -> Company:
        result = self.all(**kwargs)
        assert len(result) == 1
        return result[0]
