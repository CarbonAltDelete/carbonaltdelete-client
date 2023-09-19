from carbon_alt_delete.activities.activity_category_model_interface import ActivityCategoryModelInterface
from carbon_alt_delete.activities.activity_group_model_interface import ActivityGroupModelInterface
from carbon_alt_delete.client.module_interface import ModuleInterface


class ActivitiesModuleInterface(ModuleInterface):
    def __init__(self, client):
        super().__init__("activities", "v1")
        self.activity_categories: ActivityCategoryModelInterface = ActivityCategoryModelInterface(
            client=client,
            module=self,
        )
        self.activity_groups: ActivityGroupModelInterface = ActivityGroupModelInterface(client=client, module=self)
