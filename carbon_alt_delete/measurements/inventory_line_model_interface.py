from typing import Literal
from uuid import UUID

from carbon_alt_delete.client.model_interface import ModelInterface
from carbon_alt_delete.measurements.schemas.inventory_line import InventoryLine, InventoryLinePatch
from measurements.schemas.measurement import MeasurementCreate


class InventoryLineModelInterface(ModelInterface[InventoryLine]):
    def __init__(self, client, module):
        super().__init__(client, module, InventoryLine)

    def fetch_one(self, url: str | None = None, **kwargs):
        url = f"{self.client.server}/api/{self.module.name}/{self.module.version}/inventory-lines/{kwargs.get('id')}"
        super().fetch_one(url=url, **kwargs)

    def fetch_all(self, url: str | None = None, limit: int = 100, page: int = 1, **kwargs):
        url = f"{self.client.server}/api/{self.module.name}/{self.module.version}/inventory-lines"
        params = {"limit": limit, "page": page}
        if "organizational_unit_id" in kwargs:
            params["organizationalUnitId_equals"] = kwargs.get("organizational_unit_id")
        response = self.client.get(url=url, params=params)

        inventory_lines = [InventoryLine(**inventory_line) for inventory_line in response.json()["inventoryLines"]]
        assert len(inventory_lines) <= limit
        self._upsert_many(response.json().get("inventoryLines", []), key_field="measurement.id")
        return inventory_lines

    def create(self, **kwargs) -> InventoryLine:
        url = f"{self.client.server}/api/{self.module.name}/{self.module.version}/inventory-lines"
        response = self.client.post(
            url=url,
            json=MeasurementCreate(**kwargs).model_dump(by_alias=True, mode="json"),
        )
        inventory_line = InventoryLine(**response.json())
        self._upsert_one(response.json(), key_field="measurement.id")
        return inventory_line

    def update(
        self,
        url: str | None = None,
        method: Literal["PATCH"] = "PATCH",
        measurement_only: bool = False,
        formula_term_values_only: bool = False,
        **kwargs,
    ):
        measurement_id: UUID = kwargs.get("measurement").get("id")
        url = f"{self.client.server}/api/{self.module.name}/{self.module.version}/inventory-lines/{measurement_id}"

        return super().update(
            url,
            method=method,
            **InventoryLinePatch(
                **{"measurement": kwargs.get("measurement")} if measurement_only else {},
                **kwargs.get("formula_term_values") if formula_term_values_only else {},
                custom_fields=kwargs.get("custom_fields"),
            ).model_dump(by_alias=True, mode="json"),
        )
