# Obesity Level Prediction Application

This project builds a machine learning pipeline to predict obesity levels based on demographic and lifestyle data, using an XGBoost classifier deployed with FastAPI and Streamlit.

---
## Overview

- **Goal:** Classify individuals into one of seven obesity categories.
- **Data Processing:** Cleaned data, encoded categorical features to numeric, scaled numeric features using RobustScaler, and handled class imbalance with RandomOverSampler.
- **Model:** XGBoost classifier trained on oversampled, scaled features and saved within a pipeline including preprocessing steps.
- **Deployment:**  
  - **Backend:** FastAPI serving a `/predict` endpoint that accepts JSON inputs and returns predicted obesity categories.  
  - **Frontend:** Streamlit app where users input features via intuitive controls; data is encoded and sent to the backend for prediction.

---

## Features

- Preprocessing and modeling aligned between training and prediction using sklearn Pipeline.
- Consistent feature encoding in both frontend and backend.
- Model and scaler saved for consistent, reproducible inference.
- Tested with example inputs to ensure accurate prediction outputs.

---

For full details and code, refer to the notebook and source files.
