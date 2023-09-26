from uuid import UUID

from carbon_alt_delete.client.model_interface import ModelInterface
from carbon_alt_delete.measurements.schemas.formula_term import FormulaTerm


class FormulaTermModelInterface(ModelInterface[FormulaTerm]):
    def __init__(self, client, module):
        super().__init__(client, module, FormulaTerm)

    def fetch_all(
        self,
        measurement_id: UUID,
        url: str = None,
        **kwargs,
    ):
        self.module.formula_term_values.fetch_all(measurement_id=measurement_id, url=url, **kwargs)
