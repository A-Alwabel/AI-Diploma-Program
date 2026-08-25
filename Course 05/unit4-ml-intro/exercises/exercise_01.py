"""
Unit 4 - Exercise 1: Machine Learning Practice

Instructions:
1. Build a regression model
2. Build a classification model
3. Evaluate model performance
4. Compare different models
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, confusion_matrix, classification_report
from sklearn.datasets import fetch_california_housing
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['axes.unicode_minus'] = False
sns.set_style("whitegrid")

# Real data for regression
# ---------------------------------------------------------------------------
# California Housing: 20,640 census block groups from the 1990 U.S. census,
# shipped with scikit-learn. Target = median house value in $100,000s.
# Note the target is CAPPED at 5.0 ($500,001) in the census release - a real
# artefact you will see as a flat band at the top of any scatter plot.
# ---------------------------------------------------------------------------
housing = fetch_california_housing(as_frame=True)
house = housing.frame.sample(n=5000, random_state=42)   # classroom-size sample
HOUSE_FEATURES = ['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms',
                  'Population', 'AveOccup', 'Latitude', 'Longitude']
X_reg = house[HOUSE_FEATURES]
y_reg = house['MedHouseVal']

# Real data for classification
# ---------------------------------------------------------------------------
# The RMS Titanic passenger manifest: 891 real passengers, target = Survived.
# 177 ages are genuinely missing; we fill them with the median here so the
# exercise can start immediately, but note that choice - it is a real decision
# with real consequences, not a formality.
# ---------------------------------------------------------------------------
DATA_DIR = '../../../Course 04/datasets/raw/'
titanic = pd.read_csv(DATA_DIR + 'titanic.csv')
tit = titanic[['Age', 'Fare', 'SibSp', 'Parch', 'Pclass', 'Sex', 'Survived']].copy()
n_missing_age = tit['Age'].isna().sum()
tit['Age'] = tit['Age'].fillna(tit['Age'].median())
tit['is_female'] = (tit['Sex'] == 'female').astype(int)
CLF_FEATURES = ['Age', 'Fare', 'SibSp', 'Parch', 'Pclass', 'is_female']
X_clf = tit[CLF_FEATURES]
y_clf = tit['Survived']

print(f"Regression data: {X_reg.shape[0]:,} California census block groups "
      f"x {X_reg.shape[1]} features")
print(f"Classification data: {X_clf.shape[0]} Titanic passengers "
      f"({n_missing_age} missing ages median-filled, {y_clf.mean():.1%} survived)")
print(f"Majority-class baseline to beat: {max(y_clf.mean(), 1 - y_clf.mean()):.1%}")

# TODO: Write your code here

# Task 1: Regression Model
print("=" * 60)
print("Task 1: Linear Regression")
print("=" * 60)
# Your code here...
# - Split X_reg / y_reg into train/test sets
# - Train a linear regression model
# - Make predictions
# - Calculate MSE and R² score (expect R² around 0.6 - real data is noisy)
# - Visualize predictions vs actual, and look for the $500,001 cap

# Task 2: Classification Model
print("\n" + "=" * 60)
print("Task 2: Classification")
print("=" * 60)
# Your code here...
# - Split X_clf / y_clf into train/test sets (use stratify=y_clf)
# - Train a logistic regression model (scale the features first)
# - Train a decision tree classifier
# - Evaluate both models against the majority-class baseline printed above
# - Create confusion matrices and say WHICH errors each model makes

# Task 3: Model Comparison
print("\n" + "=" * 60)
print("Task 3: Model Comparison")
print("=" * 60)
# Your code here...
# - Compare accuracy of both classification models
# - Print classification reports (precision and recall, not just accuracy)
# - Visualize decision boundaries on two features (optional)

print("\n" + "=" * 60)
print("Exercise 1 Complete!")
print("=" * 60)
