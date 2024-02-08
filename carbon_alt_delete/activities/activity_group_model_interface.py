from carbon_alt_delete.activities.schemas.activity_group import ActivityGroup, ActivityGroupCreate
from carbon_alt_delete.client.model_interface import ModelInterface


class ActivityGroupModelInterface(ModelInterface[ActivityGroup]):
    def __init__(self, client, module):
        super().__init__(client, module, ActivityGroup)

    def fetch_all(self, url: str = None, **kwargs):
        url = f"{self.client.server}/api/{self.module.name}/{self.module.version}/activity-groups"
        super().fetch_all(url, **kwargs)

    def create(self, url: str = None, **kwargs):
        url = f"{self.client.server}/api/{self.module.name}/{self.module.version}/activity-groups"
        return super().create(
            url,
            **ActivityGroupCreate.model_validate(kwargs).model_dump(by_alias=True, mode="json"),
        )
