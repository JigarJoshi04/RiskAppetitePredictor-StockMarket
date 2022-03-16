import pickle
from joblib import load

model_scaler = load("model/scaler.pkl")
model = pickle.load(open("model/model.sav", "rb"))


"""
0 => low risk 
1 => mid risk
2 => high risk

sex => 1 => male
sex => 0 => female

marital_status => 1 => married
marital_status => 0 => unmarried

no_of_dependets (any value from 0 to 5 both inclusive)
"""


def predict_risk_appetite(age, monthly_income, sex, marital_status, no_of_dependents):
    return model.predict(
        model_scaler.transform(
            [[age, monthly_income, sex, marital_status, no_of_dependents]]
        )
    )[0]


print(
    predict_risk_appetite(
        age=25, monthly_income=100000, sex=1, marital_status=0, no_of_dependents=0
    )
)
