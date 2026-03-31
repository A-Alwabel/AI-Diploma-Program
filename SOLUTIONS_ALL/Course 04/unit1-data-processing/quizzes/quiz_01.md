# Quiz 01: Data Processing Basics | اختبار 01: أساسيات معالجة البيانات

## Instructions | التعليمات
- **Time Limit**: 30 minutes
- **Total Points**: 50 points
- **Format**: Multiple choice, short answer, code completion
- **Allowed Resources**: None (closed book)

---

## Part 1: Data Loading and Exploration (15 points)

### Question 1 (5 points)
What does `df.info()` display?
- A) First 5 rows of the DataFrame
- B) Statistical summary of numerical columns
- C) Data types, non-null counts, and memory usage
- D) Last 5 rows of the DataFrame

**Answer:** C

---

### Question 2 (5 points)
Which method is used to read a CSV file in pandas?
- A) `pd.read_excel()`
- B) `pd.read_csv()`
- C) `pd.read_json()`
- D) `pd.load_csv()`

**Answer:** B

---

### Question 3 (5 points)
What does `df.describe()` return?
- A) Data types of each column
- B) Statistical summary (mean, std, min, max, etc.) for numerical columns
- C) Number of missing values
- D) Column names

**Answer:** B

---

## Part 2: Data Cleaning (15 points)

### Question 4 (5 points)
How do you check for missing values in a DataFrame?
- A) `df.missing()`
- B) `df.isnull().sum()`
- C) `df.find_na()`
- D) `df.check_null()`

**Answer:** B

---

### Question 5 (5 points)
What method removes duplicate rows from a DataFrame?
- A) `df.remove_duplicates()`
- B) `df.drop_duplicates()`
- C) `df.unique()`
- D) `df.deduplicate()`

**Answer:** B

---

### Question 6 (5 points)
Which method fills missing values with a specific value?
- A) `df.replace()`
- B) `df.fillna()`
- C) `df.update()`
- D) `df.set_value()`

**Answer:** B

---

## Part 3: Data Preprocessing (10 points)

### Question 7 (5 points)
What is the purpose of StandardScaler?
- A) To encode categorical variables
- B) To standardize features to have mean=0 and std=1
- C) To remove outliers
- D) To handle missing values

**Answer:** B

---

### Question 8 (5 points)
Which encoding method creates binary columns for each category?
- A) Label Encoding
- B) One-Hot Encoding
- C) Ordinal Encoding
- D) Binary Encoding

**Answer:** B

---

## Part 4: Basic Regression (10 points)

### Question 9 (5 points)
In linear regression, what does the coefficient represent?
- A) The intercept
- B) The change in target variable per unit change in feature
- C) The error term
- D) The correlation coefficient

**Answer:** B

---

### Question 10 (5 points)
What is the difference between simple and multiple linear regression?
- A) Simple uses one feature, multiple uses many features
- B) Simple uses polynomial features, multiple uses linear features
- C) There is no difference
- D) Simple is for classification, multiple is for regression

**Answer:** A

---

## Answer Key | مفتاح الإجابات

1. C - Data types, non-null counts, and memory usage
2. B - `pd.read_csv()`
3. B - Statistical summary (mean, std, min, max, etc.) for numerical columns
4. B - `df.isnull().sum()`
5. B - `df.drop_duplicates()`
6. B - `df.fillna()`
7. B - To standardize features to have mean=0 and std=1
8. B - One-Hot Encoding
9. B - The change in target variable per unit change in feature
10. A - Simple uses one feature, multiple uses many features

---

**Good luck!** 🍀  
**حظاً موفقاً!**

