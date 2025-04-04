# Create Custom Emission Factors

!! **Document is work in progress** !!

## Input files

- Excel file with emission factors (based on the template on the support page)

## Steps

1. Create a Folder: Start by creating a non-shared folder with the company name.

    ```shell
    mkdir -p not_shared/company_name
    ```

2. Create an environment file with the necessary credentials.

    ```shell
    touch not_shared/company_name/company_name.env
    ```
   Example with 2 server lines to first test on staging (can be commented during final run)
    ```dotenv
    EMAIL=support+company_name@carbonaltdelete.eu
    PASSWORD=PASSWORD
    SERVER=https://app.carbonaltdelete.eu
    SERVER=https://staging-testing.dev.carbonaltdelete.eu
    ```

3. Copy Necessary Files:
    - Copy the python file named "upload_custom_emission_factors.py" into the folder.
    - Copy the received Excel file next to the upload file.

4. Set Details:
    - Ensure that all details such as the Excel file name, sheet name, and target client company are set correctly.

5. Adapt Header Row Index:
    - Adjust the header row index when reaching the Excel interpreter.

6. Test on Staging Environment:
    - Change the server to the staging environment.
    - Test the setup in the environment file.

7. Run the Script:
    - Execute the script on the staging environment and confirm the outcome.

8. Handle Incorrect Entries:
    - Note that the script only inserts new entries and does not update existing ones.
    - Incorrect emission factors need to be deleted manually or directly via the database.

9. Create Custom Entry:
    - Attempt to create a custom entry on the newly created emission factor to ensure everything is functioning
      correctly.
