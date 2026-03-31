"""
Unit 3 - Exercise 1: Solution
تقنيات التصنيف المتقدمة - تمرين 1: الحل

Complete solution for the classification exercise
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (accuracy_score, classification_report,
                            confusion_matrix)
from sklearn.datasets import make_classification

plt.rcParams['axes.unicode_minus'] = False
sns.set_style("whitegrid")

print("=" * 60)
print("Exercise 1: Solution")
print("تمرين 1: الحل")
print("=" * 60)

# Generate sample classification data
np.random.seed(42)
X, y = make_classification(
    n_samples=800,
    n_features=8,
    n_informative=5,
    n_redundant=2,
    random_state=42
)

df = pd.DataFrame(X, columns=[f'feature_{i}' for i in range(8)])
df['target'] = y

print(f"\nData Shape: {df.shape}")
print(f"Target distribution:\n{df['target'].value_counts()}")

# Task 1: Split the data
print("\n" + "=" * 60)
print("Task 1: Split data")
print("=" * 60)

X = df.drop('target', axis=1)
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print(f"Training set: {X_train.shape[0]} samples")
print(f"Test set: {X_test.shape[0]} samples")

# Task 2: Train Decision Tree
print("\n" + "=" * 60)
print("Task 2: Train Decision Tree")
print("=" * 60)

dt = DecisionTreeClassifier(random_state=42, max_depth=5)
dt.fit(X_train, y_train)

y_pred_dt = dt.predict(X_test)
acc_dt = accuracy_score(y_test, y_pred_dt)

print(f"Decision Tree Accuracy: {acc_dt:.4f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred_dt))

# Task 3: Train Random Forest
print("\n" + "=" * 60)
print("Task 3: Train Random Forest")
print("=" * 60)

rf = RandomForestClassifier(n_estimators=100, random_state=42, max_depth=5)
rf.fit(X_train, y_train)

y_pred_rf = rf.predict(X_test)
acc_rf = accuracy_score(y_test, y_pred_rf)

print(f"Random Forest Accuracy: {acc_rf:.4f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred_rf))

# Task 4: Evaluate both models
print("\n" + "=" * 60)
print("Task 4: Evaluate models")
print("=" * 60)

print(f"\nModel Comparison:")
print(f"Decision Tree Accuracy: {acc_dt:.4f}")
print(f"Random Forest Accuracy: {acc_rf:.4f}")
print(f"Improvement: {acc_rf - acc_dt:.4f}")

# Confusion Matrices
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

cm_dt = confusion_matrix(y_test, y_pred_dt)
sns.heatmap(cm_dt, annot=True, fmt='d', cmap='Blues', ax=axes[0])
axes[0].set_title('Decision Tree Confusion Matrix')
axes[0].set_ylabel('Actual')
axes[0].set_xlabel('Predicted')

cm_rf = confusion_matrix(y_test, y_pred_rf)
sns.heatmap(cm_rf, annot=True, fmt='d', cmap='Greens', ax=axes[1])
axes[1].set_title('Random Forest Confusion Matrix')
axes[1].set_ylabel('Actual')
axes[1].set_xlabel('Predicted')

plt.tight_layout()
plt.savefig('unit3-classification/examples/exercise_01_confusion_matrices.png', dpi=150, bbox_inches='tight')
plt.close()

# Task 5: Compare feature importance
print("\n" + "=" * 60)
print("Task 5: Feature importance")
print("=" * 60)

# Decision Tree feature importance
dt_importance = pd.DataFrame({
    'feature': X.columns,
    'importance_dt': dt.feature_importances_
}).sort_values('importance_dt', ascending=False)

# Random Forest feature importance
rf_importance = pd.DataFrame({
    'feature': X.columns,
    'importance_rf': rf.feature_importances_
}).sort_values('importance_rf', ascending=False)

print("\nDecision Tree - Top 5 Features:")
print(dt_importance.head())

print("\nRandom Forest - Top 5 Features:")
print(rf_importance.head())

# Visualize feature importance
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

axes[0].barh(dt_importance['feature'], dt_importance['importance_dt'], color='steelblue')
axes[0].set_title('Decision Tree Feature Importance')
axes[0].set_xlabel('Importance')

axes[1].barh(rf_importance['feature'], rf_importance['importance_rf'], color='forestgreen')
axes[1].set_title('Random Forest Feature Importance')
axes[1].set_xlabel('Importance')

plt.tight_layout()
plt.savefig('unit3-classification/examples/exercise_01_feature_importance.png', dpi=150, bbox_inches='tight')
plt.close()

print("\n" + "=" * 60)
print("Solution Complete!")
print("اكتمل الحل!")
print("=" * 60)

