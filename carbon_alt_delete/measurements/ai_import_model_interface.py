from uuid import UUID

from pydantic import BaseModel, NonNegativeFloat

from carbon_alt_delete.client.model_interface import ModelInterface


class AiImport(BaseModel):
    id: UUID


class AiImportStatus(BaseModel):
    id: UUID
    progress: NonNegativeFloat
    status: str


class AiImportModelInterface(ModelInterface[AiImport]):
    def __init__(self, client, module):
        super().__init__(client, module, AiImport)

    def status(
        self,
        id: UUID,
        url: str | None = None,
        **kwargs,
    ):
        url = f"{self.client.server}/api/{self.module.name}/{self.module.version}/measurement-ai-imports/{id}/status"
        print(url)
        response = self.client.get(url)
        if response.status_code != 200:
            raise ValueError(response.text)
        return AiImportStatus(**response.json())

    def create(self, url: str | None = None, document_ids: list[UUID] = [], **kwargs):
        url = f"{self.client.server}/api/{self.module.name}/{self.module.version}/measurement-ai-imports"
        if not document_ids:
            raise ValueError("document_ids is required")
        return super().create(
            url,
            documentIds=[str(i) for i in document_ids],
            **kwargs,
        )
