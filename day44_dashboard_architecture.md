# Day 44 – Dashboard Architecture Explanation

## Overview

The Customer Intelligence Dashboard is an interactive Streamlit application
designed to analyze customer behavior, retention, churn, segmentation, and
predictive churn risk.

## Architecture

Customer CSV Dataset
        ↓
Data Loading & Cleaning
        ↓
User Upload / Sidebar Filters
        ↓
Data Processing
        ↓
├── KPI Analytics
├── Churn Analytics
├── Customer Segmentation
└── Predictive Churn Risk
        ↓
Interactive Streamlit Dashboard
        ↓
Business Insights & Decisions

## Main Components

### 1. Data Layer
The dashboard loads the Telco customer dataset using Pandas. Users can also
upload another compatible CSV file.

### 2. Data Processing
Missing TotalCharges values are handled and customer churn is converted into
a numerical ChurnFlag.

### 3. Filtering Layer
Users can filter customers by:
- Contract Type
- Churn Status
- Tenure

### 4. KPI Layer
The dashboard displays important business metrics such as:
- Total Customers
- Active Customers
- Churn Rate
- Retention Rate
- Average Monthly Charge
- Average Tenure

### 5. Analytics Layer
The dashboard provides:
- Customer churn distribution
- Churn by contract type
- Customer segmentation
- Churn rate by segment
- Predictive churn risk

### 6. Machine Learning Layer
The Logistic Regression model developed in Day 43 is loaded into the dashboard.
It calculates churn probability for customers and categorizes them into:
- Low Risk
- Medium Risk
- High Risk

### 7. Presentation Layer
Streamlit provides an interactive business-friendly interface with KPI cards,
charts, tables, sidebar controls, and customer risk information.

## Business Impact

The dashboard helps businesses monitor customer behavior, identify customers
at risk of churn, understand customer segments, and support data-driven
retention decisions.