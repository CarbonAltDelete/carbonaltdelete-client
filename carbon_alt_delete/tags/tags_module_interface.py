from carbon_alt_delete.client.module_interface import ModuleInterface
from carbon_alt_delete.tags.field_model_interface import FieldModelInterface
from carbon_alt_delete.tags.option_model_interface import OptionModelInterface


class TagsModuleInterface(ModuleInterface):
    def __init__(self, client):
        super().__init__("tags", "v1")
        self.options: OptionModelInterface = OptionModelInterface(
            client=client,
            module=self,
        )

        self.fields: FieldModelInterface = FieldModelInterface(
            client=client,
            module=self,
        )
