# Test 2: Advanced Regression Techniques
## امتحان 2: تقنيات الانحدار المتقدمة

**Time Limit:** 90 minutes | **Marks:** 50 points

---

## Instructions
- Answer all questions
- Show your work for code questions
- Use proper comments in your code
- You may use pandas, numpy, sklearn, and matplotlib

---

## Part 1: Multiple Choice (15 points)

### Question 1 (3 points)
What is the main purpose of Ridge Regression (L2 regularization)?
- A) To reduce the number of features
- B) To penalize large coefficients and prevent overfitting
- C) To increase model complexity
- D) To handle missing values

**Answer:** B

---

### Question 2 (3 points)
What is the key difference between Ridge and Lasso regression?
- A) Ridge uses L1 penalty, Lasso uses L2 penalty
- B) Ridge uses L2 penalty, Lasso uses L1 penalty
- C) There is no difference
- D) Ridge is for classification, Lasso is for regression

**Answer:** B

---

### Question 3 (3 points)
Which regularization technique can set coefficients to exactly zero?
- A) Ridge Regression
- B) Lasso Regression
- C) Both
- D) Neither

**Answer:** B

---

### Question 4 (3 points)
What does cross-validation help with?
- A) Reducing overfitting
- B) Getting a more reliable estimate of model performance
- C) Speeding up training
- D) Handling missing values

**Answer:** B

---

### Question 5 (3 points)
In K-Fold cross-validation with K=5, how many times is the model trained?
- A) 1 time
- B) 5 times
- C) 10 times
- D) Depends on the data size

**Answer:** B

---

## Part 2: Code Implementation (25 points)

### Question 6 (10 points)
Complete the following code to implement Ridge and Lasso regression with cross-validation:

```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import Ridge, Lasso
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score

# Generate sample data
np.random.seed(42)
X = np.random.randn(200, 5)
y = 2 * X[:, 0] + 1.5 * X[:, 1] - X[:, 2] + np.random.normal(0, 0.5, 200)

# TODO: Split the data into train and test sets (80/20)
# TODO: Scale the features using StandardScaler
# TODO: Train Ridge regression with alpha=1.0
# TODO: Train Lasso regression with alpha=0.1
# TODO: Evaluate both models using cross-validation (5-fold)
# TODO: Print the cross-validation scores and R² scores for both models
```

**Expected Output:**
- Train/test split completed
- Features scaled
- Both models trained
- Cross-validation scores printed
- R² scores for both models printed

---

### Question 7 (10 points)
Write code to compare Ridge and Lasso regression coefficients:

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import Ridge, Lasso
from sklearn.preprocessing import StandardScaler

# Generate sample data
np.random.seed(42)
X = np.random.randn(200, 5)
y = 2 * X[:, 0] + 1.5 * X[:, 1] - X[:, 2] + np.random.normal(0, 0.5, 200)

# TODO: Scale the features
# TODO: Train Ridge with alpha=1.0
# TODO: Train Lasso with alpha=0.1
# TODO: Get coefficients from both models
# TODO: Create a bar plot comparing coefficients side by side
# TODO: Add labels, title, and legend
```

**Expected Output:**
- Bar plot showing Ridge and Lasso coefficients side by side
- Proper labels and legend

---

### Question 8 (5 points)
Explain the difference between MSE, RMSE, and MAE. When would you use each?

**Answer:**
- **MSE (Mean Squared Error)**: Average of squared differences. Sensitive to outliers. Used when large errors should be penalized more.
- **RMSE (Root Mean Squared Error)**: Square root of MSE. Same units as target variable. Commonly used for interpretability.
- **MAE (Mean Absolute Error)**: Average of absolute differences. Less sensitive to outliers. Used when all errors should be treated equally.

---

## Part 3: Analysis Questions (10 points)

### Question 9 (5 points)
You have a regression model with R² = 0.85 on training data but R² = 0.60 on test data. What is this problem called, and what are two ways to address it?

**Answer:**
- **Problem:** Overfitting
- **Solutions:**
  1. Use regularization (Ridge or Lasso) to penalize large coefficients
  2. Use cross-validation to get better performance estimates
  3. Reduce model complexity
  4. Increase training data size

---

### Question 10 (5 points)
Explain what happens to Ridge regression coefficients as the alpha parameter increases. What about Lasso?

**Answer:**
- **Ridge:** As alpha increases, coefficients shrink towards zero but never become exactly zero. All features remain in the model.
- **Lasso:** As alpha increases, coefficients shrink towards zero, and some become exactly zero. This performs automatic feature selection.

---

## Grading Rubric

| Question | Points | Criteria |
|----------|--------|----------|
| 1-5 | 15 | Multiple choice - 3 points each |
| 6 | 10 | Code implementation - correctness (6), completeness (4) |
| 7 | 10 | Code implementation - correctness (6), visualization (4) |
| 8 | 5 | Explanation quality - accuracy (3), clarity (2) |
| 9 | 5 | Problem identification (2), solutions (3) |
| 10 | 5 | Explanation quality - Ridge (2), Lasso (3) |

---

**Total: 50 points**

**Good luck!** 🍀  
**حظاً موفقاً!**

