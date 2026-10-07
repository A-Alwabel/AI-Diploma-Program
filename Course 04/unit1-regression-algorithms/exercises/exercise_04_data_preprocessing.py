"""
Unit 1 - Exercise 4: Data Preprocessing Practice
Data processing methods - Exercise 4: Practising data preprocessing

Instructions:
1. Load the credit card fraud dataset (or use provided sample data)
2. Identify numerical and categorical features
3. Apply feature scaling (StandardScaler and MinMaxScaler)
4. Encode categorical variables (LabelEncoder and OneHotEncoder)
5. Split data into training and testing sets
6. Compare different preprocessing methods

GDI Theme: Financial Investigations - Preparing transaction data for fraud detection models
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import (
    StandardScaler,
    MinMaxScaler,
    LabelEncoder,
    OneHotEncoder
)
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns

# Set random seed for reproducibility
np.random.seed(73)

# Generate sample financial transaction data (GDI Theme: Financial Investigations)
# This simulates transaction data that needs preprocessing for fraud detection
print("📥 Generating sample financial transaction data...")
print("Building the sample financial-transactions data...")
print("   GDI Theme: Financial Investigations / Terrorism Financing Detection\n")

# Create sample dataset with mixed data types
n_samples = 500
data = {
    'transaction_amount': np.random.uniform(10, 10000, n_samples),
    'transaction_time': np.random.uniform(0, 24, n_samples),
    'merchant_category': np.random.choice(['Retail', 'Online', 'Gas', 'Restaurant', 'Travel'], n_samples),
    'payment_method': np.random.choice(['Credit', 'Debit', 'Cash', 'Digital'], n_samples),
    'transaction_region': np.random.choice(['North', 'South', 'East', 'West', 'Central'], n_samples),
    'customer_age': np.random.randint(18, 80, n_samples),
    'account_balance': np.random.uniform(100, 50000, n_samples),
    'risk_level': np.random.choice(['Low', 'Medium', 'High'], n_samples)  # Categorical target
}

df = pd.DataFrame(data)

print(f"✅ Sample dataset created!")
print(f"   📊 Shape: {df.shape}")
print(f"   📊 Columns: {list(df.columns)}")
print(f"\n📋 Data Types:")
print(df.dtypes)
print(f"\n📋 First few rows:")
print(df.head())

# TODO: Write your code here
# TODO: write your code here

# Task 1: Identify feature types
print("\n" + "=" * 60)
print("Task 1: Identify Feature Types")
print("Task 1: Identify feature types")
print("=" * 60)
# TODO: Separate numerical and categorical features
# Hint: Use df.select_dtypes(include=['number']) for numerical
# Hint: Use df.select_dtypes(include=['object']) for categorical
# Your code here...

# Task 2: Feature Scaling - StandardScaler
print("\n" + "=" * 60)
print("Task 2: Feature Scaling - StandardScaler")
print("Task 2: Scale features - StandardScaler")
print("=" * 60)
# TODO: Apply StandardScaler to numerical features
# Steps:
# 1. Select numerical features (e.g., transaction_amount, transaction_time, customer_age, account_balance)
# 2. Create StandardScaler object
# 3. Fit on training data (after split) or on full data for demonstration
# 4. Transform the features
# 5. Display before/after statistics (mean, std)
# Your code here...

# Task 3: Feature Scaling - MinMaxScaler
print("\n" + "=" * 60)
print("Task 3: Feature Scaling - MinMaxScaler")
print("Task 3: Scale features - MinMaxScaler")
print("=" * 60)
# TODO: Apply MinMaxScaler to numerical features
# Steps:
# 1. Create MinMaxScaler object
# 2. Fit and transform numerical features
# 3. Display before/after statistics (min, max)
# 4. Compare with StandardScaler results
# Your code here...

# Task 4: Categorical Encoding - LabelEncoder
print("\n" + "=" * 60)
print("Task 4: Categorical Encoding - LabelEncoder")
print("Task 4: Encode categories - LabelEncoder")
print("=" * 60)
# TODO: Apply LabelEncoder to ordinal categorical features
# Steps:
# 1. Select ordinal categorical feature (e.g., risk_level: Low=0, Medium=1, High=2)
# 2. Create LabelEncoder object
# 3. Fit and transform the feature
# 4. Display mapping (original values -> encoded values)
# Your code here...

# Task 5: Categorical Encoding - OneHotEncoder
print("\n" + "=" * 60)
print("Task 5: Categorical Encoding - OneHotEncoder")
print("Task 5: Encode categories - OneHotEncoder")
print("=" * 60)
# TODO: Apply OneHotEncoder to nominal categorical features
# Steps:
# 1. Select nominal categorical features (e.g., merchant_category, payment_method, transaction_region)
# 2. Create OneHotEncoder object
# 3. Fit and transform the features
# 4. Convert to DataFrame for better visualization
# 5. Display the encoded columns
# Your code here...

# Task 6: Train-Test Split
print("\n" + "=" * 60)
print("Task 6: Train-Test Split")
print("Task 6: Split the data")
print("=" * 60)
# TODO: Split data into training and testing sets
# Steps:
# 1. Prepare features (X) - all columns except target
# 2. Prepare target (y) - risk_level or create binary target
# 3. Use train_test_split with test_size=0.2, random_state=73
# 4. Display shapes of train/test sets
# Your code here...

# Task 7: Complete Preprocessing Pipeline
print("\n" + "=" * 60)
print("Task 7: Complete Preprocessing Pipeline")
print("Task 7: The complete preprocessing pipeline")
print("=" * 60)
# TODO: Create a complete preprocessing pipeline
# Steps:
# 1. Split data first (train/test)
# 2. Scale numerical features on training data
# 3. Apply scaling to test data (using scaler fitted on train)
# 4. Encode categorical features
# 5. Combine scaled numerical + encoded categorical features
# 6. Display final preprocessed data shape
# Your code here...

# Task 8: Visualization - Compare Before/After Scaling
print("\n" + "=" * 60)
print("Task 8: Visualization - Compare Before/After Scaling")
print("Task 8: Visualisation - before and after scaling")
print("=" * 60)
# TODO: Create visualizations comparing original vs scaled features
# Steps:
# 1. Plot distribution of original numerical feature (e.g., transaction_amount)
# 2. Plot distribution after StandardScaler
# 3. Plot distribution after MinMaxScaler
# 4. Use subplots to show side-by-side comparison
# 5. Add titles and labels
# Your code here...

print("\n" + "=" * 60)
print("Exercise 4 Complete!")
print("Exercise 4 complete.")
print("=" * 60)
print("\n📚 What You Learned:")
print("   ✅ Feature scaling (StandardScaler vs MinMaxScaler)")
print("   ✅ Categorical encoding (LabelEncoder vs OneHotEncoder)")
print("   ✅ Train-test split for proper evaluation")
print("   ✅ Complete preprocessing pipeline")
print("   ✅ GDI context: Preparing financial data for fraud detection")

