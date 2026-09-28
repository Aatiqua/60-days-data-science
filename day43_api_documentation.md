# Day 43 – Machine Learning Model Deployment API

## Overview

This project deploys a customer churn prediction model as a REST API
using FastAPI.

The API accepts customer information and returns a churn prediction,
churn probability, and risk level.

## Model

- Model: Logistic Regression
- Features:
  - Tenure
  - Monthly Charges
  - Total Charges
- Scaling: StandardScaler

## API Endpoint

### GET /

Checks whether the API is running.

Example response:

```json
{
  "message": "Customer Churn Prediction API is running!"
}