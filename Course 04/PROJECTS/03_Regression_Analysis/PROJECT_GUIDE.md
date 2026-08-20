# Complete Project Guide: 03 Regression Analysis

---

## 🎯 Real-World Application

---

## 🚀 Quick Start (For Experienced Students)

> 💡 **New to this project?** Skip to [Complete Tutorial](#-complete-tutorial-for-beginners) section below.

## Step-by-Step Implementation

---

## 📚 Complete Tutorial (For Beginners)

> 💡 **Already familiar with this?** See [Quick Start](#-quick-start-for-experienced-students) section above.

### Step 1: Understand Regression (Day 1)

**What is Regression?**
Predicting a continuous value (like price, sales, temperature):
- **Linear:** Simple straight line
- **Ridge:** Prevents overfitting (L2 regularization)
- **Lasso:** Selects important features (L1 regularization)
- **Polynomial:** Handles non-linear relationships

**Example:**
```
Features: Advertising budget, Season, Location
Target: Sales amount

Linear: Sales = a × Budget + b × Season + c
Ridge: Same but prevents overfitting
Lasso: Same but selects only important features
Polynomial: Sales = a × Budget² + b × Budget + c
```

---

### Step 2: Set Up Project (Day 1)

**Create structure:**
```
regression_project/
├── data/
│   └── sales_data.csv
├── src/
│   ├── data_loader.py
│   ├── regressors.py
│   └── evaluator.py
├── main.py
└── README.md
```

**Install:**
```bash
pip install pandas numpy scikit-learn matplotlib seaborn
```

---

### Step 3: Load and Prepare Data (Day 2)

**File: `src/data_loader.py`**

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

class DataLoader:
    def load_data(self, filepath):
        """Load regression dataset"""
        df = pd.read_csv(filepath)
        return df
    
    def prepare_data(self, df, target_column):
        """Prepare features and target"""
        X = df.drop(columns=[target_column])
        y = df[target_column]
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        # Scale features (important for regularization)
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)
        
        return X_train_scaled, X_test_scaled, y_train, y_test, scaler
```

---

### Step 4: Implement Regressors (Day 3)

**File: `src/regressors.py`**

```python
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline

class RegressionSystem:
    """Multiple regression algorithms"""
    
    def __init__(self):
        self.models = {}
    
    def train_all(self, X_train, y_train):
        """Train all regression models"""
        
        # 1. Linear Regression
        lr = LinearRegression()
        lr.fit(X_train, y_train)
        self.models['Linear'] = lr
        
        # 2. Ridge Regression (L2 regularization)
        ridge = Ridge(alpha=1.0)  # alpha controls regularization
        ridge.fit(X_train, y_train)
        self.models['Ridge'] = ridge
        
        # 3. Lasso Regression (L1 regularization)
        lasso = Lasso(alpha=1.0)
        lasso.fit(X_train, y_train)
        self.models['Lasso'] = lasso
        
        # 4. Polynomial Regression
        poly = Pipeline([
            ('poly', PolynomialFeatures(degree=2)),
            ('linear', LinearRegression())
        ])
        poly.fit(X_train, y_train)
        self.models['Polynomial'] = poly
        
        print("✅ Trained all regression models")
        return self.models
```

---

### Step 5: Evaluate Models (Day 4)

**File: `src/evaluator.py`**

```python
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import matplotlib.pyplot as plt
import numpy as np

class RegressionEvaluator:
    """Evaluate regression models"""
    
    def evaluate_all(self, models, X_test, y_test):
        """Evaluate all models"""
        results = {}
        
        for name, model in models.items():
            y_pred = model.predict(X_test)
            
            results[name] = {
                'MSE': mean_squared_error(y_test, y_pred),
                'RMSE': np.sqrt(mean_squared_error(y_test, y_pred)),
                'MAE': mean_absolute_error(y_test, y_pred),
                'R2': r2_score(y_test, y_pred)
            }
            
            print(f"\n{name}:")
            print(f"  MSE: {results[name]['MSE']:.2f}")
            print(f"  RMSE: {results[name]['RMSE']:.2f}")
            print(f"  MAE: {results[name]['MAE']:.2f}")
            print(f"  R²: {results[name]['R2']:.4f}")
        
        return results
    
    def plot_predictions(self, model, X_test, y_test, name):
        """Plot predictions vs actual"""
        y_pred = model.predict(X_test)
        
        plt.figure(figsize=(10, 6))
        plt.scatter(y_test, y_pred, alpha=0.6)
        plt.plot([y_test.min(), y_test.max()], 
                [y_test.min(), y_test.max()], 'r--', lw=2)
        plt.xlabel('Actual Values')
        plt.ylabel('Predicted Values')
        plt.title(f'{name} Regression - Predictions vs Actual')
        plt.savefig(f'results/{name}_predictions.png')
        plt.close()
```

---

### Step 6: Hyperparameter Tuning (Day 5)

```python
from sklearn.model_selection import GridSearchCV

def tune_ridge(X_train, y_train):
    """Tune Ridge regression hyperparameters"""
    param_grid = {'alpha': [0.1, 1.0, 10.0, 100.0]}
    ridge = Ridge()
    grid_search = GridSearchCV(ridge, param_grid, cv=5, scoring='r2')
    grid_search.fit(X_train, y_train)
    
    print(f"Best alpha: {grid_search.best_params_['alpha']}")
    print(f"Best R²: {grid_search.best_score_:.4f}")
    
    return grid_search.best_estimator_

def tune_lasso(X_train, y_train):
    """Tune Lasso regression hyperparameters"""
    param_grid = {'alpha': [0.1, 1.0, 10.0, 100.0]}
    lasso = Lasso()
    grid_search = GridSearchCV(lasso, param_grid, cv=5, scoring='r2')
    grid_search.fit(X_train, y_train)
    
    print(f"Best alpha: {grid_search.best_params_['alpha']}")
    print(f"Best R²: {grid_search.best_score_:.4f}")
    
    return grid_search.best_estimator_
```

---

### Step 7: Create Main Program (Day 6)

**File: `main.py`**

```python
from src.data_loader import DataLoader
from src.regressors import RegressionSystem
from src.evaluator import RegressionEvaluator

def main():
    # Load data
    loader = DataLoader()
    df = loader.load_data('data/sales_data.csv')
    
    # Prepare data
    X_train, X_test, y_train, y_test, scaler = loader.prepare_data(
        df, target_column='sales'
    )
    
    # Train models
    regressor = RegressionSystem()
    models = regressor.train_all(X_train, y_train)
    
    # Evaluate
    evaluator = RegressionEvaluator()
    results = evaluator.evaluate_all(models, X_test, y_test)
    
    # Find best model
    best_model = max(results, key=lambda x: results[x]['R2'])
    print(f"\n✅ Best model: {best_model}")
    
    # Plot predictions
    for name, model in models.items():
        evaluator.plot_predictions(model, X_test, y_test, name)

if __name__ == "__main__":
    main()
```

---

---