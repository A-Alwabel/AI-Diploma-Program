# Test 5: Model Selection and Boosting
## امتحان 5: اختيار النموذج والتعزيز

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
What is the main purpose of Grid Search?
- A) To find the best hyperparameters by trying all combinations
- B) To find the best features
- C) To find the best model architecture
- D) To find the best dataset

**Answer:** A

---

### Question 2 (3 points)
What is the main advantage of Random Search over Grid Search?
- A) It's always more accurate
- B) It's faster and can find good solutions with fewer iterations
- C) It always finds the best solution
- D) It doesn't require cross-validation

**Answer:** B

---

### Question 3 (3 points)
What is the main idea behind boosting?
- A) To combine multiple weak learners into a strong learner
- B) To use only the best single model
- C) To reduce the number of features
- D) To increase the number of samples

**Answer:** A

---

### Question 4 (3 points)
What is the difference between bagging and boosting?
- A) Bagging trains models in parallel, boosting trains sequentially
- B) Boosting trains models in parallel, bagging trains sequentially
- C) There is no difference
- D) Bagging is for regression, boosting is for classification

**Answer:** A

---

### Question 5 (3 points)
What is XGBoost?
- A) An optimized implementation of gradient boosting
- B) A type of neural network
- C) A clustering algorithm
- D) A dimensionality reduction technique

**Answer:** A

---

## Part 2: Code Implementation (25 points)

### Question 6 (10 points)
Complete the following code to implement Grid Search for hyperparameter tuning:

```python
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
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
# TODO: Define parameter grid for Random Forest:
#       - n_estimators: [50, 100, 200]
#       - max_depth: [3, 5, 7]
#       - min_samples_split: [2, 5, 10]
# TODO: Create GridSearchCV with 5-fold cross-validation
# TODO: Fit the grid search on training data
# TODO: Get the best model and best parameters
# TODO: Evaluate on test set and print accuracy
```

**Expected Output:**
- Train/test split completed
- Grid search completed
- Best parameters printed
- Test accuracy printed

---

### Question 7 (10 points)
Write code to compare default Random Forest with Grid Search optimized Random Forest:

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, roc_auc_score, roc_curve
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
# TODO: Train default Random Forest
# TODO: Train Grid Search optimized Random Forest (use Question 6 parameters)
# TODO: Get predictions and probabilities from both
# TODO: Calculate accuracy and ROC-AUC for both
# TODO: Plot ROC curves for both models
# TODO: Add labels, title, and legend
```

**Expected Output:**
- Both models trained
- Accuracy and ROC-AUC scores printed
- ROC curves plotted with legend

---

### Question 8 (5 points)
Explain the difference between Grid Search and Random Search. When would you use each?

**Answer:**
- **Grid Search:**
  - Tries all combinations of hyperparameters
  - Guaranteed to find best combination in search space
  - Can be very slow with many parameters
  - Use when search space is small or you need the absolute best parameters

- **Random Search:**
  - Tries random combinations of hyperparameters
  - Faster, can find good solutions with fewer iterations
  - May miss optimal combination
  - Use when search space is large or you have limited time/computational resources

---

## Part 3: Analysis Questions (10 points)

### Question 9 (5 points)
You have a model that performs well on training data but poorly on test data. You've already tried regularization. What other techniques from this unit could you use to improve generalization?

**Answer:**
- **Hyperparameter Tuning:**
  1. Use Grid Search or Random Search to find optimal hyperparameters
  2. Use cross-validation to get better performance estimates
  3. Tune parameters like max_depth, min_samples_split, learning_rate, etc.

- **Ensemble Methods:**
  1. Use Boosting (Gradient Boosting, XGBoost) to combine weak learners
  2. Use Voting Classifier to combine multiple models
  3. Use Stacking with a meta-learner

- **Other Techniques:**
  1. Increase training data
  2. Use feature selection to reduce overfitting
  3. Use learning curves to diagnose the problem

---

### Question 10 (5 points)
Compare Gradient Boosting and XGBoost. What are the advantages of XGBoost?

**Answer:**
- **Gradient Boosting:**
  - Sequential training of weak learners
  - Each learner corrects previous errors
  - Can be slow and memory intensive

- **XGBoost Advantages:**
  1. **Performance:** Optimized implementation, faster training
  2. **Regularization:** Built-in L1 and L2 regularization
  3. **Handling Missing Values:** Can handle missing values automatically
  4. **Parallel Processing:** Can use parallel processing for tree construction
  5. **Early Stopping:** Built-in early stopping to prevent overfitting
  6. **Cross-validation:** Built-in cross-validation support
  7. **Feature Importance:** Better feature importance calculation

---

## Grading Rubric

| Question | Points | Criteria |
|----------|--------|----------|
| 1-5 | 15 | Multiple choice - 3 points each |
| 6 | 10 | Code implementation - correctness (6), completeness (4) |
| 7 | 10 | Code implementation - correctness (6), visualization (4) |
| 8 | 5 | Explanation quality - Grid Search (2), Random Search (3) |
| 9 | 5 | Techniques identified (3), explanation (2) |
| 10 | 5 | Comparison quality - Gradient Boosting (2), XGBoost advantages (3) |

---

**Total: 50 points**

**Good luck!** 🍀  
**حظاً موفقاً!**

