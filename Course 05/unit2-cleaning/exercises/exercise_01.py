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
# Montgomery County (Pennsylvania) 911 emergency call log - a public dataset,
# covering 2015-12-10 to 2020-07-29.
#
# Nothing below was planted. This data arrives with:
#   - missing values in 'zip' (about 12% of calls) and a few in 'twp'
#   - impossible coordinates (a handful of calls placed outside Pennsylvania)
#
# HONEST NOTE about duplicates. The full 663,522-call log is 123 MB and is NOT
# committed to this repository; load() below reads the 25,000-call sample that IS,
# which keeps 1 call in every 27. The full file's first 100,000 rows contain 37
# exact duplicate rows; the sample contains ZERO, because thinning 1-in-27 almost
# never keeps both copies of a duplicated call. Task 3 below is written around
# that fact rather than pretending otherwise. Put the full file in
# Course 04/datasets/raw/ and pass prefer="full" if you want to meet the real ones.
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

df = load("montgomery_911_calls", prefer="sample")

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
# - Count fully identical rows with df.duplicated(). Expect ZERO here, and read the
#   HONEST NOTE at the top of this file before you conclude the data is clean:
#   "no duplicates in this sample" is not the same claim as "no duplicates in the log"
# - Count duplicates on the key ['timeStamp', 'addr', 'title'] instead. Also zero.
#   Write one sentence on what a zero result does and does not prove
# - Say what you would do differently if this were a real hand-off and you needed to
#   know the duplicate rate: which file would you have to obtain, and why
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

