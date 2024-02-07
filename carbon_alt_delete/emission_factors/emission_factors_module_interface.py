from carbon_alt_delete.client.module_interface import ModuleInterface
from carbon_alt_delete.emission_factors.emission_factor_model_interface import EmissionFactorModelInterface


class EmissionFactorsModuleInterface(ModuleInterface):
    def __init__(self, client):
        super().__init__("emission-factors", "v1")

        self.emission_factors: EmissionFactorModelInterface = EmissionFactorModelInterface(
            client=client,
            module=self,
        )
