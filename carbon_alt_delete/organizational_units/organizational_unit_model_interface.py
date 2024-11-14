from carbon_alt_delete.client.model_interface import ModelInterface
from carbon_alt_delete.organizational_units.schemas.organizational_unit import (
    OrganizationalUnit,
    OrganizationalUnitCreate,
)


class OrganizationalUnitModelInterface(ModelInterface[OrganizationalUnit]):
    def __init__(self, client, module):
        super().__init__(client, module, OrganizationalUnit)

    def fetch_one(self, url: str = None, **kwargs):
        url = (
            f"{self.client.server}/api/{self.module.name}/{self.module.version}/organizational-units/{kwargs.get('id')}"
        )
        super().fetch_one(url, **kwargs)

    def fetch_all(self, url: str = None, **kwargs):
        url = f"{self.client.server}/api/{self.module.name}/{self.module.version}/organizational-units"
        super().fetch_all(url, **kwargs)

    def create(self, url: str = None, **kwargs):
        url = f"{self.client.server}/api/{self.module.name}/{self.module.version}/organizational-units"
        return super().create(
            url,
            **OrganizationalUnitCreate.model_validate(kwargs).model_dump(by_alias=True, mode="json"),
        )

    def update(self, url: str = None, **kwargs):
        url = f"{self.client.server}/api/{self.module.name}/{self.module.version}/organizational-units/{kwargs['id']}"
        return super().update(
            url,
            **OrganizationalUnit.model_validate(kwargs).model_dump(by_alias=True, mode="json"),
        )

    def delete(self, url: str = None, **kwargs):
        url = f"{self.client.server}/api/{self.module.name}/{self.module.version}/organizational-units/{kwargs['id']}"
        return super().delete(url)

    def root_organizational_unit(self) -> OrganizationalUnit:
        return self.one(parent_organizational_unit_id=None)

    def print_tree(self):
        root = self.root_organizational_unit()
        print(f"+ {root.name}")
        for child_lvl2 in self.all(parent_organizational_unit_id=root.id):
            print(f"|--> {child_lvl2.name}")
            for child_lvl3 in self.all(parent_organizational_unit_id=child_lvl2.id):
                print(f"   |--> {child_lvl3.name}")
                for child_lvl4 in self.all(parent_organizational_unit_id=child_lvl3.id):
                    print(f"   |--> {child_lvl4.name}")
