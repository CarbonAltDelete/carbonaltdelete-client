from uuid import UUID

from carbon_alt_delete.client.model_interface import ModelInterface
from carbon_alt_delete.measurements.schemas.formula_term_value import FormulaTermValue


class FormulaTermValueModelInterface(ModelInterface[FormulaTermValue]):
    def __init__(self, client, module):
        super().__init__(client, module, FormulaTermValue)

    def fetch_all(
        self,
        measurement_id: UUID,
        url: str = None,
        **kwargs,
    ):
        url = f"{self.client.server}/api/v1.0/measurements/{measurement_id}/formula"
        response = self.client.get(url)
        self._set_all(response.json().get("formulaTermValues", []))
        self.module.formula_terms._set_all(response.json().get("formulaTerms", []))

    def update(
        self,
        url: str = None,
        **kwargs,
    ):
        url = (
            f"{self.client.server}/api/v1.0/measurements/{kwargs.get('measurement_id')}"
            f"/formula-term-value/{kwargs.get('id')}"
        )
        return super().update(
            url,
            **FormulaTermValue(**kwargs).model_dump(by_alias=True, mode="json"),
        )
