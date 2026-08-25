"""
Unit 1 - Exercise 1: Data Science Fundamentals Practice
تمرين 1: ممارسة أساسيات علم البيانات

Instructions:
1. Load a sample dataset (provided below)
2. Explore the data using pandas operations
3. Perform basic statistical analysis
4. Create visualizations
5. Compare CPU (pandas) operations (optional: compare with cuDF if available)

Dataset: the Titanic passenger manifest (real data, real missing values)
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configure matplotlib for better display
plt.rcParams['axes.unicode_minus'] = False
sns.set_style("whitegrid")

# Real dataset - the Titanic passenger manifest
# 891 real passengers; Age, Cabin and Embarked have genuine gaps in the record.
DATA_DIR = '../../../Course 04/datasets/raw/'
df = pd.read_csv(DATA_DIR + 'titanic.csv')

# One derived column you will need below:
# family_size = siblings/spouses + parents/children + the passenger themselves.
df['family_size'] = df['SibSp'] + df['Parch'] + 1

# TODO: Write your code here
# TODO: اكتب الكود الخاص بك هنا

# Task 1: Explore the data
print("=" * 60)
print("Task 1: Explore the data")
print("المهمة 1: استكشاف البيانات")
print("=" * 60)
# Your code here...
# - Display first 5 rows
# - Display data shape
# - Display data info
# - Display descriptive statistics

# Task 2: Basic statistical analysis
print("\n" + "=" * 60)
print("Task 2: Statistical Analysis")
print("المهمة 2: التحليل الإحصائي")
print("=" * 60)
# Your code here...
# - Calculate mean, median, std for Age, Fare and family_size
# - Find correlation between Age, Fare, Pclass and Survived
# - Calculate average Fare and survival rate by Pclass

# Task 3: Data filtering and selection
print("\n" + "=" * 60)
print("Task 3: Data Filtering")
print("المهمة 3: تصفية البيانات")
print("=" * 60)
# Your code here...
# - Filter passengers with Fare > 100
# - Select passengers who boarded at Southampton (Embarked == 'S')
# - Find passengers older than 60, and count those with no recorded Age

# Task 4: Create visualizations
print("\n" + "=" * 60)
print("Task 4: Create Visualizations")
print("المهمة 4: إنشاء التصورات")
print("=" * 60)
# Your code here...
# - Create a histogram of Age (remember .dropna())
# - Create a scatter plot: Age vs Fare, coloured by Survived
# - Create a bar chart: survival rate by Pclass
# - Create a correlation heatmap of the numeric columns

# Task 5: Data aggregation
print("\n" + "=" * 60)
print("Task 5: Data Aggregation")
print("المهمة 5: تجميع البيانات")
print("=" * 60)
# Your code here...
# - Group by Pclass and calculate mean Age, Fare and Survived
# - Find which Pclass had the highest survival rate
# - Group by Sex and Pclass together and interpret the result

print("\n" + "=" * 60)
print("Exercise 1 Complete!")
print("اكتمل التمرين 1!")
print("=" * 60)

