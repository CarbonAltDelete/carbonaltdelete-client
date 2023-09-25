from carbon_alt_delete.client.model_interface import ModelInterface
from carbon_alt_delete.measurements.schemas.measurement import Measurement, MeasurementCreate


class MeasurementModelInterface(ModelInterface[Measurement]):
    def __init__(self, client, module):
        super().__init__(client, module, Measurement)

    def create_entry(self, measurement_create: MeasurementCreate) -> Measurement:
        # create measurement
        url = f"{self.client.server}/api/v1.0/measurements/v2"
        measurement = super().create(
            url,
            **measurement_create.model_dump(by_alias=True, mode="json"),
        )

        # update formula term value
        self.client.measurements.formula_term_values.one(measurement_ids=[measurement.id], name="consumption")

        # refresh measurement
        self.one(id=measurement.id, refresh=True)

        return measurement
