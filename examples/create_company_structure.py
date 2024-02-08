import os

from dotenv import load_dotenv

from carbon_alt_delete.client.carbon_alt_delete_client import CarbonAltDeleteClient
from carbon_alt_delete.client.connect import connect


def create_company_structure():
    client: CarbonAltDeleteClient
    with connect(
        email=os.getenv("EMAIL"),
        password=os.getenv("PASSWORD"),
        server=os.getenv("SERVER"),
    ) as client:
        # Create Company and switch to it
        company = client.accounts.companies.create(name="My first client company")
        client.switch(company.id)

        user = client.accounts.users.create(
            first_name="John",
            last_name="Doe",
            email=f"testing+{company.id}@carbonaltdelete.eu",
            company_id=company.id,
            return_if_exists=True,
        )
        client.accounts.users.activate(user.id)

        # Build organizational units
        root = client.organizational_units.organizational_units.root_organizational_unit()
        sales = client.organizational_units.organizational_units.create(
            name="Sales",
            parent_organizational_unit_id=root.id,
            position=0,
        )
        belgium = client.organizational_units.organizational_units.create(
            name="Belgium",
            parent_organizational_unit_id=sales.id,
            position=0,
        )
        client.organizational_units.organizational_units.create(
            name="Germany",
            parent_organizational_unit_id=sales.id,
            position=belgium.position + 1,
        )
        client.organizational_units.organizational_units.create(
            name="Marketing",
            parent_organizational_unit_id=root.id,
            position=sales.position + 1,
        )

        print("\nCreated company structure:")
        print(f"Company: {company.name}")

        print("\nOrganizational Units:")
        client.organizational_units.organizational_units.print_tree()

        print("\nUsers:")
        users = client.accounts.users.all(refresh=True, company_id=company.id, is_consultant=False)
        api_key = os.getenv("API_KEY")
        for user in users:
            if api_key:
                redirect_key = client.keys.redirect.create(
                    user_id=user.id,
                    api_key=api_key,
                    secret=os.getenv("SECRET"),
                )
                print(
                    f"\t{user.first_name} {user.last_name} ({user.email}) [{user.status}] "
                    f"-> {os.getenv('FRONTEND', os.getenv('SERVER'))}/redirect?key={redirect_key.redirect_key}",
                )
            else:
                print(f"\t{user.first_name} {user.last_name} ({user.email}) [{user.status}]")

        print("\nReporting Periods:")
        client.reporting_periods.reporting_periods.create(
            short_name="Y-2021",
            start_date="2021-01-01",
            end_date="2021-12-31",
            description="Base year for carbon footprint",
        )
        for reporting_period in client.reporting_periods.reporting_periods.all():
            print(f"\t{reporting_period.short_name} [{reporting_period.start_date} - {reporting_period.end_date}]")

        print("\nActivity Categories:")
        for activity_category in client.activities.activity_categories.all():
            print(f"\t{activity_category.name} [{activity_category.activity_category_type}]")

        print("\nActivity Groups:")
        for activity_group in client.activities.activity_groups.all():
            print(f"\t{activity_group.name}")

        print("\nResults:")
        for result in client.results.dashboard.all(params={"organizationUnitId_eq": root.id}):
            print(f"\t{result.activity_category_id}")


if __name__ == "__main__":
    load_dotenv()
    create_company_structure()
