# Dataset Quick Reference Guide

Quick code snippets to load diverse real-world datasets for each unit.

---

## 🔧 Unit 1: Data Processing & Regression

### 1. California Housing (Real Estate) ✅
**Already implemented in Example 5**

```python
from sklearn.datasets import fetch_california_housing
import pandas as pd

housing = fetch_california_housing()
df = pd.DataFrame(housing.data, columns=housing.feature_names)
df['target'] = housing.target
```

### 2. Student Performance (Education)
```python
# Option 1: Load from UCI URL
import pandas as pd

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00320/student.zip"
# Download and extract, then:
df = pd.read_csv('student/student-mat.csv', sep=';')

# Option 2: Use generated realistic data
import numpy as np
np.random.seed(42)
n_students = 500

data = {
    'study_hours': np.random.normal(20, 5, n_students),
    'attendance': np.random.normal(85, 10, n_students),
    'previous_grade': np.random.normal(75, 15, n_students),
    'extracurricular': np.random.choice([0, 1], n_students),
    'final_grade': None
}
# Create relationship: final_grade = f(study_hours, attendance, previous_grade)
df = pd.DataFrame(data)
```

### 3. Sales Data (E-Commerce)
```python
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)
n_products = 1000

categories = ['Electronics', 'Clothing', 'Food', 'Books', 'Sports']
dates = pd.date_range(start='2023-01-01', periods=365, freq='D')

df = pd.DataFrame({
    'date': np.random.choice(dates, n_products),
    'product_id': range(1, n_products + 1),
    'category': np.random.choice(categories, n_products),
    'price': np.random.uniform(10, 500, n_products),
    'quantity_sold': np.random.poisson(50, n_products),
    'customer_rating': np.random.uniform(1, 5, n_products),
    'sales_amount': None  # Will be price * quantity
})
df['sales_amount'] = df['price'] * df['quantity_sold']
```

---

## 📈 Unit 2: Advanced Regression

### 1. Bike Sharing (Transportation)
```python
import pandas as pd

# From UCI ML Repository
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00275/Bike-Sharing-Dataset.zip"
# Download, extract, then:
df = pd.read_csv('hour.csv')  # or 'day.csv' for daily data

# Key columns: season, weather, temp, humidity, windspeed, cnt (count of rentals)
```

### 2. Energy Consumption (Energy)
```python
import pandas as pd

# From UCI ML Repository  
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00242/ENB2012_data.xlsx"
df = pd.read_excel(url)

# Features: Temperature, Humidity, Light, CO2, Humidity Ratio
# Target: Energy consumption (Heating/Cooling)
```

### 3. Diabetes (Healthcare)
```python
from sklearn.datasets import load_diabetes
import pandas as pd

diabetes = load_diabetes()
df = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
df['target'] = diabetes.target  # Disease progression measure
```

---

## 🎯 Unit 3: Classification

### 1. Breast Cancer (Healthcare)
```python
from sklearn.datasets import load_breast_cancer
import pandas as pd

cancer = load_breast_cancer()
df = pd.DataFrame(cancer.data, columns=cancer.feature_names)
df['target'] = cancer.target  # 0 = malignant, 1 = benign
df['target_name'] = df['target'].map({0: 'Malignant', 1: 'Benign'})
```

### 2. Wine Quality (Food & Beverage)
```python
import pandas as pd

# Red wine
url_red = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
df_red = pd.read_csv(url_red, sep=';')

# White wine
url_white = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv"
df_white = pd.read_csv(url_white, sep=';')

# Combine or use separately
df_red['wine_type'] = 'red'
df_white['wine_type'] = 'white'
df = pd.concat([df_red, df_white], ignore_index=True)
```

### 3. Credit Card Fraud (Finance)
```python
import pandas as pd

# From Kaggle (requires login) or use sample
# URL: https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

# For demo, use smaller subset
# Full dataset has 284,807 transactions
# Only 492 fraud cases (highly imbalanced)

# Load sample (if available locally)
df = pd.read_csv('creditcard.csv')

# Or use sklearn's make_classification for demo
from sklearn.datasets import make_classification
X, y = make_classification(
    n_samples=10000, 
    n_features=30,
    n_informative=15,
    n_redundant=10,
    n_classes=2,
    weights=[0.998, 0.002],  # Imbalanced like real fraud data
    random_state=42
)
df = pd.DataFrame(X)
df['fraud'] = y
```

### 4. Pima Diabetes (Healthcare)
```python
import pandas as pd

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
column_names = ['pregnancies', 'glucose', 'blood_pressure', 'skin_thickness', 
                'insulin', 'bmi', 'diabetes_pedigree', 'age', 'outcome']
df = pd.read_csv(url, names=column_names)

# outcome: 0 = no diabetes, 1 = diabetes
```

---

## 🔍 Unit 4: Clustering

### 1. Mall Customers (Retail)
```python
import pandas as pd

# From Kaggle: https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python
# Or generate realistic data:

import numpy as np
np.random.seed(42)

n_customers = 200
df = pd.DataFrame({
    'customer_id': range(1, n_customers + 1),
    'gender': np.random.choice(['Male', 'Female'], n_customers),
    'age': np.random.normal(39, 14, n_customers).astype(int),
    'annual_income_k': np.random.normal(60, 26, n_customers),
    'spending_score': np.random.uniform(1, 100, n_customers)
})

# Clustering features: age, annual_income_k, spending_score
```

