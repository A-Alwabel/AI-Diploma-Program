"""
Unit 3 - Exercise 1: Solution
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['axes.unicode_minus'] = False
sns.set_style("whitegrid")

# Sample data
np.random.seed(42)
data = {
    'month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'sales': [1200, 1500, 1800, 1600, 2000, 2200],
    'region': np.random.choice(['North', 'South', 'East', 'West'], 6),
    'product': np.random.choice(['A', 'B', 'C'], 6),
    'rating': np.random.uniform(3, 5, 6)
}
df = pd.DataFrame(data)

advanced_data = pd.DataFrame({
    'x': np.random.randn(100),
    'y': np.random.randn(100),
    'category': np.random.choice(['Type1', 'Type2', 'Type3'], 100),
    'value': np.random.uniform(10, 100, 100)
})

# Task 1: Basic plots
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.plot(df['month'], df['sales'], marker='o', linewidth=2)
plt.title('Sales Over Months')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True, alpha=0.3)

plt.subplot(1, 3, 2)
region_sales = df.groupby('region')['sales'].sum()
plt.bar(region_sales.index, region_sales.values, color='steelblue')
plt.title('Sales by Region')
plt.xlabel('Region')
plt.ylabel('Sales')
plt.xticks(rotation=45)

plt.subplot(1, 3, 3)
plt.scatter(advanced_data['x'], advanced_data['y'], alpha=0.6)
plt.title('Scatter Plot')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('unit3-visualization/examples/task1_basic.png', dpi=150)
plt.close()

# Task 2: Statistical plots
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

sns.histplot(advanced_data['value'], kde=True, ax=axes[0])
axes[0].set_title('Distribution Plot')

sns.boxplot(data=advanced_data, x='category', y='value', ax=axes[1])
axes[1].set_title('Box Plot by Category')

corr = advanced_data[['x', 'y', 'value']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', ax=axes[2])
axes[2].set_title('Correlation Heatmap')

plt.tight_layout()
plt.savefig('unit3-visualization/examples/task2_statistical.png', dpi=150)
plt.close()

# Task 3: Customization
plt.figure(figsize=(10, 6))
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A']
bars = plt.bar(df['month'], df['sales'], color=colors, alpha=0.8, edgecolor='black')
plt.title('Monthly Sales - Customized', fontsize=16, fontweight='bold')
plt.xlabel('Month', fontsize=12)
plt.ylabel('Sales ($)', fontsize=12)
plt.grid(True, alpha=0.3, axis='y')
plt.legend(['Sales'], loc='upper left')
for i, v in enumerate(df['sales']):
    plt.text(i, v + 50, str(v), ha='center', va='bottom')
plt.tight_layout()
plt.savefig('unit3-visualization/examples/task3_customized.png', dpi=150)
plt.close()

# Task 4: Multiple subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

axes[0, 0].plot(df['month'], df['sales'], marker='o', color='blue')
axes[0, 0].set_title('Line Plot')
axes[0, 0].grid(True, alpha=0.3)

axes[0, 1].bar(df['region'], df.groupby('region')['sales'].sum(), color='green')
axes[0, 1].set_title('Bar Chart')
axes[0, 1].tick_params(axis='x', rotation=45)

axes[1, 0].scatter(advanced_data['x'], advanced_data['y'], c=advanced_data['value'], cmap='viridis', alpha=0.6)
axes[1, 0].set_title('Scatter Plot')
axes[1, 0].set_xlabel('X')
axes[1, 0].set_ylabel('Y')

sns.violinplot(data=advanced_data, x='category', y='value', ax=axes[1, 1])
axes[1, 1].set_title('Violin Plot')

fig.suptitle('Multiple Visualizations', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig('unit3-visualization/examples/task4_subplots.png', dpi=150)
plt.close()

print("All visualizations created and saved!")

