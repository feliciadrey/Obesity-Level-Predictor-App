from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd

#Load pipeline
with open("pipeline.pkl", "rb") as f:
    pipeline = pickle.load(f)

app = FastAPI()

#Input schema sesuai fitur 
class InputData(BaseModel):
    Gender: int
    Age: int
    Height: float
    Weight: float
    family_history_with_overweight: int
    FAVC: int
    FCVC: int
    NCP: int
    CAEC: int
    SMOKE: int
    CH2O: int
    SCC: int
    FAF: int
    TUE: int
    CALC: int
    MTRANS: int

#Mapping label ke nama kelas
label_mapping = {
    0: 'Insufficient_Weight',
    1: 'Normal_Weight',
    2: 'Obesity_Type_I',
    3: 'Obesity_Type_II',
    4: 'Obesity_Type_III',
    5: 'Overweight_Level_I',
    6: 'Overweight_Level_II'
}

#List kolom sesuai urutan training
expected_cols = [
    'Gender', 'Age', 'Height', 'Weight', 'family_history_with_overweight',
    'FAVC', 'FCVC', 'NCP', 'CAEC', 'SMOKE', 'CH2O',
    'SCC', 'FAF', 'TUE', 'CALC', 'MTRANS'
]

@app.post("/predict")
def predict(data: InputData):
    input_dict = data.dict()

    df = pd.DataFrame([[input_dict[col] for col in expected_cols]], columns=expected_cols)
    pred = pipeline.predict(df)[0]
    label = label_mapping[int(pred)]

    return {
        "prediction": int(pred),
        "label": label
    }
