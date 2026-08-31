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
# HONEST NOTE: the full log is 663,522 calls / 123 MB and is NOT committed to this
# repository. load(..., prefer="sample") reads the 25,000-call copy that IS: 1 call
# in every 27, evenly spread, covering the same 2015-12-10 to 2020-07-29 window with
# all 100 call types and all 68 townships. Every COUNT you plot is therefore about a
# twenty-seventh of the county's real counts; every SHAPE - the seasonal swing, the
# hour-of-day cycle, the service mix, the missing-ZIP rate - is the real one.
# --- Data setup. Works from any folder, and on Google Colab. -------------------------
# WHAT: find the repository root and put it on sys.path, then import the shared loader.
# WHY:  a hard-coded '../../../Course 04/datasets/raw/titanic.csv' only resolves when the
#       working directory happens to be this file's folder. This does not care, and the
#       datasets themselves are not committed - the loader fetches or samples them for you.
import sys, pathlib

_here = (pathlib.Path(__file__).resolve().parent if "__file__" in globals()
         else pathlib.Path.cwd().resolve())
_root = next((p for p in [_here, *_here.parents] if (p / "tools" / "data.py").exists()), None)
if _root is None:                     # Google Colab, or a stray copy of this file
    import urllib.request
    pathlib.Path("tools").mkdir(exist_ok=True)
    try:
        urllib.request.urlretrieve(
            "https://raw.githubusercontent.com/A-Alwabel/"
            "AI-Diploma-Program/main/tools/data.py", "tools/data.py")
    except Exception as _e:
        raise RuntimeError(
            "Could not find the AI Diploma repository from this folder, and could not "
            "download the data loader either. Run this file inside a clone of "
            "https://github.com/A-Alwabel/AI-Diploma-Program, or connect to the internet "
            f"and run it again. (underlying error: {_e})") from None
    _root = pathlib.Path.cwd()
sys.path.insert(0, str(_root))

from tools.data import load
# -------------------------------------------------------------------------------------

calls = load("montgomery_911_calls", prefer="sample",
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
