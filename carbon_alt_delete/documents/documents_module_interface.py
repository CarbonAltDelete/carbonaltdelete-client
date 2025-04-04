from carbon_alt_delete.client.module_interface import ModuleInterface
from carbon_alt_delete.documents.s3_model_interface import S3UrlModelInterface


class DocumentsModuleInterface(ModuleInterface):
    def __init__(self, client):
        super().__init__("documents", "v1")

        self.documents: S3UrlModelInterface = S3UrlModelInterface(
            client=client,
            module=self,
        )
