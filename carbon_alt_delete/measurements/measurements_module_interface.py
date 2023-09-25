from carbon_alt_delete.client.module_interface import ModuleInterface
from carbon_alt_delete.measurements.measurement_model_interface import MeasurementModelInterface


class MeasurementsModuleInterface(ModuleInterface):
    def __init__(self, client):
        super().__init__("measurements", "v1")
        self.measurements: MeasurementModelInterface = MeasurementModelInterface(
            client=client,
            module=self,
        )
