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


## Day 14 — Sprint 2 Review

### Real-World Feature Removal Challenge

The most important feature identified during the analysis was `S-P4`.

To simulate a real-world situation where an important feature becomes unavailable, `S-P4` was removed and the best-performing model from Day 13 was retrained.

### Performance Comparison

The model was evaluated before and after removing `S-P4` using:

- R² Score
- RMSE

The results are available in `day14_performance_comparison.csv`.

### Key Learning

Removing an important feature can affect model performance because useful information is lost. Retraining allows the model to adapt to the remaining available features.

This experiment demonstrated why real-world ML systems need to be flexible and capable of adapting when datasets or features change.

### Sprint 2 Reflection

Sprint 2 helped me understand the complete ML workflow, including regression, regularization, model evaluation, and feature removal.

I learned that production ML systems must handle changing data and unexpected constraints rather than relying on fixed assumptions.


## Day 15 — Classification Foundations

### Objective

Built a Logistic Regression classification model to predict whether customers are likely to churn.

### Work Completed

- Loaded a customer churn dataset
- Identified the target variable `Churn`
- Encoded categorical features
- Split data into training and testing sets
- Trained a Logistic Regression classifier
- Generated predictions on unseen data
- Evaluated accuracy, precision, recall and F1-score
- Created a confusion matrix
- Analyzed false positives and false negatives
- Documented the business impact of prediction errors

### Business Insight

False negatives can be particularly costly in customer churn prediction because the business may fail to identify customers who are actually at risk of leaving.

False positives can result in unnecessary retention efforts, discounts or offers.

### Files

- `classification_foundations.ipynb`
- `churn_predictions.csv`
- `confusion_matrix.png`

## Day 16 — Distance-Based Learning

### Objective

Built a movie recommendation system using the K-Nearest Neighbors (KNN) algorithm.

### Work Completed

- Created a movie recommendation dataset
- Prepared numerical movie features
- Applied feature scaling
- Trained a KNN model
- Experimented with different K values
- Generated similarity-based movie recommendations
- Compared recommendation distances
- Selected K = 4 as the working value

### Features Used

- Action
- SciFi
- Romance
- Adventure
- Popularity

### Key Learning

KNN recommends items based on similarity and distance. Choosing an appropriate K value is important because it affects how many neighboring items influence the recommendations.

### Files

- `knn_recommendation.ipynb`
- `movie_recommendations.csv`
- `k_comparison.csv`

# Day 17 — Decision Tree Learning

## Objective
Build a Decision Tree classifier for a real-world loan approval problem.

## What I Did
- Created a loan approval dataset
- Prepared features and target variable
- Split the dataset into training and testing sets
- Trained a Decision Tree classifier
- Visualized the Decision Tree
- Analyzed feature importance
- Checked training vs testing accuracy
- Investigated potential overfitting
- Explained how the model makes decisions

## Real-World Application
Decision Trees can be used by banks and financial institutions to support loan approval and risk assessment decisions.

## Key Learning
A Decision Tree makes predictions using a series of feature-based rules. Controlling the tree depth can help reduce overfitting.

## Files
- `decision_tree.ipynb`
- `loan_approval.csv`
- `loan_feature_importance.csv`