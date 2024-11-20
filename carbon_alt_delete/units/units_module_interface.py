from carbon_alt_delete.client.module_interface import ModuleInterface
from units.unit_class_model_interface import UnitClassModelInterface
from units.unit_model_interface import UnitModelInterface


class UnitsModuleInterface(ModuleInterface):
    def __init__(self, client):
        super().__init__("units", "v1")
        self.units: UnitModelInterface = UnitModelInterface(client=client, module=self)
        self.unit_classes: UnitClassModelInterface = UnitClassModelInterface(client=client, module=self)
