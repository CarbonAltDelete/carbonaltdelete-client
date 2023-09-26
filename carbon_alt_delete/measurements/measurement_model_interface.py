from carbon_alt_delete.client.model_interface import ModelInterface
from carbon_alt_delete.measurements.schemas.measurement import Measurement, MeasurementCreate


class MeasurementModelInterface(ModelInterface[Measurement]):
    def __init__(self, client, module):
        super().__init__(client, module, Measurement)

    def fetch_one(self, url: str = None, **kwargs):
        url = f"{self.client.server}/api/v1.0/measurements/v2/{kwargs.get('id')}"
        super().fetch_one(url=url, **kwargs)

    def create_entry(self, measurement_create: MeasurementCreate) -> Measurement:
        # create measurement
        url = f"{self.client.server}/api/v1.0/measurements/v2"
        measurement = super().create(
            url,
            **measurement_create.model_dump(by_alias=True, mode="json"),
        )

        # update formula term value
        formula_term = self.client.measurements.formula_terms.one(
            name="consumption",
            measurement_id=measurement.id,
            refresh=True,
        )
        formula_term_value = self.client.measurements.formula_term_values.one(formula_term_id=formula_term.id)

        formula_term_value.value = measurement_create.consumption
        formula_term_value = self.client.measurements.formula_term_values.update(
            **formula_term_value.model_dump(),
        )

        # refresh measurement
        measurement = self.one(id=measurement.id, refresh=True)

        return measurement
