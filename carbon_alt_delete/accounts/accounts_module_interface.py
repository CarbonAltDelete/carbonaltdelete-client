from carbon_alt_delete.accounts.company_model_interface import CompanyModelInterface
from carbon_alt_delete.accounts.user_model_interface import UserModelInterface
from carbon_alt_delete.client.module_interface import ModuleInterface


class AccountsModuleInterface(ModuleInterface):
    def __init__(self, client):
        super().__init__("accounts", "v1")
        self.companies: CompanyModelInterface = CompanyModelInterface(client=client, module=self)
        self.users: UserModelInterface = UserModelInterface(client=client, module=self)
