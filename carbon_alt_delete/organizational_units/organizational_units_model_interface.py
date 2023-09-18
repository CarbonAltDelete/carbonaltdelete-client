from carbon_alt_delete.client.model_interface import ModelInterface
from carbon_alt_delete.organizational_units.schemas.organizational_unit import OrganizationalUnit


class OrganizationalUnitModelInterface(ModelInterface[OrganizationalUnit]):
    def __init__(self, client, module):
        super().__init__(client, module, OrganizationalUnit)

    def fetch_all(self, url: str = None):
        url = f"{self.client.server}/api/{self.module.name}/{self.module.version}/organizational-units"
        super().fetch_all(url)

    def root_organizational_unit(self) -> OrganizationalUnit:
        return self.one(parent_organizational_unit_id=None)