### 2. Countries Data (Economics)
```python
import pandas as pd

# Option 1: World Bank API (requires wbdata package)
# pip install wbdata
import wbdata

countries = wbdata.get_countries()
indicators = {
    'NY.GDP.PCAP.CD': 'gdp_per_capita',
    'SP.DYN.LE00.IN': 'life_expectancy',
    'SP.POP.TOTL': 'population'
}
df = wbdata.get_dataframe(indicators, country='all')

# Option 2: Use UCI Countries dataset
# Or generate realistic data based on World Bank patterns
```

### 3. Wine (for Clustering)
```python
from sklearn.datasets import load_wine
import pandas as pd

wine = load_wine()
df = pd.DataFrame(wine.data, columns=wine.feature_names)
df['wine_type'] = wine.target  # 0, 1, 2 (for supervised)
# For clustering, use only features (exclude wine_type)
```

---

## 🚀 Unit 5: Model Selection & Boosting

### 1. Loan Default (Finance)
```python
import pandas as pd
import numpy as np

# Generate realistic loan data
np.random.seed(42)
n_loans = 10000

df = pd.DataFrame({
    'loan_amount': np.random.normal(100000, 50000, n_loans),
    'interest_rate': np.random.normal(7.5, 2, n_loans),
    'credit_score': np.random.normal(650, 100, n_loans),
    'employment_years': np.random.exponential(5, n_loans),
    'debt_to_income': np.random.normal(30, 10, n_loans),
    'has_collateral': np.random.choice([0, 1], n_loans),
    'default': None  # Will be calculated based on risk factors
})

# Create relationship: higher risk = more likely to default
risk_score = (
    (df['credit_score'] < 600).astype(int) * 2 +
    (df['debt_to_income'] > 40).astype(int) * 1.5 +
    (df['employment_years'] < 2).astype(int) * 1.5 +
    (df['loan_amount'] > 150000).astype(int) * 0.5
)
df['default'] = (np.random.random(n_loans) < (risk_score / 10)).astype(int)
```

### 2. Employee Performance (HR)
```python
import pandas as pd
import numpy as np

np.random.seed(42)
n_employees = 1500

departments = ['Sales', 'Engineering', 'Marketing', 'HR', 'Finance']
education_levels = ['High School', 'Bachelor', 'Master', 'PhD']

df = pd.DataFrame({
    'employee_id': range(1, n_employees + 1),
    'age': np.random.normal(35, 10, n_employees).astype(int),
    'department': np.random.choice(departments, n_employees),
    'education': np.random.choice(education_levels, n_employees, 
                                   p=[0.1, 0.5, 0.3, 0.1]),
    'years_experience': np.random.exponential(5, n_employees),
    'training_hours': np.random.normal(40, 15, n_employees),
    'performance_score': None  # Target variable
})

# Create performance relationship
education_map = {'High School': 1, 'Bachelor': 2, 'Master': 3, 'PhD': 4}
df['education_numeric'] = df['education'].map(education_map)
df['performance_score'] = (
    50 + 
    df['years_experience'] * 2 +
    df['education_numeric'] * 5 +
    df['training_hours'] * 0.3 +
    np.random.normal(0, 10, n_employees)
)
df['performance_score'] = np.clip(df['performance_score'], 0, 100)
```

---

## 🔄 Utility Functions

### Function to Load Any sklearn Dataset
```python
from sklearn.datasets import (
    load_breast_cancer, load_wine, load_iris,
    load_diabetes, fetch_california_housing
)

def load_sklearn_dataset(dataset_name):
    """Load sklearn dataset and return as DataFrame"""
    dataset_map = {
        'breast_cancer': load_breast_cancer,
        'wine': load_wine,
        'iris': load_iris,
        'diabetes': load_diabetes,
        'california_housing': fetch_california_housing,
    }
    
    loader = dataset_map.get(dataset_name.lower())
    if not loader:
        raise ValueError(f"Unknown dataset: {dataset_name}")
    
    data = loader()
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['target'] = data.target
    return df, data
```

### Function to Download from URL with Caching
```python
import os
import pandas as pd
import requests
from pathlib import Path

def load_dataset_from_url(url, filename, cache_dir='data', **kwargs):
    """Download dataset from URL with caching"""
    cache_dir = Path(cache_dir)
    cache_dir.mkdir(exist_ok=True)
    
    filepath = cache_dir / filename
    
    if not filepath.exists():
        print(f"Downloading {filename}...")
        response = requests.get(url)
        filepath.write_bytes(response.content)
        print(f"Saved to {filepath}")
    
    # Load based on file extension
    if filename.endswith('.csv'):
        return pd.read_csv(filepath, **kwargs)
    elif filename.endswith('.xlsx') or filename.endswith('.xls'):
        return pd.read_excel(filepath, **kwargs)
    else:
        raise ValueError(f"Unsupported file type: {filename}")
```

---

## 📊 Quick Comparison Table

| Dataset | Domain | Load Method | Size | Best For |
|---------|--------|-------------|------|----------|
| California Housing | Real Estate | sklearn | 20K | Regression |
| Breast Cancer | Healthcare | sklearn | 569 | Classification |
| Wine Quality | Food | UCI URL | 6K | Classification/Clustering |
| Mall Customers | Retail | Generate/Kaggle | 200 | Clustering |
| Bike Sharing | Transportation | UCI URL | 17K | Regression |
| Diabetes | Healthcare | sklearn | 442 | Regression |
| Loan Default | Finance | Generate | 10K | Model Selection |

---

