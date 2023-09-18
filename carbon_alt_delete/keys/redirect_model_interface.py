from carbon_alt_delete.client.model_interface import ModelInterface
from carbon_alt_delete.keys.schemas.redirect_key import RedirectKey, RedirectKeyCreate


class RedirectModelInterface(ModelInterface[RedirectKey]):
    def __init__(self, client, module):
        super().__init__(client, module, RedirectKey)

    def create(self, url: str = None, **kwargs):
        url = f"{self.client.server}/api/{self.module.name}/{self.module.version}/redirect"
        return super().create(
            url,
            **RedirectKeyCreate.model_validate(kwargs).model_dump(by_alias=True, mode="json"),
            skip_state=True,
        )
