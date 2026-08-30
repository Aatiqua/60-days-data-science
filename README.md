# 60-days-data-science

Project: Sales Data Analysis

Problem Statement

The objective of this project is to analyze sales data and identify useful patterns and trends. The analysis will help understand product-wise sales performance and generate meaningful insights from the dataset.

Domain

Sales

Dataset

The dataset used for this project is "statsfinal.csv".

Tools & Libraries

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn

Analysis

The project includes:

- Loading and exploring the sales dataset
- Checking dataset information
- Calculating basic statistics
- Checking for missing values
- Analyzing sales data
- Creating visualizations
- Finding useful sales insights

Project Files

- "statsfinal.csv" — Sales dataset
- "sales_analysis.py" — Python analysis program
- "README.md" — Project documentation

Goal

The goal is to use Python and data analysis techniques to understand the sales data and present the findings through clear visualizations and insights.

Day 8 — Exploratory Data Analysis (EDA)

Business Insights

1. Sales are centered around ₹52,000: The mean Total Sales is approximately 51,633, while the median is approximately 51,873. This shows that typical sales are around the ₹52,000 level.

2. Sales show considerable variation: Total Sales range from approximately 11,296 to 93,819, indicating significant differences in sales performance across observations.

3. Quantity varies substantially: Total Quantity ranges from approximately 2,069 to 19,108, showing that the volume of products sold differs considerably across observations.

4. Sales and quantity can be compared to understand business performance: The relationship visualization helps examine whether higher quantities are generally associated with higher sales.

5. Potential anomalies require further investigation: The distribution and box plot reveal extreme observations that may represent unusual sales or quantity values. These should be investigated before making business decisions.

EDA Learning Outcomes

- Understood the purpose of Exploratory Data Analysis.
- Learned to use Pandas for summary statistics.
- Created distribution and relationship visualizations using Matplotlib and Seaborn.
- Learned to identify patterns and potential anomalies.
- Practiced communicating data-driven business insights.


## Day 9 — Data Cleaning & Preparation

Cleaning Process

The dataset was cleaned and prepared to improve data quality and ensure reliable analysis.

Missing Values

Missing values were identified using Pandas. Numeric missing values were handled using the median, while categorical/text missing values were handled using the mode.

Duplicate Records

Duplicate records were detected using "df.duplicated().sum()" and removed using "df.drop_duplicates()".

Data Formats

The "Date" column was converted from text to a proper datetime format using "pd.to_datetime()".

Feature Creation

Two useful features were created:

- "Total_Sales" — total sales across all products.
- "Total_Quantity" — total quantity across all products.

Validation

After cleaning, the dataset was checked again for missing values, duplicates, and correct data types.

Output

The final cleaned dataset was saved as:

"cleaned_statsfinal.csv"

The cleaning process improves the reliability and consistency of the dataset for further analysis and machine learning.


## Day 10 — Feature Engineering

### Objective

Feature engineering was performed to prepare the cleaned dataset for machine learning.

### Work Completed

- Identified numerical and categorical features.
- Applied one-hot encoding to categorical features.
- Applied StandardScaler to numerical features.
- Created two derived features:
  - Sales_per_Quantity
  - Sales_per_Product
- Compared the dataset before and after feature engineering.
- Checked the final dataset for missing values.

### Model Readiness

Before feature engineering, the dataset contained the original features, including categorical information.

After feature engineering, categorical features were encoded into numerical values and numerical features were scaled. Two additional derived features were also created.

Therefore, the resulting dataset is more suitable as input for machine learning models.

### Output

The feature-engineered dataset was saved as:

feature_engineered_statsfinal.csv


## Day 11 — Machine Learning Foundations

### ML Workflow

- Loaded the cleaned dataset.
- Selected Total_Sales as the target variable.
- Split the data into 80% training and 20% testing sets.
- Used Linear Regression as the baseline algorithm.
- Trained the model on the training data.
- Generated predictions on the test data.
- Evaluated prediction quality using MAE, RMSE, and R² Score.
- Saved predictions in prediction_outputs.csv.

### Output

The prediction output contains actual and predicted Total Sales values for the test dataset.


## Day 12 — Regression Modeling

### Objective

The objective of this task was to build a Linear Regression model to predict `Total_Sales` and understand relationships between input features and the target variable.

### Work Completed

- Prepared the dataset for regression modeling.
- Selected `Total_Sales` as the target variable.
- Split the dataset into training and testing sets.
- Trained a Linear Regression model.
- Generated predictions on the test data.
- Evaluated the model using MAE, RMSE, and R² Score.
- Created an Actual vs Predicted visualization.
- Visualized prediction errors.
- Analyzed the model coefficients.

### Prediction Analysis

The Actual vs Predicted plot was used to compare the model's predictions with the actual sales values.

The prediction-error plot was used to identify unusual errors and patterns in the model's predictions.

### Model Coefficients

The regression coefficients were examined to understand how the input features influence predicted Total Sales.

### Output Files

- `regression_modeling.ipynb`
- `regression_predictions.csv`
- `regression_coefficients.csv`


## Day 13 — Model Optimization

### Objective

The objective of this task was to understand overfitting and regularization by comparing Linear Regression, Ridge Regression, and Lasso Regression.

### Models Used

- **Linear Regression:** Used as the baseline model.
- **Ridge Regression:** Uses L2 regularization to control large coefficients.
- **Lasso Regression:** Uses L1 regularization and can reduce some coefficients toward zero.

### Performance Comparison

Training and testing R² and RMSE scores were calculated for all three models.

A large difference between train and test performance may indicate overfitting. A smaller difference generally indicates better generalization.

### Key Learning

Regularization helps control model complexity and can improve a model's ability to generalize to unseen data.

The comparison between Linear, Ridge, and Lasso Regression demonstrates how different regularization techniques affect model behavior.

### Output

The model comparison results were saved as:

`model_comparison.csv`