from carbon_alt_delete.client.module_interface import ModuleInterface
from carbon_alt_delete.organizational_units.organizational_unit_model_interface import OrganizationalUnitModelInterface


class OrganizationalUnitsModuleInterface(ModuleInterface):
    def __init__(self, client):
        super().__init__("organizational-units", "v1")
        self.organizational_units: OrganizationalUnitModelInterface = OrganizationalUnitModelInterface(
            client=client,
            module=self,
        )
