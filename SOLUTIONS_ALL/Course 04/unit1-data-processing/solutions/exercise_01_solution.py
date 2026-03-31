"""
Unit 1 - Exercise 1: Solution
أساليب معالجة البيانات - تمرين 1: الحل

Complete solution for the data processing exercise
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("=" * 60)
print("Exercise 1: Solution")
print("تمرين 1: الحل")
print("=" * 60)

# Sample dataset - Sales data
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

# Task 1: Load and explore the data
print("\n" + "=" * 60)
print("Task 1: Explore the data")
print("المهمة 1: استكشاف البيانات")
print("=" * 60)

print(f"\nData Shape: {df.shape}")
print(f"الصفوف: {df.shape[0]}, الأعمدة: {df.shape[1]}")

print("\nFirst 10 rows:")
print(df.head(10))

print("\nData Info:")
print(df.info())

print("\nDescriptive Statistics:")
print(df.describe())

print("\nMissing Values:")
missing = df.isnull().sum()
print(missing[missing > 0])

print("\nDuplicates:")
duplicates = df.duplicated().sum()
print(f"Number of duplicates: {duplicates}")

# Task 2: Handle missing values
print("\n" + "=" * 60)
print("Task 2: Handle missing values")
print("المهمة 2: معالجة القيم المفقودة")
print("=" * 60)

# Fill numeric columns with mean
df_clean = df.copy()

# Fill customer_rating with mean
df_clean['customer_rating'].fillna(df_clean['customer_rating'].mean(), inplace=True)

# Fill price with mean
df_clean['price'].fillna(df_clean['price'].mean(), inplace=True)

print("\nMissing values after handling:")
print(df_clean.isnull().sum().sum(), "missing values remaining")

# Task 3: Remove duplicates
print("\n" + "=" * 60)
print("Task 3: Remove duplicates")
print("المهمة 3: إزالة التكرارات")
print("=" * 60)

print(f"Rows before removing duplicates: {df_clean.shape[0]}")
df_clean = df_clean.drop_duplicates()
print(f"Rows after removing duplicates: {df_clean.shape[0]}")

# Task 4: Create visualizations
print("\n" + "=" * 60)
print("Task 4: Create visualizations")
print("المهمة 4: إنشاء التصورات")
print("=" * 60)

# Visualization 1: Distribution of prices
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.hist(df_clean['price'], bins=20, edgecolor='black', alpha=0.7, color='skyblue')
plt.xlabel('Price ($)')
plt.ylabel('Frequency')
plt.title('Distribution of Product Prices')
plt.grid(True, alpha=0.3)

# Visualization 2: Category distribution
plt.subplot(1, 2, 2)
category_counts = df_clean['category'].value_counts()
plt.bar(category_counts.index, category_counts.values, color='coral')
plt.xlabel('Category')
plt.ylabel('Count')
plt.title('Products by Category')
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig('exercise_01_visualization_1.png', dpi=300, bbox_inches='tight')
print("\n✓ Saved visualization 1: 'exercise_01_visualization_1.png'")
plt.close()

# Visualization 3: Price vs Quantity Sold
plt.figure(figsize=(10, 6))
plt.scatter(df_clean['price'], df_clean['quantity_sold'], alpha=0.6, s=50)
plt.xlabel('Price ($)')
plt.ylabel('Quantity Sold')
plt.title('Price vs Quantity Sold')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('exercise_01_visualization_2.png', dpi=300, bbox_inches='tight')
print("✓ Saved visualization 2: 'exercise_01_visualization_2.png'")
plt.close()

# Visualization 4: Customer Rating by Category
plt.figure(figsize=(10, 6))
df_clean.boxplot(column='customer_rating', by='category', grid=True)
plt.xlabel('Category')
plt.ylabel('Customer Rating')
plt.title('Customer Rating Distribution by Category')
plt.suptitle('')  # Remove default title
plt.tight_layout()
plt.savefig('exercise_01_visualization_3.png', dpi=300, bbox_inches='tight')
print("✓ Saved visualization 3: 'exercise_01_visualization_3.png'")
plt.close()

print("\n" + "=" * 60)
print("Exercise 1 Solution Complete! ✓")
print("اكتمل حل التمرين 1! ✓")
print("=" * 60)

