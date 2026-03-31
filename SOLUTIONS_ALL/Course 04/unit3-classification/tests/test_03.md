# Test 3: Classification Techniques
## امتحان 3: تقنيات التصنيف

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
What is the main difference between regression and classification?
- A) Regression predicts continuous values, classification predicts categories
- B) Classification predicts continuous values, regression predicts categories
- C) There is no difference
- D) Regression uses neural networks, classification uses trees

**Answer:** A

---

### Question 2 (3 points)
Which algorithm uses a sigmoid function to output probabilities?
- A) Decision Tree
- B) Logistic Regression
- C) K-Nearest Neighbors
- D) Support Vector Machine

**Answer:** B

---

### Question 3 (3 points)
What does precision measure?
- A) The proportion of correctly classified instances
- B) The proportion of positive predictions that are correct
- C) The proportion of actual positives that are correctly identified
- D) The harmonic mean of precision and recall

**Answer:** B

---

### Question 4 (3 points)
What does recall measure?
- A) The proportion of correctly classified instances
- B) The proportion of positive predictions that are correct
- C) The proportion of actual positives that are correctly identified
- D) The harmonic mean of precision and recall

**Answer:** C

---

### Question 5 (3 points)
In a confusion matrix, what does True Positive (TP) represent?
- A) Correctly predicted negative cases
- B) Correctly predicted positive cases
- C) Incorrectly predicted negative cases
- D) Incorrectly predicted positive cases

**Answer:** B

---

## Part 2: Code Implementation (25 points)

### Question 6 (10 points)
Complete the following code to train and evaluate a classification model:

```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (accuracy_score, precision_score, recall_score,
                            f1_score, confusion_matrix, classification_report)
from sklearn.datasets import make_classification

# Generate sample classification data
np.random.seed(42)
X, y = make_classification(
    n_samples=500,
    n_features=5,
    n_informative=3,
    random_state=42
)

# TODO: Split the data into train and test sets (80/20)
# TODO: Train a Decision Tree classifier with max_depth=5
# TODO: Make predictions on test set
# TODO: Calculate and print: accuracy, precision, recall, F1-score
# TODO: Print confusion matrix
# TODO: Print classification report
```

**Expected Output:**
- Train/test split completed
- Model trained
- All metrics printed
- Confusion matrix displayed
- Classification report printed

---

### Question 7 (10 points)
Write code to compare Logistic Regression and Random Forest:

```python
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, roc_auc_score, roc_curve
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification

# Generate sample classification data
np.random.seed(42)
X, y = make_classification(
    n_samples=500,
    n_features=5,
    n_informative=3,
    random_state=42
)

# TODO: Split the data
# TODO: Train Logistic Regression
# TODO: Train Random Forest
# TODO: Get predictions and probabilities from both models
# TODO: Calculate accuracy and ROC-AUC for both
# TODO: Plot ROC curves for both models on the same graph
# TODO: Add labels, title, and legend
```

**Expected Output:**
- Both models trained
- Accuracy and ROC-AUC scores printed
- ROC curves plotted on same graph with legend

---

### Question 8 (5 points)
Explain when you would use precision vs recall. Give a real-world example for each.

**Answer:**
- **Precision:** Use when false positives are costly. Example: Email spam detection - we don't want to mark important emails as spam.
- **Recall:** Use when false negatives are costly. Example: Medical diagnosis - we don't want to miss detecting a disease.

---

## Part 3: Analysis Questions (10 points)

### Question 9 (5 points)
You have a classification model with 95% accuracy, but when you check the confusion matrix, you see it predicts class 0 for 98% of cases. What is the problem, and how would you fix it?

**Answer:**
- **Problem:** Class imbalance - the model is biased towards the majority class
- **Solutions:**
  1. Use class weights to balance the classes
  2. Use resampling techniques (oversample minority, undersample majority)
  3. Use different evaluation metrics (precision, recall, F1-score)
  4. Use SMOTE or other synthetic sampling techniques

---

### Question 10 (5 points)
Compare Decision Trees and Random Forest. What are the advantages and disadvantages of each?

**Answer:**
- **Decision Trees:**
  - Advantages: Easy to interpret, no feature scaling needed, handles non-linear relationships
  - Disadvantages: Prone to overfitting, sensitive to small data changes, can be unstable

- **Random Forest:**
  - Advantages: Reduces overfitting, more stable, handles missing values, feature importance
  - Disadvantages: Less interpretable, requires more computational resources, can be slower

---

## Grading Rubric

| Question | Points | Criteria |
|----------|--------|----------|
| 1-5 | 15 | Multiple choice - 3 points each |
| 6 | 10 | Code implementation - correctness (6), completeness (4) |
| 7 | 10 | Code implementation - correctness (6), visualization (4) |
| 8 | 5 | Explanation quality - accuracy (3), examples (2) |
| 9 | 5 | Problem identification (2), solutions (3) |
| 10 | 5 | Comparison quality - Decision Trees (2), Random Forest (3) |

---

**Total: 50 points**

**Good luck!** 🍀  
**حظاً موفقاً!**

