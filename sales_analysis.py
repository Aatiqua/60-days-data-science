import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the sales dataset
df = pd.read_csv("statsfinal.csv")

# Display first 5 rows
print("First 5 rows:")
print(df.head())

# Display dataset information
print("\nDataset Information:")
print(df.info())

# Display basic statistics
print("\nBasic Statistics:")
print(df.describe())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())
