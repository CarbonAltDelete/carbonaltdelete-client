from uuid import UUID

from carbon_alt_delete.client.model_interface import ModelInterface


class MeasurementInterface(ModelInterface):
    def delete(
        self,
        measurement_id: UUID | str,
    ) -> list[dict]:
        if isinstance(measurement_id, str):
            measurement_id = UUID(hex=measurement_id)
        url_stub = f"measurements/{measurement_id}"

        return self.client.delete(url_stub).json()
