"""
Unit 5 - Exercise 1: Solution
اختيار النموذج والتعزيز - تمرين 1: الحل

Complete solution for the model selection exercise
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
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
    n_samples=1000,
    n_features=10,
    n_informative=5,
    random_state=42
)

df = pd.DataFrame(X, columns=[f'feature_{i}' for i in range(10)])
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

# Task 2: Train default Random Forest
print("\n" + "=" * 60)
print("Task 2: Default Random Forest")
print("=" * 60)

rf_default = RandomForestClassifier(random_state=42)
rf_default.fit(X_train, y_train)

y_pred_default = rf_default.predict(X_test)
acc_default = accuracy_score(y_test, y_pred_default)

print(f"Default Random Forest Accuracy: {acc_default:.4f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred_default))

# Task 3: Grid Search for Random Forest
print("\n" + "=" * 60)
print("Task 3: Grid Search")
print("=" * 60)

# Define parameter grid
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [3, 5, 7, None],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

# Create base model
rf = RandomForestClassifier(random_state=42)

# Grid search with cross-validation
grid_search = GridSearchCV(
    rf,
    param_grid,
    cv=5,
    scoring='accuracy',
    n_jobs=-1,
    verbose=1
)

print("Starting Grid Search...")
grid_search.fit(X_train, y_train)

print(f"\nBest parameters: {grid_search.best_params_}")
print(f"Best cross-validation score: {grid_search.best_score_:.4f}")

# Train with best parameters
rf_best = grid_search.best_estimator_
y_pred_best = rf_best.predict(X_test)
acc_best = accuracy_score(y_test, y_pred_best)

print(f"\nBest Model Test Accuracy: {acc_best:.4f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred_best))

# Task 4: Compare results
print("\n" + "=" * 60)
print("Task 4: Compare")
print("=" * 60)

print(f"\nModel Comparison:")
print(f"Default Random Forest Accuracy: {acc_default:.4f}")
print(f"Grid Search Best Model Accuracy: {acc_best:.4f}")
print(f"Improvement: {acc_best - acc_default:.4f} ({((acc_best - acc_default) / acc_default * 100):.2f}%)")

# Confusion Matrices
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

cm_default = confusion_matrix(y_test, y_pred_default)
sns.heatmap(cm_default, annot=True, fmt='d', cmap='Blues', ax=axes[0])
axes[0].set_title(f'Default RF\nAccuracy: {acc_default:.4f}')
axes[0].set_ylabel('Actual')
axes[0].set_xlabel('Predicted')

cm_best = confusion_matrix(y_test, y_pred_best)
sns.heatmap(cm_best, annot=True, fmt='d', cmap='Greens', ax=axes[1])
axes[1].set_title(f'Grid Search Best\nAccuracy: {acc_best:.4f}')
axes[1].set_ylabel('Actual')
axes[1].set_xlabel('Predicted')

plt.tight_layout()
plt.savefig('unit5-model-selection/examples/exercise_01_comparison.png', dpi=150, bbox_inches='tight')
plt.close()

# Feature importance comparison
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

default_importance = pd.DataFrame({
    'feature': X.columns,
    'importance': rf_default.feature_importances_
}).sort_values('importance', ascending=False)

best_importance = pd.DataFrame({
    'feature': X.columns,
    'importance': rf_best.feature_importances_
}).sort_values('importance', ascending=False)

axes[0].barh(default_importance['feature'], default_importance['importance'], color='steelblue')
axes[0].set_title('Default RF Feature Importance')
axes[0].set_xlabel('Importance')

axes[1].barh(best_importance['feature'], best_importance['importance'], color='forestgreen')
axes[1].set_title('Grid Search Best RF Feature Importance')
axes[1].set_xlabel('Importance')

plt.tight_layout()
plt.savefig('unit5-model-selection/examples/exercise_01_feature_importance.png', dpi=150, bbox_inches='tight')
plt.close()

# Optional: XGBoost if available
try:
    import xgboost as xgb
    print("\n" + "=" * 60)
    print("Optional: XGBoost")
    print("=" * 60)
    
    xgb_model = xgb.XGBClassifier(random_state=42)
    xgb_model.fit(X_train, y_train)
    
    y_pred_xgb = xgb_model.predict(X_test)
    acc_xgb = accuracy_score(y_test, y_pred_xgb)
    
    print(f"XGBoost Accuracy: {acc_xgb:.4f}")
    print(f"Comparison with Grid Search: {acc_xgb - acc_best:.4f}")
    
except ImportError:
    print("\nXGBoost not available. Install with: pip install xgboost")

print("\n" + "=" * 60)
print("Solution Complete!")
print("اكتمل الحل!")
print("=" * 60)

