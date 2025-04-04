from carbon_alt_delete.client.module_interface import ModuleInterface
from carbon_alt_delete.emission_factors.dataset_model_interface import (
    DatasetModelInterface,
)
from carbon_alt_delete.emission_factors.dataset_version_model_interface import (
    DatasetVersionModelInterface,
)
from carbon_alt_delete.emission_factors.emission_factor_custom_model_interface import (
    EmissionFactorCustomModelInterface,
)
from carbon_alt_delete.emission_factors.emission_factor_model_interface import (
    EmissionFactorModelInterface,
)
from carbon_alt_delete.emission_factors.emission_factor_value_model_interface import (
    EmissionFactorValueModelInterface,
)
from carbon_alt_delete.emission_factors.value_mapping_model_interface import (
    ValueMappingModelInterface,
)


class EmissionFactorsModuleInterface(ModuleInterface):
    def __init__(self, client):
        super().__init__("emission-factors", "v1")

        self.datasets: DatasetModelInterface = DatasetModelInterface(
            client=client,
            module=self,
        )
        self.dataset_versions: DatasetVersionModelInterface = (
            DatasetVersionModelInterface(
                client=client,
                module=self,
            )
        )

        self.emission_factors: EmissionFactorModelInterface = (
            EmissionFactorModelInterface(
                client=client,
                module=self,
            )
        )

        self.emission_factors_custom: EmissionFactorCustomModelInterface = (
            EmissionFactorCustomModelInterface(
                client=client,
                module=self,
            )
        )

        self.emission_factor_values: EmissionFactorValueModelInterface = (
            EmissionFactorValueModelInterface(
                client=client,
                module=self,
            )
        )

        self.value_mappings: ValueMappingModelInterface = ValueMappingModelInterface(
            client=client,
            module=self,
        )
