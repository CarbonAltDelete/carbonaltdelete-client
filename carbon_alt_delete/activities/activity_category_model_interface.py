from carbon_alt_delete.activities.schemas.activity_category import ActivityCategory, ActivityCategoryCreate
from carbon_alt_delete.client.model_interface import ModelInterface


class ActivityCategoryModelInterface(ModelInterface[ActivityCategory]):
    def __init__(self, client, module):
        super().__init__(client, module, ActivityCategory)

    def fetch_all(self, url: str = None, **kwargs):
        url = f"{self.client.server}/api/{self.module.name}/{self.module.version}/activity-categories"
        super().fetch_all(url, **kwargs)

    def create(self, url: str = None, **kwargs):
        url = f"{self.client.server}/api/{self.module.name}/{self.module.version}/activity-categories"
        return super().create(
            url,
            **ActivityCategoryCreate.model_validate(kwargs).model_dump(by_alias=True, mode="json"),
        )
