import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.set_page_config(
    page_title="Customer Intelligence Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Customer Intelligence Dashboard")
st.write(
    "Interactive dashboard for customer KPIs, retention, "
    "churn analytics, and predictive risk."
)

# Load customer data
st.sidebar.header("📂 Data & Filters")

uploaded_file = st.sidebar.file_uploader(
    "Upload Customer CSV",
    type=["csv"]
)

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
else:
    data = pd.read_csv("WA_FnUseC_TelcoCustomerChurn.csv")

# Prepare data
data["TotalCharges"] = pd.to_numeric(
    data["TotalCharges"],
    errors="coerce"
)

data = data.dropna(subset=["TotalCharges"]).copy()

data["ChurnFlag"] = data["Churn"].map({
    "Yes": 1,
    "No": 0
})

st.sidebar.subheader("🔎 Filters")

contract_options = sorted(data["Contract"].dropna().unique())

contract_filter = st.sidebar.multiselect(
    "Contract Type",
    contract_options,
    default=contract_options
)

churn_filter = st.sidebar.multiselect(
    "Churn Status",
    ["No", "Yes"],
    default=["No", "Yes"]
)

min_tenure = int(data["tenure"].min())
max_tenure = int(data["tenure"].max())

tenure_filter = st.sidebar.slider(
    "Tenure (Months)",
    min_tenure,
    max_tenure,
    (min_tenure, max_tenure)
)

data = data[
    data["Contract"].isin(contract_filter) &
    data["Churn"].isin(churn_filter) &
    data["tenure"].between(tenure_filter[0], tenure_filter[1])
]

st.success("Customer data loaded successfully!")

# KPI calculations
total_customers = len(data)
churned_customers = data["ChurnFlag"].sum()
active_customers = total_customers - churned_customers

retention_rate = (active_customers / total_customers) * 100
churn_rate = (churned_customers / total_customers) * 100

average_monthly_charge = data["MonthlyCharges"].mean()
average_tenure = data["tenure"].mean()

# KPI Cards
st.subheader("📌 Key Business Metrics")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Customers",
    total_customers
)

col2.metric(
    "Active Customers",
    active_customers
)

col3.metric(
    "Churn Rate",
    f"{churn_rate:.2f}%"
)

col4.metric(
    "Retention Rate",
    f"{retention_rate:.2f}%"
)

st.subheader("📊 Customer Overview")

st.write(
    f"Average Monthly Charge: **{average_monthly_charge:.2f}**"
)

st.write(
    f"Average Tenure: **{average_tenure:.2f} months**"
)

st.subheader("Dataset Preview")
st.dataframe(data.head(10))

# Churn Analytics
st.subheader("📈 Churn Analytics")

churn_counts = data["Churn"].value_counts()

col1, col2 = st.columns(2)

with col1:
    st.write("### Customer Churn Distribution")
    st.bar_chart(churn_counts)

with col2:
    st.write("### Churn by Contract Type")

    contract_churn = pd.crosstab(
        data["Contract"],
        data["Churn"]
    )

    st.bar_chart(contract_churn)

    # Customer Segmentation
st.subheader("👥 Customer Segmentation")

data["CustomerSegment"] = pd.cut(
    data["tenure"],
    bins=[-1, 12, 36, 100],
    labels=[
        "New Customers",
        "Growing Customers",
        "Loyal Customers"
    ]
)

segment_counts = data["CustomerSegment"].value_counts()

col1, col2 = st.columns(2)

with col1:
    st.write("### Customers by Segment")
    st.bar_chart(segment_counts)

with col2:
    st.write("### Churn Rate by Segment")

    segment_churn = (
        data.groupby("CustomerSegment", observed=False)["ChurnFlag"]
        .mean() * 100
    )

    st.bar_chart(segment_churn)

   # Predictive Churn Risk
st.subheader("🔮 Predictive Churn Risk")

# Load trained model and scaler
model = joblib.load("day43_churn_model.pkl")
scaler = joblib.load("day43_scaler.pkl")

features = [
    "tenure",
    "MonthlyCharges",
    "TotalCharges"
]

X = data[features]

# Scale customer data
X_scaled = scaler.transform(X)

# Predict churn probability
data["ChurnProbability"] = model.predict_proba(X_scaled)[:, 1]

# Create risk levels
data["RiskLevel"] = np.where(
    data["ChurnProbability"] >= 0.70,
    "High Risk",
    np.where(
        data["ChurnProbability"] >= 0.40,
        "Medium Risk",
        "Low Risk"
    )
)

risk_counts = data["RiskLevel"].value_counts()

col1, col2 = st.columns(2)

with col1:
    st.write("### Customer Risk Distribution")
    st.bar_chart(risk_counts)

with col2:
    st.write("### High-Risk Customers")

    high_risk = data[
        data["RiskLevel"] == "High Risk"
    ][
        ["customerID", "tenure", "MonthlyCharges",
         "TotalCharges", "ChurnProbability", "RiskLevel"]
    ].sort_values(
        "ChurnProbability",
        ascending=False
    )

    st.dataframe(
        high_risk.head(10),
        use_container_width=True
    )