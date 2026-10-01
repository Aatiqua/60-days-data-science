# Day 45 – Cloud Deployment Architecture Report

## Project
Customer Intelligence Dashboard

## Deployment Platform
Streamlit Community Cloud

## Objective
Deploy the Customer Intelligence Dashboard to a cloud platform so that
users can access and interact with the analytics system through a web browser.

## Deployment Architecture

GitHub Repository
        ↓
Streamlit Community Cloud
        ↓
requirements.txt
        ↓
Streamlit Application
(day44_dashboard.py)
        ↓
Data Processing & Analytics
        ↓
Machine Learning Model
(day43_churn_model.pkl)
        ↓
Customer Intelligence Dashboard
        ↓
Public Web Browser

## Main Components

### 1. GitHub Repository
The project source code, dashboard application, machine learning model,
dataset, and dependency configuration are stored in GitHub.

### 2. Streamlit Community Cloud
Streamlit Community Cloud pulls the application from the GitHub repository
and runs the Streamlit application online.

### 3. Requirements Configuration
The `requirements.txt` file specifies the Python libraries required by the
application, including Streamlit, Pandas, NumPy, Scikit-learn, and Joblib.

### 4. Dashboard Application
`day44_dashboard.py` provides the interactive Customer Intelligence Dashboard
with KPI analytics, churn analysis, customer segmentation, filters, CSV
upload, and predictive churn-risk analysis.

### 5. Machine Learning Model
The Logistic Regression churn model created during Day 43 is loaded by the
dashboard to calculate customer churn probabilities.

### 6. User Interface
Users can access the deployed application through a web browser and interact
with the dashboard without running Python locally.

## Live Deployment

Live application:
https://60-days-data-science-dv79e9yybfbcbpxlxqyafh.streamlit.app/

## Testing Performed

The deployed application was tested for:

- Dashboard loading
- KPI display
- Customer churn analytics
- Customer segmentation
- Contract filtering
- Churn-status filtering
- Tenure filtering
- Predictive churn-risk display
- CSV upload functionality

## Deployment Challenges

During deployment, the application required a `requirements.txt` file so that
the cloud platform could install the required Python dependencies.

The deployment also required the correct GitHub repository, branch, and
Streamlit entrypoint file.

## Outcome

The Customer Intelligence Dashboard was successfully deployed as a publicly
accessible Streamlit application. The system can now be accessed through a
web browser and used for interactive customer analytics.