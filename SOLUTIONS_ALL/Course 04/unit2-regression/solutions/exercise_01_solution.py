"""
Unit 2 - Exercise 1: Solution
تقنيات الانحدار المتقدمة - تمرين 1: الحل
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score

print("=" * 60)
print("Exercise 1: Solution")
print("تمرين 1: الحل")
print("=" * 60)

# Generate sample data
np.random.seed(42)
n_samples = 300

X = np.random.randn(n_samples, 8)
X[:, 2] = X[:, 0] + 0.3 * np.random.randn(n_samples)
X[:, 3] = X[:, 1] + 0.3 * np.random.randn(n_samples)

y = (2 * X[:, 0] + 1.5 * X[:, 1] - X[:, 2] + 3 * X[:, 3] + 
     0.5 * X[:, 4] + np.random.normal(0, 0.5, n_samples))

df = pd.DataFrame(X, columns=[f'feature_{i}' for i in range(8)])
df['target'] = y

# Task 1: Split the data and scale features
print("\n" + "=" * 60)
print("Task 1: Split and scale data")
print("=" * 60)

X_data = df.drop('target', axis=1)
y_data = df['target']

X_train, X_test, y_train, y_test = train_test_split(
    X_data, y_data, test_size=0.2, random_state=42
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print(f"Training set: {X_train.shape}")
print(f"Test set: {X_test.shape}")

# Task 2: Train models
print("\n" + "=" * 60)
print("Task 2: Train models")
print("=" * 60)

# Linear Regression
lr = LinearRegression()
lr.fit(X_train_scaled, y_train)
y_pred_lr = lr.predict(X_test_scaled)
mse_lr = mean_squared_error(y_test, y_pred_lr)

# Ridge Regression
ridge = Ridge(alpha=1.0)
ridge.fit(X_train_scaled, y_train)
y_pred_ridge = ridge.predict(X_test_scaled)
mse_ridge = mean_squared_error(y_test, y_pred_ridge)

# Lasso Regression
lasso = Lasso(alpha=0.1)
lasso.fit(X_train_scaled, y_train)
y_pred_lasso = lasso.predict(X_test_scaled)
mse_lasso = mean_squared_error(y_test, y_pred_lasso)

print(f"\nTest MSE:")
print(f"Linear Regression: {mse_lr:.4f}")
print(f"Ridge (α=1.0): {mse_ridge:.4f}")
print(f"Lasso (α=0.1): {mse_lasso:.4f}")

# Task 3: Compare coefficients
print("\n" + "=" * 60)
print("Task 3: Compare coefficients")
print("=" * 60)

coef_comparison = pd.DataFrame({
    'Feature': X_data.columns,
    'Linear': lr.coef_,
    'Ridge': ridge.coef_,
    'Lasso': lasso.coef_
})

print("\nCoefficient Comparison:")
print(coef_comparison.round(4).to_string(index=False))

# Visualize coefficients
plt.figure(figsize=(12, 6))
x_pos = np.arange(len(coef_comparison))
width = 0.25

plt.bar(x_pos - width, np.abs(coef_comparison['Linear']), width, label='Linear', alpha=0.7)
plt.bar(x_pos, np.abs(coef_comparison['Ridge']), width, label='Ridge', alpha=0.7)
plt.bar(x_pos + width, np.abs(coef_comparison['Lasso']), width, label='Lasso', alpha=0.7)

plt.xlabel('Features')
plt.ylabel('Absolute Coefficient Value')
plt.title('Coefficient Comparison')
plt.xticks(x_pos, coef_comparison['Feature'], rotation=45)
plt.legend()
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.savefig('exercise_02_coefficients.png', dpi=300, bbox_inches='tight')
print("\n✓ Plot saved as 'exercise_02_coefficients.png'")
plt.close()

# Task 4: Find optimal alpha
print("\n" + "=" * 60)
print("Task 4: Find optimal alpha")
print("=" * 60)

alphas = [0.01, 0.1, 0.5, 1.0, 5.0, 10.0, 50.0, 100.0]
ridge_mses = []
lasso_mses = []

for alpha in alphas:
    # Ridge
    ridge_temp = Ridge(alpha=alpha)
    ridge_temp.fit(X_train_scaled, y_train)
    y_pred_temp = ridge_temp.predict(X_test_scaled)
    ridge_mses.append(mean_squared_error(y_test, y_pred_temp))
    
    # Lasso
    lasso_temp = Lasso(alpha=alpha)
    lasso_temp.fit(X_train_scaled, y_train)
    y_pred_temp = lasso_temp.predict(X_test_scaled)
    lasso_mses.append(mean_squared_error(y_test, y_pred_temp))

# Find optimal alpha
optimal_ridge_alpha = alphas[np.argmin(ridge_mses)]
optimal_lasso_alpha = alphas[np.argmin(lasso_mses)]

print(f"\nOptimal Ridge Alpha: {optimal_ridge_alpha}")
print(f"Optimal Lasso Alpha: {optimal_lasso_alpha}")

# Plot
plt.figure(figsize=(10, 6))
plt.semilogx(alphas, ridge_mses, 'o-', label='Ridge', linewidth=2)
plt.semilogx(alphas, lasso_mses, 's-', label='Lasso', linewidth=2)
plt.axvline(optimal_ridge_alpha, color='blue', linestyle='--', alpha=0.5)
plt.axvline(optimal_lasso_alpha, color='orange', linestyle='--', alpha=0.5)
plt.xlabel('Alpha')
plt.ylabel('Test MSE')
plt.title('Finding Optimal Alpha')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('exercise_02_optimal_alpha.png', dpi=300, bbox_inches='tight')
print("\n✓ Plot saved as 'exercise_02_optimal_alpha.png'")
plt.close()

print("\n" + "=" * 60)
print("Exercise 1 Solution Complete! ✓")
print("=" * 60)

