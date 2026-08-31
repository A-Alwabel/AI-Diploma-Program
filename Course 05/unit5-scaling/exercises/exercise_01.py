"""
Unit 5 - Exercise 1: Extending the Scope of Data Science

Instructions:
1. Work with large datasets using chunking
2. Optimize data processing
3. Use Dask for distributed computing (if available)
4. Profile and optimize code performance
"""

import pandas as pd
import numpy as np
import time
import os
import matplotlib.pyplot as plt

# Real large dataset
# ---------------------------------------------------------------------------
# CICIDS2017: a 708 MB packet-capture summary from the Canadian Institute for
# Cybersecurity - 2,300,825 real network flows recorded over five days, each
# with 79 statistics and an attack label.
#
# We do NOT load it whole. `LARGE_FILE` is the path; every task below streams
# it. That is the entire point of this unit: the file is bigger than the
# comfortable working set, and it is real.
#
# Real defects you will meet: column names carry leading spaces, and the
# flow-rate columns contain infinities produced by zero-duration flows.
# ---------------------------------------------------------------------------
# HONEST NOTE: the full 708 MB / 2,300,825-flow capture is NOT committed to this
# repository. dataset_path(..., prefer="sample") returns the 14,015-flow copy that
# IS - stratified by Label, so all 15 attack classes survive. The code below is
# unchanged for the full file: put cicids2017.csv in Course 04/datasets/raw/ and
# drop the prefer= argument. CHUNK_SIZE is scaled to the file you actually have,
# because chunking a 14,015-row file into 200,000-row chunks gives one chunk and
# teaches nothing.
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

from tools.data import load, path as dataset_path
# -------------------------------------------------------------------------------------

LARGE_FILE = dataset_path("cicids2017", prefer="sample")

USECOLS = [' Destination Port', ' Flow Duration', ' Total Fwd Packets',
           ' Total Backward Packets', ' Fwd Packet Length Mean',
           'Flow Bytes/s', ' Label']
CHUNK_SIZE = 1_500 if os.path.getsize(LARGE_FILE) < 50e6 else 200_000

print(f"Source file: {LARGE_FILE.name} ({os.path.getsize(LARGE_FILE) / 1e6:,.1f} MB on disk)")
print(f"Columns selected: {len(USECOLS)} of 79")
print(f"Chunk size: {CHUNK_SIZE:,} rows")

# A classroom-size in-memory slice, for the tasks that need one DataFrame.
large_data = pd.read_csv(LARGE_FILE, usecols=USECOLS, nrows=100_000)
large_data.columns = [c.strip() for c in large_data.columns]
print(f"\nIn-memory slice for profiling: {large_data.shape}")
print(large_data.head())
print(f"\nInfinite values in 'Flow Bytes/s' (real, from zero-duration flows): "
      f"{np.isinf(large_data['Flow Bytes/s']).sum()}")

# TODO: Write your code here

# Task 1: Process large dataset efficiently
print("=" * 60)
print("Task 1: Efficient Processing")
print("=" * 60)
# Your code here...
# - Stream LARGE_FILE with pd.read_csv(..., usecols=USECOLS, chunksize=CHUNK_SIZE)
# - Count the total rows without ever loading the file whole
# - Measure how long the full pass takes, and how many chunks it took

# Task 2: Data aggregation on large dataset
print("\n" + "=" * 60)
print("Task 2: Aggregation")
print("=" * 60)
# Your code here...
# - Group by 'Label' and compute the mean 'Flow Duration' across the WHOLE file
# - Carry a running SUM and COUNT per label, then divide at the end
#   (averaging the per-chunk means is wrong - the last chunk is smaller)
# - Compare your answer against a single-chunk estimate: how far off is it?

# Task 3: Memory optimization
print("\n" + "=" * 60)
print("Task 3: Memory Optimization")
print("=" * 60)
# Your code here...
# - Measure large_data.memory_usage(deep=True).sum()
# - Convert 'Label' to the 'category' dtype and downcast the numeric columns
# - Measure again and report the percentage saved
# - Handle the infinities in 'Flow Bytes/s' - and say what you chose to do

# Task 4: Distributed computing with Dask (optional)
print("\n" + "=" * 60)
print("Task 4: Dask (optional)")
print("=" * 60)
# Your code here...
# - import dask.dataframe as dd; ddf = dd.read_csv(LARGE_FILE, usecols=USECOLS)
# - Repeat the Task 2 aggregation with Dask and .compute()
# - Time BOTH the pandas end-to-end job and the Dask one, and report which won
#   (include the pandas read time - excluding it makes the comparison dishonest)

print("\n" + "=" * 60)
print("Exercise 1 Complete!")
print("=" * 60)
