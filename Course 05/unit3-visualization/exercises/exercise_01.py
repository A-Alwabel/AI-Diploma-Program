"""
Unit 3 - Exercise 1: Data Visualization Practice

Instructions:
1. Create various types of visualizations
2. Customize plots with labels, colors, and styles
3. Create statistical visualizations
4. Create interactive visualizations (optional)
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['axes.unicode_minus'] = False
sns.set_style("whitegrid")

# Real dataset
# ---------------------------------------------------------------------------
# Montgomery County (Pennsylvania) 911 emergency call log - a public dataset of
# every call dispatched between December 2015 and July 2020. Nothing here was
# generated: the categories, the volumes, the missing ZIP codes and the seasonal
# swings are all real, which is exactly what makes the charts worth reading.
#
# `df`       : monthly call volume per service (EMS / Fire / Traffic)
# `calls`    : the full call-level table, for distribution and correlation plots
# ---------------------------------------------------------------------------
DATA_DIR = '../../../Course 04/datasets/raw/'

calls = pd.read_csv(DATA_DIR + 'montgomery_911_calls.csv',
                    usecols=['lat', 'lng', 'zip', 'title', 'timeStamp', 'twp'],
                    parse_dates=['timeStamp'])

# 'title' looks like 'EMS: BACK PAINS/INJURY' - split it into service and reason.
calls['service'] = calls['title'].str.split(':').str[0]
calls['reason'] = calls['title'].str.split(': ').str[1].str.strip()
calls['hour'] = calls['timeStamp'].dt.hour
calls['month'] = calls['timeStamp'].dt.to_period('M').dt.to_timestamp()

print(f"Loaded {len(calls):,} real 911 calls "
      f"({calls['timeStamp'].min():%Y-%m-%d} to {calls['timeStamp'].max():%Y-%m-%d})")
print(f"Services: {calls['service'].value_counts().to_dict()}")
print(f"Missing ZIP codes (real gaps): {calls['zip'].isna().sum():,}")

# Monthly volume per service - a tidy table for line and bar charts.
df = (calls.groupby(['month', 'service']).size()
      .reset_index(name='calls'))

# A 2,000-call sample keeps scatter plots readable. Sampling is legitimate
# randomness: the DATA is real, only WHICH rows we draw is random.
sample = calls.sample(n=2000, random_state=42)

# TODO: Write your code here

# Task 1: Basic matplotlib plots
print("=" * 60)
print("Task 1: Basic Plots")
print("=" * 60)
# Your code here...
# - Create a line plot of total monthly call volume over time (use `df`)
# - Create a bar chart of total calls by township (top 10, use `calls['twp']`)
# - Create a scatter plot of incident longitude vs latitude (use `sample`)

# Task 2: Seaborn statistical plots
print("\n" + "=" * 60)
print("Task 2: Statistical Plots")
print("=" * 60)
# Your code here...
# - Create a distribution plot (histogram + KDE) of 'hour' - when do people call?
# - Create a box plot of monthly 'calls' by 'service' (use `df`)
# - Create a correlation heatmap of a month-by-service pivot table

# Task 3: Customization
print("\n" + "=" * 60)
print("Task 3: Plot Customization")
print("=" * 60)
# Your code here...
# - Create a customized bar chart of the 10 most common call reasons
# - Add grid, legend, and proper axis labels (state the date range in the title)
# - Save the plot as PNG

# Task 4: Multiple subplots
print("\n" + "=" * 60)
print("Task 4: Multiple Subplots")
print("=" * 60)
# Your code here...
# - Create a figure with 2x2 subplots
# - Plot four different views of the same log (where / when / what / who)
# - Add overall title

print("\n" + "=" * 60)
print("Exercise 1 Complete!")
print("=" * 60)
