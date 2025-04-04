from carbon_alt_delete.client.model_interface import ModelInterface
from carbon_alt_delete.documents.schemas.url import Url


class S3UrlModelInterface(ModelInterface[Url]):
    def __init__(self, client, module):
        super().__init__(client, module, Url)

    def pre_signed_write(self, file_name: str, **kwargs):
        url = f"{self.client.server}/api/{self.module.name}/{self.module.version}/pre-signed-write"
        response = self.client.post(
            url,
            json={
                "entityIds": [],
                "emissionFactorId": None,
                "fileName": file_name,
            },
        )
        print()
        return Url(
            **response.json(),
        )
