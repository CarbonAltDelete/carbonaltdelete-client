import os

from dotenv import load_dotenv

from carbon_alt_delete.client.carbon_alt_delete_client import CarbonAltDeleteClient
from carbon_alt_delete.client.connect import connect


def fetch_activities_tree():
    client: CarbonAltDeleteClient
    with connect(
        email=os.getenv("EMAIL"),
        password=os.getenv("PASSWORD"),
        server=os.getenv("SERVER"),
    ) as client:

        activity_groups = client.activities.activity_groups.all()
        activity_categories = client.activities.activity_categories.all()

        activity_categories_by_group = {
            ag.id: [ac for ac in activity_categories if ac.activity_group_id == ag.id] for ag in activity_groups
        }

        print("\nActivity Groups:")
        for activity_group in activity_groups:
            print(f"{activity_group.name} ({activity_group.id})")
            for activity_category in activity_categories_by_group[activity_group.id]:
                print(
                    f"\t[{'x'if activity_category.is_used else ' '}] ({activity_category.position:2d})"
                    f" {activity_category.name} ({activity_category.id})",
                )


if __name__ == "__main__":
    load_dotenv()
    fetch_activities_tree()
