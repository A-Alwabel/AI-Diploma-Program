"""
Unit 4 - Exercise 1: Solution
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['axes.unicode_minus'] = False
sns.set_style("whitegrid")

# Generate data
np.random.seed(42)
n_samples = 200
X_reg = np.random.randn(n_samples, 3)
y_reg = 2.5 * X_reg[:, 0] + 1.5 * X_reg[:, 1] - 0.5 * X_reg[:, 2] + np.random.randn(n_samples) * 0.5

X_clf = np.random.randn(n_samples, 2)
y_clf = (X_clf[:, 0] + X_clf[:, 1] > 0).astype(int)

# Task 1: Regression
print("=" * 60)
print("Task 1: Linear Regression")
print("=" * 60)

X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(
    X_reg, y_reg, test_size=0.2, random_state=42
)

lr = LinearRegression()
lr.fit(X_train_reg, y_train_reg)
y_pred_reg = lr.predict(X_test_reg)

mse = mean_squared_error(y_test_reg, y_pred_reg)
r2 = r2_score(y_test_reg, y_pred_reg)

print(f"\nMSE: {mse:.4f}")
print(f"R² Score: {r2:.4f}")

# Visualization
plt.figure(figsize=(8, 6))
plt.scatter(y_test_reg, y_pred_reg, alpha=0.6)
plt.plot([y_test_reg.min(), y_test_reg.max()], 
         [y_test_reg.min(), y_test_reg.max()], 'r--', lw=2)
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.title('Regression: Actual vs Predicted')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('unit4-ml-intro/examples/regression_plot.png', dpi=150)
plt.close()

# Task 2: Classification
print("\n" + "=" * 60)
print("Task 2: Classification")
print("=" * 60)

X_train_clf, X_test_clf, y_train_clf, y_test_clf = train_test_split(
    X_clf, y_clf, test_size=0.2, random_state=42, stratify=y_clf
)

# Logistic Regression
log_reg = LogisticRegression(random_state=42)
log_reg.fit(X_train_clf, y_train_clf)
y_pred_log = log_reg.predict(X_test_clf)
acc_log = accuracy_score(y_test_clf, y_pred_log)

# Decision Tree
dt = DecisionTreeClassifier(random_state=42)
dt.fit(X_train_clf, y_train_clf)
y_pred_dt = dt.predict(X_test_clf)
acc_dt = accuracy_score(y_test_clf, y_pred_dt)

print(f"\nLogistic Regression Accuracy: {acc_log:.4f}")
print(f"Decision Tree Accuracy: {acc_dt:.4f}")

# Confusion Matrices
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

cm_log = confusion_matrix(y_test_clf, y_pred_log)
sns.heatmap(cm_log, annot=True, fmt='d', cmap='Blues', ax=axes[0])
axes[0].set_title('Logistic Regression Confusion Matrix')

cm_dt = confusion_matrix(y_test_clf, y_pred_dt)
sns.heatmap(cm_dt, annot=True, fmt='d', cmap='Greens', ax=axes[1])
axes[1].set_title('Decision Tree Confusion Matrix')

plt.tight_layout()
plt.savefig('unit4-ml-intro/examples/confusion_matrices.png', dpi=150)
plt.close()

# Task 3: Model Comparison
print("\n" + "=" * 60)
print("Task 3: Model Comparison")
print("=" * 60)

print("\nLogistic Regression Classification Report:")
print(classification_report(y_test_clf, y_pred_log))

print("\nDecision Tree Classification Report:")
print(classification_report(y_test_clf, y_pred_dt))

print(f"\nBest Model: {'Decision Tree' if acc_dt > acc_log else 'Logistic Regression'}")
print(f"Accuracy Difference: {abs(acc_dt - acc_log):.4f}")

print("\n" + "=" * 60)
print("Solution Complete!")
print("=" * 60)

