"""
Unit 1 - Exercise 1: Data Processing Practice
أساليب معالجة البيانات - تمرين 1: ممارسة معالجة البيانات

Instructions:
1. Load the sample dataset provided below
2. Explore the data (shape, info, statistics)
3. Handle missing values appropriately
4. Remove any duplicates
5. Create visualizations (at least 2 different plots)

Dataset: Sales data for a retail store
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Sample dataset - Sales data
# البيانات النموذجية - بيانات المبيعات
np.random.seed(42)
data = {
    'product_id': range(1, 101),
    'product_name': [f'Product_{i}' for i in range(1, 101)],
    'category': np.random.choice(['Electronics', 'Clothing', 'Food', 'Books', 'Sports'], 100),
    'price': np.random.uniform(10, 500, 100),
    'quantity_sold': np.random.randint(10, 1000, 100),
    'customer_rating': np.random.uniform(1, 5, 100),
    'month': np.random.choice(['Jan', 'Feb', 'Mar', 'Apr', 'May'], 100)
}

df = pd.DataFrame(data)

# Introduce some missing values and duplicates for exercise
df.loc[10:15, 'customer_rating'] = np.nan
df.loc[5:7, 'price'] = np.nan
df = pd.concat([df, df.iloc[[0, 1, 2]]], ignore_index=True)

# TODO: Write your code here
# TODO: اكتب الكود الخاص بك هنا

# Task 1: Load and explore the data
print("Task 1: Explore the data")
# Your code here...

# Task 2: Handle missing values
print("\nTask 2: Handle missing values")
# Your code here...

# Task 3: Remove duplicates
print("\nTask 3: Remove duplicates")
# Your code here...

# Task 4: Create visualizations
print("\nTask 4: Create visualizations")
# Your code here...

print("\nExercise 1 Complete!")
print("اكتمل التمرين 1!")

