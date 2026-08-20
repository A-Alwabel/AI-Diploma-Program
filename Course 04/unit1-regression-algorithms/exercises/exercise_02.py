"""
Unit 1 - Exercise 2: Linear Regression Practice
أساليب معالجة البيانات - تمرين 2: ممارسة الانحدار الخطي

Instructions:
1. Create a simple linear regression model to predict house prices based on size
2. Evaluate the model using appropriate metrics
3. Visualize the results
4. Make predictions for new data points

Use the provided dataset
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Generate sample housing data
np.random.seed(42)
house_sizes = np.random.uniform(800, 4000, 150)
house_prices = 45 * house_sizes + 80000 + np.random.normal(0, 35000, 150)

df = pd.DataFrame({
    'size': house_sizes,
    'price': house_prices
})

print("Dataset Info:")
print(f"Shape: {df.shape}")
print(df.head())

# TODO: Write your code here
# TODO: اكتب الكود الخاص بك هنا

# Task 1: Split the data into train and test sets (80/20)
print("\nTask 1: Split data")
# Your code here...

# Task 2: Create and train a Linear Regression model
print("\nTask 2: Train Linear Regression model")
# Your code here...

# Task 3: Make predictions and evaluate the model
print("\nTask 3: Evaluate model")
# Your code here...

# Task 4: Visualize the results
print("\nTask 4: Visualize results")
# Your code here...

# Task 5: Make predictions for new house sizes: [1000, 2000, 3000]
print("\nTask 5: Predict for new sizes")
new_sizes = [[1000], [2000], [3000]]
# Your code here...

print("\nExercise 2 Complete!")
print("اكتمل التمرين 2!")

