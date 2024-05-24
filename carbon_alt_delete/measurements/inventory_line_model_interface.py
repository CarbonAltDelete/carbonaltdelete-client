from typing import Literal
from uuid import UUID

from carbon_alt_delete.client.model_interface import ModelInterface
from carbon_alt_delete.measurements.schemas.inventory_line import InventoryLine, InventoryLinePatch


class InventoryLineModelInterface(ModelInterface[InventoryLine]):
    def __init__(self, client, module):
        super().__init__(client, module, InventoryLine)

    def fetch_one(self, url: str | None = None, **kwargs):
        url = f"{self.client.server}/api/{self.module.name}/{self.module.version}/inventory-lines/{kwargs.get('id')}"
        super().fetch_one(url=url, **kwargs)

    def update(
        self,
        url: str | None = None,
        method: Literal["PATCH"] = "PATCH",
        **kwargs,
    ):
        measurement_id: UUID = kwargs.get("measurement").get("id")
        url = f"{self.client.server}/api/{self.module.name}/{self.module.version}/inventory-lines/{measurement_id}"

        return super().update(
            url,
            method=method,
            **InventoryLinePatch(
                **{"measurement": kwargs.get("measurement")},
                **kwargs.get("formula_term_values"),
            ).model_dump(by_alias=True, mode="json"),
        )
