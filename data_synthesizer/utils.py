from random import randint
import pandas as pd


def make_empty_dataframe():
    column_names = [
        "age",
        "monthly_income",
        "sex",
        "marital_status",
        "no_of_dependents",
    ]
    df = pd.DataFrame(columns=column_names)

    return df


def highrisk_midrisk_lowrisk_splitter(total_data_points):
    return (
        int(40 * total_data_points / 100),
        int(20 * total_data_points / 100),
        int(40 * total_data_points / 100),
    )


def make_age_column(no_of_data_points, age_distribution):
    age = []
    for key in age_distribution.keys():
        for _ in range(age_distribution[key] * no_of_data_points // 100):
            age.append(randint(int(key.split("-")[0]), int(key.split("-")[1])))

    return age


def make_monthly_income(no_of_data_points, income_distribution):
    income = []
    for key in income_distribution.keys():
        for _ in range(income_distribution[key] * no_of_data_points // 100):
            income.append(randint(int(key.split("-")[0]), int(key.split("-")[1])))
    income.reverse()
    return income


def make_marital_status(no_of_data_points, marital_status_distribution):
    marital_status = []
    for _ in range(marital_status_distribution["unmarried"] * no_of_data_points // 100):
        marital_status.append(0)
    for _ in range(marital_status_distribution["married"] * no_of_data_points // 100):
        marital_status.append(1)

    return marital_status


def make_gender(no_of_data_points, gender_distribution):
    gender = []
    sample_space_array = []
    sample_space_array += [1] * gender_distribution["male"]
    sample_space_array += [0] * gender_distribution["female"]

    for _ in range(no_of_data_points):
        gender.append(sample_space_array[randint(0, 99)])

    return gender


def make_no_of_dependents(no_of_data_points, no_of_dependents_distribution):
    no_of_dependents = []
    for i in range(no_of_dependents_distribution[0] * no_of_data_points // 100):
        no_of_dependents.append(0)
    for i in range(no_of_dependents_distribution[1] * no_of_data_points // 100):
        no_of_dependents.append(1)
    for i in range(no_of_dependents_distribution[2] * no_of_data_points // 100):
        no_of_dependents.append(2)
    for i in range(no_of_dependents_distribution[3] * no_of_data_points // 100):
        no_of_dependents.append(3)
    for i in range(no_of_dependents_distribution[4] * no_of_data_points // 100):
        no_of_dependents.append(4)
    for i in range(no_of_dependents_distribution[5] * no_of_data_points // 100):
        no_of_dependents.append(5)

    return no_of_dependents
