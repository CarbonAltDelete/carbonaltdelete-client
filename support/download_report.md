# Download Inventory Report in XLSX Format

## Documentation

Swagger Online Docs: https://cad-backend-production.herokuapp.com/api/docs

Python Client:  https://github.com/CarbonAltDelete/carbonaltdelete-client

## Flow of endpoints

- The flow below is also implemented simplified in the following example
  file: https://github.com/CarbonAltDelete/carbonaltdelete-client/blob/main/examples/download_inventory_excel.py

1. Authenticate with API key/secret or email/password

- With API
  key/secret: https://cad-backend-production.herokuapp.com/api/docs#/keys/post_authenticate_api_key_keys_v1_api_auth_post
- With email(username)
  /password: https://cad-backend-production.herokuapp.com/api/docs#/authorization/post_login_for_access_token_auth_token_post

- IMPORTANT: In both cases the user linked to the credentials needs to have expert access to the company you want to
  download the report for. This can be configured once by you Admin user via the frontend once. If a new company is
  added, the admin again needs to grant expert rights to the user linked to the credentials.

- The response contains a JWT token which needs to be used for all subsequent requests. The token is valid for 90
  minutes. The token contains the information about the addressed company. If you want to switch to another company, you
  need to follow the next step, otherwise continue with the init of the report generation.

2. Switch to relevant company (optional last login company is default)

- Get list of companies (find id based on name of
  company): https://cad-backend-production.herokuapp.com/api/docs#/accounts/get_companies_accounts_v1_companies_get
- Switch to the
  company: https://cad-backend-production.herokuapp.com/api/docs#/authorization/post_company_switch_auth_token_switch_post
- IMPORTANT: This endpoint provides a new JWT, containing the company switched to, that needs to be used in the
  following requests instead.

3. Initiate report generation

- To initiate a report the following endpoint is
  used: https://cad-backend-production.herokuapp.com/api/docs#/reports/post_report_reports_v1_reports_post
- The required reporting period can be extracted from here (NOTE: no swagger link (to be added soon), but actual GET
  endpoint):
  https://cad-backend-production.herokuapp.com/api/v1.0/reporting-periods
- The required organizational unit can be extracted
  from: https://cad-backend-production.herokuapp.com/api/docs#/organizational-units/get_organizational_units_organizational_units_v1_organizational_units_get

- In the current implementation a process is started to generate all available report types at once to ensure data
  consistency. The downside is that it take about a 1 minute (depending on the company data volume) before being able to
  download the report in the desired template and file format.
- The response provides the report id which is used in the next step.

4. Check status of report generation

- Following up on the status of the report can be done
  here: https://cad-backend-production.herokuapp.com/api/docs#/reports/get_report_reports_v1_reports__report_id__get
- The report is ready to download once the `report_file_status` is `DONE`

5. Obtain pre-signed URL for report download

- The pre-signed URL is obtained using the following
  endpoint: https://cad-backend-production.herokuapp.com/api/docs#/reports/get_report_presigned_url_reports_v1_reports__report_id__presigned_url_get
- The report type for the inventory is called `DATA_DUMP` and the available file format is `XLSX`

6. Download report from AWS S3 File storage

- The pre-signed URL is valid for 5 minutes and can be used to download the report. The file is downloaded to the local
  machine and can be opened with Excel.
