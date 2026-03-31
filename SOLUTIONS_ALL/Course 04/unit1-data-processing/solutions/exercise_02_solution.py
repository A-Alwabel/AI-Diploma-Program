"""
Unit 1 - Exercise 2: Solution
أساليب معالجة البيانات - تمرين 2: الحل

Complete solution for the linear regression exercise
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

print("=" * 60)
print("Exercise 2: Solution")
print("تمرين 2: الحل")
print("=" * 60)

# Generate sample housing data
np.random.seed(42)
house_sizes = np.random.uniform(800, 4000, 150)
house_prices = 45 * house_sizes + 80000 + np.random.normal(0, 35000, 150)

df = pd.DataFrame({
    'size': house_sizes,
    'price': house_prices
})

print("\nDataset Info:")
print(f"Shape: {df.shape}")
print(df.head())

# Task 1: Split the data into train and test sets (80/20)
print("\n" + "=" * 60)
print("Task 1: Split data")
print("المهمة 1: تقسيم البيانات")
print("=" * 60)

X = df[['size']]
y = df['price']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"Training set: {X_train.shape[0]} samples")
print(f"Test set: {X_test.shape[0]} samples")

# Task 2: Create and train a Linear Regression model
print("\n" + "=" * 60)
print("Task 2: Train Linear Regression model")
print("المهمة 2: تدريب نموذج الانحدار الخطي")
print("=" * 60)

model = LinearRegression()
model.fit(X_train, y_train)

print("Model trained successfully!")
print(f"Intercept: {model.intercept_:.2f}")
print(f"Coefficient: {model.coef_[0]:.4f}")

# Task 3: Make predictions and evaluate the model
print("\n" + "=" * 60)
print("Task 3: Evaluate model")
print("المهمة 3: تقييم النموذج")
print("=" * 60)

y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)

# Calculate metrics
train_mse = mean_squared_error(y_train, y_train_pred)
test_mse = mean_squared_error(y_test, y_test_pred)
train_mae = mean_absolute_error(y_train, y_train_pred)
test_mae = mean_absolute_error(y_test, y_test_pred)
train_r2 = r2_score(y_train, y_train_pred)
test_r2 = r2_score(y_test, y_test_pred)

print("\nTraining Metrics:")
print(f"  MSE: {train_mse:,.2f}")
print(f"  MAE: {train_mae:,.2f}")
print(f"  R² Score: {train_r2:.4f}")

print("\nTest Metrics:")
print(f"  MSE: {test_mse:,.2f}")
print(f"  MAE: {test_mae:,.2f}")
print(f"  R² Score: {test_r2:.4f}")

# Task 4: Visualize the results
print("\n" + "=" * 60)
print("Task 4: Visualize results")
print("المهمة 4: تصور النتائج")
print("=" * 60)

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Training data
axes[0].scatter(X_train, y_train, alpha=0.6, label='Training Data', color='blue')
axes[0].plot(X_train, y_train_pred, 'r-', linewidth=2, label='Regression Line')
axes[0].set_xlabel('House Size (sq ft)')
axes[0].set_ylabel('Price ($)')
axes[0].set_title(f'Training Data (R² = {train_r2:.4f})')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Test data
axes[1].scatter(X_test, y_test, alpha=0.6, label='Test Data', color='green')
axes[1].plot(X_test, y_test_pred, 'r-', linewidth=2, label='Regression Line')
axes[1].set_xlabel('House Size (sq ft)')
axes[1].set_ylabel('Price ($)')
axes[1].set_title(f'Test Data (R² = {test_r2:.4f})')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('exercise_02_visualization.png', dpi=300, bbox_inches='tight')
print("✓ Saved visualization: 'exercise_02_visualization.png'")
plt.close()

# Task 5: Make predictions for new house sizes
print("\n" + "=" * 60)
print("Task 5: Predict for new sizes")
print("المهمة 5: التنبؤ لأحجام جديدة")
print("=" * 60)

new_sizes = [[1000], [2000], [3000]]
new_predictions = model.predict(new_sizes)

print("\nPredictions for new house sizes:")
for size, price in zip([s[0] for s in new_sizes], new_predictions):
    print(f"  Size: {size:,.0f} sq ft → Predicted Price: ${price:,.2f}")

print("\n" + "=" * 60)
print("Exercise 2 Solution Complete! ✓")
print("اكتمل حل التمرين 2! ✓")
print("=" * 60)

