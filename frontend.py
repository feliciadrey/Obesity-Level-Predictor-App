import streamlit as st
import requests

st.set_page_config(page_title="Obesity Prediction", layout="centered")
st.title("Obesity Prediction App")

st.markdown("Input your data here:")

col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ["Female", "Male"])
    age = st.slider("Age", 15, 55, 23)
    height = st.number_input("Height (m)", min_value=1.45, max_value=1.95, value=1.70, step=0.01)
    weight = st.number_input("Weight (kg)", min_value=39.0, max_value=173.0, value=86.0, step=0.5)
    family_history = st.selectbox("Family History with Overweight", ["No", "Yes"])
    favc = st.selectbox("Frequent High Caloric Food Consumption (FAVC)", ["No", "Yes"])
    fcvc = st.slider("Vegetable Consumption Frequency (FCVC)", 1, 3, 2, step=1)
    ncp = st.slider("Number of Meals (NCP)", 1, 4, 3, step=1)

with col2:
    caec = st.selectbox("Food Between Meals (CAEC)", ["no", "Sometimes", "Frequently", "Always"])
    smoke = st.selectbox("Smoker", ["No", "Yes"])
    ch2o = st.slider("Water Intake (CH2O)", 1, 3, 2, step=1)
    scc = st.selectbox("Calories Monitoring (SCC)", ["No", "Yes"])
    faf = st.slider("Physical Activity Frequency (FAF)", 0, 3, 1, step=1)
    tue = st.slider("Technology Usage (TUE)", 0, 3, 1, step=1)
    calc = st.selectbox("Alcohol Consumption (CALC)", ["no", "Sometimes", "Frequently", "Always"])
    mtrans = st.selectbox("Transportation", ["Automobile", "Motorbike", "Bike", "Public_Transportation", "Walking"])

input_data = {
    "Gender": 1 if gender == "Male" else 0,
    "Age": age,
    "Height": height,
    "Weight": weight,
    "family_history_with_overweight": 1 if family_history == "Yes" else 0,
    "FAVC": 1 if favc == "Yes" else 0,
    "FCVC": fcvc,
    "NCP": ncp,
    "CAEC": {"no": 0, "Sometimes": 1, "Frequently": 2, "Always": 3}[caec],
    "SMOKE": 1 if smoke == "Yes" else 0,
    "CH2O": ch2o,
    "SCC": 1 if scc == "Yes" else 0,
    "FAF": faf,
    "TUE": tue,
    "CALC": {"no": 0, "Sometimes": 1, "Frequently": 2, "Always": 3}[calc],
    "MTRANS": {
        "Automobile": 0,
        "Motorbike": 1,
        "Bike": 2,
        "Public_Transportation": 3,
        "Walking": 4
    }[mtrans]
}

#Submit ke backend
if st.button("Predict Obesity Level"):
    response = requests.post("http://localhost:8000/predict", json=input_data)
    result = response.json()
    st.success(f"Predicted Category: **{result['label']}** (Class {result['prediction']})")
