"""
Unit 2 - Exercise 1: Solution
تمرين 1: الحل
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

plt.rcParams['axes.unicode_minus'] = False
sns.set_style("whitegrid")

print("=" * 60)
print("Exercise 1: Solution")
print("=" * 60)

# Sample dataset
np.random.seed(42)
data = {
    'id': range(1, 201),
    'name': [f'Item_{i}' for i in range(1, 201)],
    'price': np.random.uniform(10, 1000, 200),
    'quantity': np.random.randint(1, 100, 200),
    'category': np.random.choice(['A', 'B', 'C', 'D'], 200),
    'rating': np.random.uniform(1, 5, 200),
    'date': pd.date_range('2023-01-01', periods=200, freq='D')
}

df = pd.DataFrame(data)

# Introduce issues
df.loc[10:20, 'price'] = np.nan
df.loc[50:55, 'rating'] = np.nan
df.loc[100:105, 'quantity'] = np.nan
df = pd.concat([df, df.iloc[[0, 1, 2, 10, 11]]], ignore_index=True)
df.loc[150, 'price'] = 50000
df.loc[160, 'quantity'] = -10

# Task 1: Identify missing values
print("\n" + "=" * 60)
print("Task 1: Identify Missing Values")
print("=" * 60)

missing = df.isnull().sum()
print("\nMissing values per column:")
print(missing[missing > 0])

# Visualize missing values
plt.figure(figsize=(10, 6))
sns.heatmap(df.isnull(), cbar=True, yticklabels=False, cmap='viridis')
plt.title('Missing Values Pattern')
plt.tight_layout()
plt.savefig('unit2-cleaning/examples/missing_values.png', dpi=150)
plt.close()

# Task 2: Handle missing values
print("\n" + "=" * 60)
print("Task 2: Handle Missing Values")
print("=" * 60)

df['price'].fillna(df['price'].median(), inplace=True)
df['rating'].fillna(df['rating'].mean(), inplace=True)
df['quantity'].fillna(method='ffill', inplace=True)

print("\nMissing values after handling:")
print(df.isnull().sum().sum())

# Task 3: Handle duplicates
print("\n" + "=" * 60)
print("Task 3: Handle Duplicates")
print("=" * 60)

duplicates = df.duplicated().sum()
print(f"\nNumber of duplicates: {duplicates}")

df = df.drop_duplicates()
print(f"Rows after removing duplicates: {len(df)}")

# Task 4: Identify outliers
print("\n" + "=" * 60)
print("Task 4: Identify Outliers")
print("=" * 60)

# IQR method for price
Q1 = df['price'].quantile(0.25)
Q3 = df['price'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

price_outliers = df[(df['price'] < lower_bound) | (df['price'] > upper_bound)]
print(f"\nPrice outliers (IQR method): {len(price_outliers)}")

# Z-score method for quantity
z_scores = np.abs(stats.zscore(df['quantity']))
quantity_outliers = df[z_scores > 3]
print(f"Quantity outliers (Z-score method): {len(quantity_outliers)}")

# Visualize
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
axes[0].boxplot(df['price'])
axes[0].set_title('Price Distribution')
axes[1].boxplot(df['quantity'])
axes[1].set_title('Quantity Distribution')
plt.tight_layout()
plt.savefig('unit2-cleaning/examples/outliers.png', dpi=150)
plt.close()

# Task 5: Handle outliers
print("\n" + "=" * 60)
print("Task 5: Handle Outliers")
print("=" * 60)

# Cap price outliers
df.loc[df['price'] > upper_bound, 'price'] = upper_bound
df.loc[df['price'] < lower_bound, 'price'] = lower_bound

# Handle invalid values
df.loc[df['quantity'] < 0, 'quantity'] = 0

print("\nData quality check:")
print(f"Price range: {df['price'].min():.2f} - {df['price'].max():.2f}")
print(f"Quantity range: {df['quantity'].min()} - {df['quantity'].max()}")

# Task 6: Data transformation
print("\n" + "=" * 60)
print("Task 6: Data Transformation")
print("=" * 60)

# Min-Max normalization
from sklearn.preprocessing import MinMaxScaler, StandardScaler

scaler_minmax = MinMaxScaler()
df['price_normalized'] = scaler_minmax.fit_transform(df[['price']])

# Z-score standardization
scaler_std = StandardScaler()
df['rating_standardized'] = scaler_std.fit_transform(df[['rating']])

# New feature
df['total_value'] = df['price'] * df['quantity']

print("\nTransformation complete!")
print(f"Price normalized range: {df['price_normalized'].min():.3f} - {df['price_normalized'].max():.3f}")
print(f"Rating standardized mean: {df['rating_standardized'].mean():.3f}, std: {df['rating_standardized'].std():.3f}")

print("\n" + "=" * 60)
print("Solution Complete!")
print("=" * 60)

