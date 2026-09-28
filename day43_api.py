from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load trained model and scaler
model = joblib.load("day43_churn_model.pkl")
scaler = joblib.load("day43_scaler.pkl")

# Create FastAPI application
app = FastAPI(
    title="Customer Churn Prediction API",
    description="API for predicting customer churn probability",
    version="1.0"
)


# Prediction request format
class CustomerData(BaseModel):
    tenure: float
    MonthlyCharges: float
    TotalCharges: float


# Home endpoint
@app.get("/")
def home():
    return {
        "message": "Customer Churn Prediction API is running!"
    }


# Prediction endpoint
@app.post("/predict")
def predict_churn(customer: CustomerData):

    input_data = np.array([[
        customer.tenure,
        customer.MonthlyCharges,
        customer.TotalCharges
    ]])

    # Scale input
    input_scaled = scaler.transform(input_data)

    # Prediction
    probability = model.predict_proba(input_scaled)[0][1]
    prediction = model.predict(input_scaled)[0]

    if prediction == 1:
        risk = "High Churn Risk"
    else:
        risk = "Low Churn Risk"

    return {
        "churn_prediction": int(prediction),
        "churn_probability": round(float(probability), 4),
        "risk_level": risk
    }