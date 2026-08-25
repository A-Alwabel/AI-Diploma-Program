"""
Unit 2 - Exercise 1: Data Cleaning Practice
تمرين 1: ممارسة تنظيف البيانات

Instructions:
1. Load the real dataset (provided below)
2. Identify and handle missing values
3. Detect and remove duplicates
4. Identify and handle outliers
5. Transform and normalize data
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

plt.rcParams['axes.unicode_minus'] = False
sns.set_style("whitegrid")

# Real dataset with real issues
# ---------------------------------------------------------------------------
# Montgomery County (Pennsylvania) 911 emergency call log - a public dataset.
# We read the first 100,000 calls so the exercise runs in seconds. That slice is
# a contiguous window of real history, not a random sample, so the duplicate
# records the dispatch system produced are preserved.
#
# Nothing below was planted. This file arrives with:
#   - missing values in 'zip' and 'twp'
#   - exact duplicate rows (the same call written twice)
#   - impossible coordinates (a handful of calls placed outside Pennsylvania)
DATA_DIR = '../../../Course 04/datasets/raw/'

df = pd.read_csv(DATA_DIR + 'montgomery_911_calls.csv', nrows=100_000)

# One parsing step you need before any time-based task:
df['timeStamp'] = pd.to_datetime(df['timeStamp'])

# The 'title' column looks like "EMS: BACK PAINS/INJURY" - the part before the
# colon is the emergency category.
df['category'] = df['title'].str.split(':').str[0]

print(f"Loaded {len(df):,} real 911 calls, {df.shape[1]} columns")
print(f"Covering {df['timeStamp'].min():%Y-%m-%d} to {df['timeStamp'].max():%Y-%m-%d}")

# TODO: Write your code here
# TODO: اكتب الكود الخاص بك هنا

# Task 1: Identify missing values
print("=" * 60)
print("Task 1: Identify Missing Values")
print("=" * 60)
# Your code here...
# - Count missing values per column (and as a percentage of rows)
# - Visualize the missing-value pattern (seaborn heatmap of df.isnull())
# - Ask WHY 'zip' is missing so much more often than 'twp'

# Task 2: Handle missing values
print("\n" + "=" * 60)
print("Task 2: Handle Missing Values")
print("=" * 60)
# Your code here...
# - Fill missing 'twp' with the most common township (mode)
# - Decide what to do about 'zip': it is missing for ~12% of calls.
#   Is a filled-in ZIP code useful, or is a "zip_missing" flag more honest?
# - Justify your choice in a comment - there is no single right answer

# Task 3: Detect and remove duplicates
print("\n" + "=" * 60)
print("Task 3: Handle Duplicates")
print("=" * 60)
# Your code here...
# - Count fully identical rows with df.duplicated()
# - Count duplicates on the key ['timeStamp', 'addr', 'title'] instead
# - Remove the exact duplicates and verify the count dropped
# - Explain why the two numbers differ

# Task 4: Identify outliers
print("\n" + "=" * 60)
print("Task 4: Identify Outliers")
print("=" * 60)
# Your code here...
# - Use the IQR method to find outliers in 'lat'
# - Use the Z-score method to find outliers in 'lng'
# - Visualize both with box plots
# - Montgomery County sits near latitude 40.1 N, longitude -75.3 W

# Task 5: Handle outliers and invalid values
print("\n" + "=" * 60)
print("Task 5: Handle Outliers")
print("=" * 60)
# Your code here...
# - Flag calls whose coordinates fall outside the county
#   (lat < 39.9 or lat > 40.5, lng < -75.8 or lng > -74.9)
# - Decide: drop them, or keep them with a flag? Say why.
# - Verify how many rows your decision affects

# Task 6: Data transformation
print("\n" + "=" * 60)
print("Task 6: Data Transformation")
print("=" * 60)
# Your code here...
# - Normalize 'lat' using Min-Max scaling
# - Standardize 'lng' using Z-score
# - Create a new feature: hour = df['timeStamp'].dt.hour
# - Then count calls per hour: when is the county busiest?

print("\n" + "=" * 60)
print("Exercise 1 Complete!")
print("=" * 60)

