# Quiz 1: Data Processing Basics
## اختبار 1: أساسيات معالجة البيانات

**Time Limit:** 30 minutes | **Marks:** 30 points

---

## Part 1: Multiple Choice (10 points)

### Question 1 (2 points)
What does `df.isnull().sum()` return?
- A) The total number of missing values in the dataframe
- B) A series showing missing values per column
- C) A boolean dataframe
- D) None of the above

**Answer:** B

---

### Question 2 (2 points)
Which method removes duplicate rows in pandas?
- A) `df.remove_duplicates()`
- B) `df.drop_duplicates()`
- C) `df.unique()`
- D) `df.deduplicate()`

**Answer:** B

---

### Question 3 (2 points)
What does StandardScaler do?
- A) Scales features to range [0, 1]
- B) Scales features to have mean=0 and std=1
- C) Normalizes features using min-max
- D) Removes outliers

**Answer:** B

---

### Question 4 (2 points)
When should you use Label Encoding vs One-Hot Encoding?
- A) Label Encoding for ordinal, One-Hot for nominal
- B) Label Encoding for nominal, One-Hot for ordinal
- C) Both work the same way
- D) Only use One-Hot Encoding

**Answer:** A

---

### Question 5 (2 points)
What is the purpose of train_test_split?
- A) To split data into training and testing sets
- B) To shuffle the data
- C) To remove missing values
- D) To scale the data

**Answer:** A

---

## Part 2: Code Writing (10 points)

### Question 6 (5 points)
Write Python code to:
1. Load a CSV file named "data.csv"
2. Display basic information about the dataset
3. Check for missing values
4. Fill missing values in numeric columns with the mean

**Answer:**
```python
import pandas as pd
import numpy as np

# Load CSV
df = pd.read_csv('data.csv')

# Display basic info
print(df.info())
print(df.describe())

# Check missing values
print(df.isnull().sum())

# Fill missing values in numeric columns
numeric_cols = df.select_dtypes(include=[np.number]).columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
```

---

### Question 7 (5 points)
Write code to:
1. Create a StandardScaler
2. Fit it on training data X_train
3. Transform both X_train and X_test

**Answer:**
```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

---

## Part 3: Short Answer (10 points)

### Question 8 (5 points)
Explain the difference between standardization and normalization. When would you use each?

**Answer:**
- **Standardization (Z-score normalization):** Transforms data to have mean=0 and std=1. Formula: (x - mean) / std. Use when data has outliers or follows normal distribution.
- **Normalization (Min-Max scaling):** Transforms data to range [0, 1]. Formula: (x - min) / (max - min). Use when you need bounded range or data doesn't follow normal distribution.

---

### Question 9 (5 points)
What is multicollinearity? Why is it a problem in machine learning?

**Answer:**
Multicollinearity occurs when features are highly correlated with each other. Problems:
1. Makes model coefficients unstable
2. Reduces interpretability
3. Can cause overfitting
4. Makes it hard to determine individual feature importance

Solutions: Remove correlated features, use regularization (Ridge/Lasso), or use PCA.

---

## Answer Key

**Part 1:**
1. B - 2 points
2. B - 2 points
3. B - 2 points
4. A - 2 points
5. A - 2 points

**Part 2:**
6. Full code with all steps - 5 points
7. Correct scaler usage - 5 points

**Part 3:**
8. Clear explanation of both - 5 points
9. Definition + problems + solutions - 5 points

**Total: 30 points**

---

## Grading Rubric

- **90-100% (27-30 points):** Excellent understanding
- **80-89% (24-26 points):** Good understanding
- **70-79% (21-23 points):** Satisfactory
- **60-69% (18-20 points):** Needs improvement
- **Below 60% (<18 points):** Requires additional study

