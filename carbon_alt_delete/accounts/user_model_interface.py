from carbon_alt_delete.accounts.schemas.user import User
from carbon_alt_delete.client.model_interface import ModelInterface


class UserModelInterface(ModelInterface):
    def __init__(self, client, module):
        super().__init__(client, module, User)

    def fetch_all(self, url: str = None):
        url = f"{self.client.server}/api/{self.module.name}/{self.module.version}/users"
        super().fetch_all(url)
