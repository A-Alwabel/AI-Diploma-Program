# Quiz 2: Data Cleaning and Preparation

**Time Limit:** 30 minutes | **Marks:** 30 points

---

## Part 1: Multiple Choice (10 points)

### Question 1 (2 points)
What is the best strategy for handling missing values in a dataset?
- A) Always drop rows with missing values
- B) Always fill with mean/median
- C) Depends on the data and context
- D) Always use forward fill

---

### Question 2 (2 points)
What does `df.duplicated()` return?
- A) A DataFrame with duplicate rows removed
- B) A boolean Series indicating duplicate rows
- C) The number of duplicate rows
- D) A list of duplicate indices

---

### Question 3 (2 points)
What is an outlier?
- A) A data point that significantly differs from other observations
- B) A missing value
- C) A duplicate row
- D) A column with wrong data type

---

### Question 4 (2 points)
Which method is commonly used to detect outliers?
- A) One-hot encoding
- B) Mean imputation
- C) Label encoding
- D) IQR (Interquartile Range) method

---

### Question 5 (2 points)
What does normalization do?
- A) Removes missing values
- B) Removes duplicates
- C) Scales data to a specific range (usually 0-1)
- D) Changes data types

---

## Part 2: Code Writing (10 points)

### Question 6 (5 points)
Write Python code to:
1. Load a CSV file
2. Check for missing values
3. Fill missing values in numeric columns with median
4. Remove duplicate rows

```python
import pandas as pd

# Load CSV
df = pd.read_csv('data.csv')

# Check missing values
print(df.isnull().sum())

# Fill missing values in numeric columns with median
numeric_cols = df.select_dtypes(include=['number']).columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())

# Remove duplicates
df = df.drop_duplicates()

print(df.info())
```

---

### Question 7 (5 points)
Write code to detect and handle outliers using IQR method:
1. Calculate Q1, Q3, and IQR
2. Define outlier boundaries
3. Remove outliers from a specific column

```python
import pandas as pd
import numpy as np

# Assuming df and column_name are defined
Q1 = df[column_name].quantile(0.25)
Q3 = df[column_name].quantile(0.75)
IQR = Q3 - Q1

# Define boundaries
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Remove outliers
df_clean = df[(df[column_name] >= lower_bound) & (df[column_name] <= upper_bound)]
```

---

## Part 3: Short Answer (10 points)

### Question 8 (5 points)
Explain different strategies for handling missing values. When would you use each?

**Strategies:**
1. **Deletion**: Drop rows/columns with missing values
   - Use when: Missing data is <5% and random
   
2. **Mean/Median/Mode Imputation**: Fill with central tendency
   - Use when: Data is normally distributed (mean) or has outliers (median)
   
3. **Forward Fill / Backward Fill**: Use previous/next value
   - Use when: Time series data with temporal patterns
   
4. **Interpolation**: Estimate based on surrounding values
   - Use when: Ordered data with patterns
   
5. **Predictive Imputation**: Use ML models to predict missing values
   - Use when: Significant missing data and strong relationships exist

---

### Question 9 (5 points)
What are the main steps in data cleaning? Why is it important?

**Main Steps:**
1. **Handle Missing Values**: Identify and treat missing data
2. **Remove Duplicates**: Eliminate duplicate records
3. **Detect and Handle Outliers**: Identify and treat anomalies
4. **Fix Data Types**: Ensure correct data types
5. **Standardize Formats**: Consistent naming, date formats, etc.
6. **Validate Data**: Check for logical inconsistencies

**Importance:**
- "Garbage in, garbage out" - poor data quality leads to poor models
- Improves model accuracy and reliability
- Reduces bias and errors in analysis
- Ensures data consistency and usability
- Critical for production ML systems

---

## Grading Rubric

- **90-100% (27-30 points):** Excellent understanding
- **80-89% (24-26 points):** Good understanding
- **70-79% (21-23 points):** Satisfactory
- **60-69% (18-20 points):** Needs improvement
- **Below 60% (<18 points):** Requires additional study
