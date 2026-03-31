"""
Unit 1 - Exercise 1: Solution
تمرين 1: الحل

Complete solution for the data science fundamentals exercise
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configure matplotlib
plt.rcParams['axes.unicode_minus'] = False
sns.set_style("whitegrid")

print("=" * 60)
print("Exercise 1: Solution")
print("تمرين 1: الحل")
print("=" * 60)

# Sample dataset
np.random.seed(42)
data = {
    'student_id': range(1, 101),
    'student_name': [f'Student_{i}' for i in range(1, 101)],
    'age': np.random.randint(18, 25, 100),
    'math_score': np.random.uniform(50, 100, 100),
    'science_score': np.random.uniform(50, 100, 100),
    'english_score': np.random.uniform(50, 100, 100),
    'attendance': np.random.uniform(60, 100, 100),
    'study_hours': np.random.uniform(5, 40, 100),
    'department': np.random.choice(['CS', 'Engineering', 'Business', 'Arts', 'Science'], 100)
}

df = pd.DataFrame(data)

# Task 1: Explore the data
print("\n" + "=" * 60)
print("Task 1: Explore the data")
print("=" * 60)

print(f"\nData Shape: {df.shape}")
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

print("\nFirst 5 rows:")
print(df.head())

print("\nData Info:")
print(df.info())

print("\nDescriptive Statistics:")
print(df.describe())

# Task 2: Statistical Analysis
print("\n" + "=" * 60)
print("Task 2: Statistical Analysis")
print("=" * 60)

score_columns = ['math_score', 'science_score', 'english_score']
print("\nMean scores:")
print(df[score_columns].mean())

print("\nMedian scores:")
print(df[score_columns].median())

print("\nStandard deviation:")
print(df[score_columns].std())

print("\nCorrelation between scores:")
correlation = df[score_columns].corr()
print(correlation)

print("\nAverage scores by department:")
dept_avg = df.groupby('department')[score_columns].mean()
print(dept_avg)

# Task 3: Data Filtering
print("\n" + "=" * 60)
print("Task 3: Data Filtering")
print("=" * 60)

high_math = df[df['math_score'] > 80]
print(f"\nStudents with math_score > 80: {len(high_math)}")
print(high_math[['student_name', 'math_score', 'department']].head())

cs_students = df[df['department'] == 'CS']
print(f"\nCS Department students: {len(cs_students)}")
print(cs_students[['student_name', 'department', 'math_score']].head())

high_attendance = df[df['attendance'] > 90]
print(f"\nStudents with attendance > 90: {len(high_attendance)}")
print(high_attendance[['student_name', 'attendance', 'department']].head())

# Task 4: Create Visualizations
print("\n" + "=" * 60)
print("Task 4: Create Visualizations")
print("=" * 60)

# Create figure with subplots
fig, axes = plt.subplots(2, 2, figsize=(15, 12))

# Histogram of math scores
axes[0, 0].hist(df['math_score'], bins=20, edgecolor='black', alpha=0.7)
axes[0, 0].set_title('Distribution of Math Scores', fontsize=12)
axes[0, 0].set_xlabel('Math Score')
axes[0, 0].set_ylabel('Frequency')
axes[0, 0].grid(True, alpha=0.3)

# Scatter plot: study_hours vs math_score
axes[0, 1].scatter(df['study_hours'], df['math_score'], alpha=0.6)
axes[0, 1].set_title('Study Hours vs Math Score', fontsize=12)
axes[0, 1].set_xlabel('Study Hours')
axes[0, 1].set_ylabel('Math Score')
axes[0, 1].grid(True, alpha=0.3)

# Bar chart: average score by department
dept_avg_scores = df.groupby('department')['math_score'].mean().sort_values(ascending=False)
axes[1, 0].bar(dept_avg_scores.index, dept_avg_scores.values, color='steelblue', alpha=0.7)
axes[1, 0].set_title('Average Math Score by Department', fontsize=12)
axes[1, 0].set_xlabel('Department')
axes[1, 0].set_ylabel('Average Math Score')
axes[1, 0].tick_params(axis='x', rotation=45)
axes[1, 0].grid(True, alpha=0.3, axis='y')

# Correlation heatmap
im = axes[1, 1].imshow(correlation, cmap='coolwarm', aspect='auto', vmin=-1, vmax=1)
axes[1, 1].set_xticks(range(len(score_columns)))
axes[1, 1].set_yticks(range(len(score_columns)))
axes[1, 1].set_xticklabels(score_columns, rotation=45, ha='right')
axes[1, 1].set_yticklabels(score_columns)
axes[1, 1].set_title('Score Correlation Heatmap', fontsize=12)
plt.colorbar(im, ax=axes[1, 1])

plt.tight_layout()
plt.savefig('unit1-introduction/examples/exercise_01_visualizations.png', dpi=150, bbox_inches='tight')
print("\nVisualizations saved to: exercise_01_visualizations.png")
plt.show()

# Task 5: Data Aggregation
print("\n" + "=" * 60)
print("Task 5: Data Aggregation")
print("=" * 60)

# Group by department and calculate mean scores
dept_stats = df.groupby('department').agg({
    'math_score': 'mean',
    'science_score': 'mean',
    'english_score': 'mean',
    'study_hours': 'sum'
}).round(2)

print("\nDepartment Statistics:")
print(dept_stats)

# Department with highest average math score
best_dept = df.groupby('department')['math_score'].mean().idxmax()
best_score = df.groupby('department')['math_score'].mean().max()
print(f"\nDepartment with highest average math score: {best_dept} ({best_score:.2f})")

# Total study hours per department
total_hours = df.groupby('department')['study_hours'].sum()
print("\nTotal study hours per department:")
print(total_hours)

print("\n" + "=" * 60)
print("Solution Complete!")
print("اكتمل الحل!")
print("=" * 60)

