from carbon_alt_delete.client.module_interface import ModuleInterface
from carbon_alt_delete.keys.redirect_model_interface import RedirectModelInterface


class KeysModuleInterface(ModuleInterface):
    def __init__(self, client):
        super().__init__("keys", "v1")
        self.redirect: RedirectModelInterface = RedirectModelInterface(client=client, module=self)
