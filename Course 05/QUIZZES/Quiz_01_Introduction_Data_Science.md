# Quiz 1: Introduction to Data Science
## اختبار 1: مقدمة في علم البيانات

**Time Limit:** 30 minutes | **Marks:** 30 points

---

## Part 1: Multiple Choice (10 points)

### Question 1 (2 points)
What is the main advantage of pandas DataFrame over Python lists?
- A) Faster iteration
- B) Built-in data manipulation and analysis tools
- C) Less memory usage
- D) Better for mathematical operations

---

### Question 2 (2 points)
What does `df.head()` return?
- A) The last 5 rows
- B) The first 5 rows
- C) A random sample of 5 rows
- D) Summary statistics

---

### Question 3 (2 points)
What is cuDF?
- A) A CPU-accelerated DataFrame library
- B) A GPU-accelerated DataFrame library
- C) A visualization library
- D) A machine learning library

---

### Question 4 (2 points)
What does `df.describe()` show?
- A) Data types of columns
- B) Summary statistics (count, mean, std, min, max, etc.)
- C) Missing values count
- D) Column names

---

### Question 5 (2 points)
Which NumPy function creates an array of zeros?
- A) `np.zeros()`
- B) `np.empty()`
- C) `np.ones()`
- D) `np.array()`

---

## Part 2: Code Writing (10 points)

### Question 6 (5 points)
Write Python code to:
1. Create a pandas DataFrame with columns: 'name', 'age', 'city'
2. Add 3 rows of sample data
3. Display the DataFrame
4. Show basic statistics

```python
import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'city': ['New York', 'London', 'Tokyo']
})

# Display DataFrame
print(df)

# Show basic statistics
print(df.describe())
```

---

### Question 7 (5 points)
Write code to:
1. Create a NumPy array with values [1, 2, 3, 4, 5]
2. Calculate the mean
3. Calculate the standard deviation
4. Reshape it to a 5x1 array

```python
import numpy as np

# Create array
arr = np.array([1, 2, 3, 4, 5])

# Calculate mean
mean = np.mean(arr)
print(f"Mean: {mean}")

# Calculate standard deviation
std = np.std(arr)
print(f"Std: {std}")

# Reshape
arr_reshaped = arr.reshape(5, 1)
print(arr_reshaped)
```

---

## Part 3: Short Answer (10 points)

### Question 8 (5 points)
Explain the data science lifecycle. What are the main stages?

The data science lifecycle typically includes:
1. **Problem Definition**: Understanding the business problem
2. **Data Collection**: Gathering relevant data
3. **Data Cleaning**: Handling missing values, outliers, duplicates
4. **Exploratory Data Analysis (EDA)**: Understanding patterns and relationships
5. **Feature Engineering**: Creating new features from existing data
6. **Model Building**: Training machine learning models
7. **Model Evaluation**: Testing model performance
8. **Deployment**: Putting the model into production
9. **Monitoring**: Tracking model performance over time

---

### Question 9 (5 points)
What are the key differences between pandas and NumPy? When would you use each?

**Pandas:**
- Built on top of NumPy
- Designed for structured data (tables, time series)
- Has labeled axes (index, columns)
- Better for data manipulation and analysis
- Use for: CSV files, data cleaning, data analysis, time series

**NumPy:**
- Fundamental library for numerical computing
- Works with arrays (n-dimensional)
- Faster for mathematical operations
- Use for: Mathematical computations, linear algebra, array operations, scientific computing

---

## Grading Rubric

- **90-100% (27-30 points):** Excellent understanding
- **80-89% (24-26 points):** Good understanding
- **70-79% (21-23 points):** Satisfactory
- **60-69% (18-20 points):** Needs improvement
- **Below 60% (<18 points):** Requires additional study

