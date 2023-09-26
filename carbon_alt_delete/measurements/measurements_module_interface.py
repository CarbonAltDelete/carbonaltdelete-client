from carbon_alt_delete.client.module_interface import ModuleInterface
from carbon_alt_delete.measurements.formula_term_model_interface import FormulaTermModelInterface
from carbon_alt_delete.measurements.formula_term_value_model_interface import FormulaTermValueModelInterface
from carbon_alt_delete.measurements.measurement_model_interface import MeasurementModelInterface


class MeasurementsModuleInterface(ModuleInterface):
    def __init__(self, client):
        super().__init__("measurements", "v1")
        self.measurements: MeasurementModelInterface = MeasurementModelInterface(
            client=client,
            module=self,
        )

        self.formula_terms: FormulaTermModelInterface = FormulaTermModelInterface(
            client=client,
            module=self,
        )

        self.formula_term_values: FormulaTermValueModelInterface = FormulaTermValueModelInterface(
            client=client,
            module=self,
        )
