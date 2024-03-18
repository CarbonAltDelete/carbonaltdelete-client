import os

import pandas as pd
from dotenv import load_dotenv

from carbon_alt_delete.client.carbon_alt_delete_client import CarbonAltDeleteClient
from carbon_alt_delete.client.connect import connect
from carbon_alt_delete.emission_factors.enums.dataset_type import DatasetType
from carbon_alt_delete.emission_factors.enums.emission_factor_value_stage import EmissionFactorValueStage
from carbon_alt_delete.emission_factors.enums.emission_factor_value_stage_detail import EmissionFactorValueStageDetail
from carbon_alt_delete.emission_factors.enums.reporting_split import ReportingSplit
from carbon_alt_delete.measurements.enums.emission_calculation_type import EmissionCalculationType


def upload_custom_emission_factors(
        file_path: str,
        sheet_name: str,
):
    client: CarbonAltDeleteClient
    with connect(
            email=os.getenv("EMAIL"),
            password=os.getenv("PASSWORD"),
            server=os.getenv("SERVER"),
    ) as client:

        dataset = client.emission_factors.datasets.one(
            is_integrated=False,
            is_shared=True,
            dataset_type=DatasetType.CUSTOM,
            company_id=client.company.id,
        )
        print("Dataset", dataset)

        df = pd.read_excel(file_path, sheet_name=sheet_name)
        print(df.head())

        for i, row in df.iterrows():
            print(i, row)
            # Post create the emission factors
            # {datasetId: "4b342e2c-15a1-4b02-8771-3ab1b3bbc926", unit: "", attribute: "", keyword: "",…}

            # Single stage emission factor
            if pd.isna(row["Combustion EF (kgCO2e/unit)"]):
                continue
                emission_factor_custom = client.emission_factors.emission_factors_custom.create(
                    dataset_id=str(dataset.id),
                    unit=row["Unit"],
                    attribute=row["Detail"],
                    keyword=row["Keyword"],
                    description=str(row["Description"]),
                    reporting_split=ReportingSplit.DEFAULT,
                    stage_detail=EmissionFactorValueStageDetail.NO_DETAIL,
                    emission_calculation_type=EmissionCalculationType.DEFAULT,
                    stage=EmissionFactorValueStage.PRINCIPAL,
                )
                print("Emission factor CUSTOM\n", emission_factor_custom)

                # Get latest emission factor value
                emission_factor_value = client.emission_factors.emission_factor_values.latest(
                    emission_factor_id=emission_factor_custom.id,
                )
                print(emission_factor_value)
                emission_factor_value.greenhouse_gases.CO2EQ.factor = float(row["Total EF (kgCO2e/unit)"])
                client.emission_factors.emission_factor_values.update(
                    **emission_factor_value.model_dump(mode="json"),
                )

            # Multi-stage emission factor
            else:
                emission_factor_custom = client.emission_factors.emission_factors_custom.create(
                    dataset_id=str(dataset.id),
                    unit=row["Unit"],
                    attribute=row["Detail"],
                    keyword=row["Keyword"],
                    description=str(row["Description"]),
                    reporting_split=ReportingSplit.DEFAULT,
                    stage_detail=EmissionFactorValueStageDetail.NO_DETAIL,
                    emission_calculation_type=EmissionCalculationType.DEFAULT,
                    stage=EmissionFactorValueStage.PRINCIPAL,
                )
                emission_factor_custom.stage_detail = EmissionFactorValueStageDetail.FULL_DETAIL
                emission_factor_custom = client.emission_factors.emission_factors_custom.update(
                    **emission_factor_custom.model_dump(mode="json"),
                )
                print("Emission factor", emission_factor_custom)

                emission_factor_value_set = client.emission_factors.emission_factor_values.latest_set(
                    emission_factor_id=emission_factor_custom.id, )

                # Principal emission factor
                emission_factor_value_principal = \
                [efv for efv in emission_factor_value_set if efv.stage == EmissionFactorValueStage.PRINCIPAL][0]
                emission_factor_value_principal.greenhouse_gases.CO2EQ.factor = float(
                    row["Combustion EF (kgCO2e/unit)"])
                client.emission_factors.emission_factor_values.update(
                    **emission_factor_value_principal.model_dump(mode="json"),
                )
                if not pd.isna(row["Generation EF (kgCO2e/unit)"]):
                    emission_factor_value_t_d = [efv for efv in emission_factor_value_set if
                                                 efv.stage == EmissionFactorValueStage.ENERGY_AND_FUEL_GENERATION][0]
                    emission_factor_value_t_d.greenhouse_gases.CO2EQ.factor = float(
                        row["Generation EF (kgCO2e/unit)"])
                    client.emission_factors.emission_factor_values.update(
                        **emission_factor_value_t_d.model_dump(mode="json"),
                    )
                if not pd.isna(row["T&D EF (kgCO2e/unit)"]):
                    emission_factor_value_t_d = [efv for efv in emission_factor_value_set if
                                                 efv.stage == EmissionFactorValueStage.ENERGY_AND_FUEL_TRANSMISSION_DISTRIBUTION][
                        0]
                    emission_factor_value_t_d.greenhouse_gases.CO2EQ.factor = float(
                        row["T&D EF (kgCO2e/unit)"])
                    client.emission_factors.emission_factor_values.update(
                        **emission_factor_value_t_d.model_dump(mode="json"),
                    )


if __name__ == "__main__":
    load_dotenv()
    file = "data/Emission factors_Bulk Upload_Custom Astorg.xlsx"
    upload_custom_emission_factors(
        file_path=file,
        sheet_name="EF to import",
    )
