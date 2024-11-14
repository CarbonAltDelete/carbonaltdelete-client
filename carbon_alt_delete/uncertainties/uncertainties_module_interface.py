from carbon_alt_delete.client.module_interface import ModuleInterface
from uncertainties.uncertainty_model_interface import UncertaintyModelInterface


class UncertaintiesModuleInterface(ModuleInterface):
    def __init__(self, client):
        super().__init__("uncertainties", "v1")
        self.uncertainties: UncertaintyModelInterface = UncertaintyModelInterface(client=client, module=self)
