from utils import (
    highrisk_midrisk_lowrisk_splitter,
    make_empty_dataframe,
    make_age_column,
    make_monthly_income,
    make_marital_status,
    make_gender,
    make_no_of_dependents,
)
import pandas as pd


def make_highrisk_dataframe(no_of_high_risk_datapoints):
    highrisk_df = make_empty_dataframe()

    age_distribution = {"18-30": 70, "30-50": 20, "50-80": 10}
    highrisk_df["age"] = make_age_column(no_of_high_risk_datapoints, age_distribution)

    income_distribution = {"40-60": 5, "60-80": 5, "80-100": 60, "100-200": 30}
    highrisk_df["monthly_income"] = make_monthly_income(
        no_of_high_risk_datapoints, income_distribution
    )

    marital_status_distribution = {"married": 30, "unmarried": 70}
    highrisk_df["marital_status"] = make_marital_status(
        no_of_high_risk_datapoints, marital_status_distribution
    )

    gender_distribution = {"male": 70, "female": 30}
    highrisk_df["sex"] = make_gender(no_of_high_risk_datapoints, gender_distribution)

    no_of_dependents_distribution = {0: 30, 1: 30, 2: 20, 3: 10, 4: 5, 5: 5}
    highrisk_df["no_of_dependents"] = make_no_of_dependents(
        no_of_high_risk_datapoints, no_of_dependents_distribution
    )

    highrisk_df.to_csv("data/highrisk_dataset.csv")

    return highrisk_df


def make_midrisk_dataframe(no_of_mid_risk_datapoints):
    midrisk_df = make_empty_dataframe()

    age_distribution = {"18-30": 40, "30-50": 35, "50-80": 25}
    midrisk_df["age"] = make_age_column(no_of_mid_risk_datapoints, age_distribution)

    income_distribution = {"10-20": 5, "20-40": 25, "40-60": 70}
    midrisk_df["monthly_income"] = make_monthly_income(
        no_of_mid_risk_datapoints, income_distribution
    )

    marital_status_distribution = {"married": 50, "unmarried": 50}
    midrisk_df["marital_status"] = make_marital_status(
        no_of_mid_risk_datapoints, marital_status_distribution
    )

    gender_distribution = {"male": 50, "female": 50}
    midrisk_df["sex"] = make_gender(no_of_mid_risk_datapoints, gender_distribution)

    no_of_dependents_distribution = {0: 5, 1: 20, 2: 30, 3: 30, 4: 10, 5: 5}
    midrisk_df["no_of_dependents"] = make_no_of_dependents(
        no_of_mid_risk_datapoints, no_of_dependents_distribution
    )

    midrisk_df.to_csv("data/midrisk_dataset.csv")

    return midrisk_df


def make_lowrisk_dataframe(no_of_low_risk_datapoints):
    lowrisk_df = make_empty_dataframe()

    age_distribution = {"18-30": 10, "30-50": 20, "50-80": 70}
    lowrisk_df["age"] = make_age_column(no_of_low_risk_datapoints, age_distribution)

    income_distribution = {"10-20": 10, "20-40": 20, "40-60": 70}
    lowrisk_df["monthly_income"] = make_monthly_income(
        no_of_low_risk_datapoints, income_distribution
    )

    marital_status_distribution = {"married": 50, "unmarried": 50}
    lowrisk_df["marital_status"] = make_marital_status(
        no_of_low_risk_datapoints, marital_status_distribution
    )

    gender_distribution = {"male": 50, "female": 50}
    lowrisk_df["sex"] = make_gender(no_of_low_risk_datapoints, gender_distribution)

    no_of_dependents_distribution = {0: 5, 1: 5, 2: 10, 3: 20, 4: 30, 5: 30}
    lowrisk_df["no_of_dependents"] = make_no_of_dependents(
        no_of_low_risk_datapoints, no_of_dependents_distribution
    )

    lowrisk_df.to_csv("data/lowrisk_dataset.csv")

    return lowrisk_df


def main():
    total_data_points = int(input("Enter total number of data points you need : "))
    (
        no_of_highrisk_data_points,
        no_of_midrisk_data_points,
        no_of_low_risk_data_points,
    ) = highrisk_midrisk_lowrisk_splitter(total_data_points)
    make_highrisk_dataframe(no_of_highrisk_data_points)
    make_midrisk_dataframe(no_of_midrisk_data_points)
    make_lowrisk_dataframe(no_of_low_risk_data_points)
    df1 = pd.read_csv("data/highrisk_dataset.csv")
    df2 = pd.read_csv("data/midrisk_dataset.csv")
    df3 = pd.read_csv("data/lowrisk_dataset.csv")
    df = pd.concat([df1, df2, df3])
    df.to_csv("data/dataset.csv", index=False)


main()
