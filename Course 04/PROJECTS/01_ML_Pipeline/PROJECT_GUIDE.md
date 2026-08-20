# Complete Project Guide: ML Pipeline

---

## 🎯 Real-World Application

### Example: House Price Prediction System
**Imagine you're building a system like Zillow or Redfin that predicts house prices.**

**Problem:** Real estate companies need to estimate house prices quickly and accurately to:
- Help buyers make informed decisions
- Help sellers price their homes
- Enable automated valuations

**Solution:** Your ML pipeline:
1. **Loads** house data (size, bedrooms, location, etc.)
2. **Cleans** data (removes errors, handles missing values)
3. **Processes** features (scales, encodes categories)
4. **Trains** models to predict prices
5. **Evaluates** which model works best
6. **Deploys** for real-time predictions

**Real-World Impact:**
- ✅ Instant price estimates for millions of homes
- ✅ More accurate than manual appraisals
- ✅ Available 24/7
- ✅ Saves time and money

**Similar Systems:**
- Zillow, Redfin (real estate)
- Amazon (product pricing)
- Financial services (credit scoring)
- Healthcare (treatment recommendations)

---

## 🚀 Quick Start (For Experienced Students)

> 💡 **New to ML pipelines?** Skip to [Complete Tutorial](#-complete-tutorial-for-beginners) section below.

### Project Structure
```
ml_pipeline_project/
├── data/
│   └── house_prices.csv
├── src/
│   ├── data_loader.py
│   ├── preprocessor.py
│   ├── feature_engineer.py
│   ├── model_trainer.py
│   └── pipeline.py
├── models/
├── results/
├── main.py
└── README.md
```

### Key Functions to Implement

**data_loader.py:**
```python
def load_data(filepath):
    # Load data from file
    pass

def explore_data(df):
    # Generate summary statistics
    pass
```

**preprocessor.py:**
```python
def handle_missing_values(df, strategy='mean'):
    # Handle missing values
    pass

def encode_categorical(df, columns):
    # Encode categorical variables
    pass

def scale_features(X_train, X_test):
    # Scale features
    pass
```

**feature_engineer.py:**
```python
def create_features(df):
    # Create new features
    pass

def select_features(X, y, method='correlation'):
    # Select important features
    pass
```

**model_trainer.py:**
```python
def train_models(X_train, y_train):
    # Train multiple models
    pass

def evaluate_models(models, X_test, y_test):
    # Evaluate models
    pass
```

**pipeline.py:**
```python
class MLPipeline:
    def fit(self, X, y):
        # Fit pipeline
        pass
    
    def predict(self, X):
        # Make predictions
        pass
```

### Testing Checklist
- [ ] Data loads correctly
- [ ] Preprocessing handles all edge cases
- [ ] Models train without errors
- [ ] Evaluation metrics calculated
- [ ] Pipeline works end-to-end

---

## 📚 Complete Tutorial (For Beginners)

> 💡 **Already familiar with ML pipelines?** See [Quick Start](#-quick-start-for-experienced-students) section above.

### Step 1: Understand the ML Pipeline (Day 1)

**📖 Course Connection:** Review `unit1-data-processing/examples/01_data_loading_exploration.ipynb` to understand data pipelines

**What is an ML Pipeline?**
A series of steps that transform raw data into predictions:

```
Raw Data → Clean Data → Process Features → Train Model → Make Predictions
```

**Why Pipeline?**
- ✅ Reusable: Use same steps for new data
- ✅ Organized: Each step has clear purpose
- ✅ Testable: Test each step separately
- ✅ Maintainable: Easy to update and fix

**Real-World Example:**
When Zillow estimates a house price, they:
1. Load house data (size, location, etc.)
2. Clean the data (fix errors)
3. Process features (normalize, encode)
4. Run through trained model
5. Get price prediction

---

### Step 2: Set Up Your Project (Day 1)

**Create this structure:**

```
ml_pipeline_project/
├── data/
│   └── house_prices.csv
├── src/
│   ├── data_loader.py
│   ├── preprocessor.py
│   ├── feature_engineer.py
│   ├── model_trainer.py
│   └── pipeline.py
├── models/
│   └── (saved models will go here)
├── results/
│   └── (plots and reports will go here)
├── main.py
├── requirements.txt
└── README.md
```

**Install libraries:**
```bash
pip install pandas numpy scikit-learn matplotlib seaborn
```

---

### Step 3: Create Data Loader (Day 2)

**📖 Course Connection:** Review `unit1-data-processing/examples/01_data_loading_exploration.ipynb` for data loading techniques

**File: `src/data_loader.py`**

```python
import pandas as pd
import numpy as np

class DataLoader:
    """Loads and explores data"""
    
    def __init__(self, filepath):
        self.filepath = filepath
        self.data = None
    
    def load_data(self):
        """Load data from CSV file"""
        try:
            self.data = pd.read_csv(self.filepath)
            print(f"✅ Loaded {len(self.data)} rows, {len(self.data.columns)} columns")
            return self.data
        except Exception as e:
            print(f"❌ Error loading data: {e}")
            return None
    
    def explore_data(self):
        """Explore the data"""
        if self.data is None:
            print("❌ No data loaded")
            return
        
        print("\n" + "=" * 50)
        print("Data Overview")
        print("=" * 50)
        
        # Basic info
        print(f"\nShape: {self.data.shape}")
        print(f"\nColumns: {list(self.data.columns)}")
        
        # First few rows
        print("\nFirst 5 rows:")
        print(self.data.head())
        
        # Data types
        print("\nData types:")
        print(self.data.dtypes)
        
        # Missing values
        print("\nMissing values:")
        print(self.data.isnull().sum())
        
        # Statistics
        print("\nStatistics:")
        print(self.data.describe())
    
    def get_data(self):
        """Get loaded data"""
        return self.data
```

**Test it:**
```python
loader = DataLoader('data/house_prices.csv')
data = loader.load_data()
loader.explore_data()
```

---

### Step 4: Create Preprocessor (Day 3)

**📖 Course Connection:** Follow `unit1-data-processing/examples/02_data_cleaning.ipynb` and `03_data_preprocessing.ipynb` for preprocessing steps

**File: `src/preprocessor.py`**

```python
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder

class Preprocessor:
    """Preprocesses data for ML"""
    
    def __init__(self):
        self.scaler = StandardScaler()
        self.encoders = {}
    
    def handle_missing_values(self, df, strategy='mean'):
        """Handle missing values"""
        df_clean = df.copy()
        
        for col in df_clean.columns:
            if df_clean[col].isnull().sum() > 0:
                if strategy == 'mean' and df_clean[col].dtype in ['int64', 'float64']:
                    df_clean[col].fillna(df_clean[col].mean(), inplace=True)
                elif strategy == 'median' and df_clean[col].dtype in ['int64', 'float64']:
                    df_clean[col].fillna(df_clean[col].median(), inplace=True)
                elif strategy == 'mode':
                    df_clean[col].fillna(df_clean[col].mode()[0], inplace=True)
                else:
                    df_clean[col].fillna(0, inplace=True)
        
        print(f"✅ Handled missing values using {strategy}")
        return df_clean
    
    def encode_categorical(self, df, categorical_columns):
        """Encode categorical variables"""
        df_encoded = df.copy()
        
        for col in categorical_columns:
            if col in df_encoded.columns:
                le = LabelEncoder()
                df_encoded[col] = le.fit_transform(df_encoded[col].astype(str))
                self.encoders[col] = le
                print(f"✅ Encoded column: {col}")
        
        return df_encoded
    
    def scale_features(self, X_train, X_test):
        """Scale numerical features"""
        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)
        print("✅ Scaled features")
        return X_train_scaled, X_test_scaled
```

---

### Step 5: Create Feature Engineer (Day 4)

**📖 Course Connection:** Review `unit1-data-processing/examples/03_data_preprocessing.ipynb` for feature engineering

**File: `src/feature_engineer.py`**

```python
import pandas as pd
import numpy as np

class FeatureEngineer:
    """Creates and selects features"""
    
    def create_features(self, df):
        """Create new features from existing ones"""
        df_new = df.copy()
        
        # Example: Create area per room
        if 'area' in df_new.columns and 'bedrooms' in df_new.columns:
            df_new['area_per_bedroom'] = df_new['area'] / (df_new['bedrooms'] + 1)
        
        # Example: Create age feature (if year_built exists)
        if 'year_built' in df_new.columns:
            current_year = 2024
            df_new['house_age'] = current_year - df_new['year_built']
        
        print("✅ Created new features")
        return df_new
    
    def select_features(self, X, y, top_n=10):
        """Select most important features"""
        from sklearn.feature_selection import SelectKBest, f_regression
        
        selector = SelectKBest(score_func=f_regression, k=top_n)
        X_selected = selector.fit_transform(X, y)
        
        selected_features = X.columns[selector.get_support()]
        print(f"✅ Selected {len(selected_features)} features: {list(selected_features)}")
        
        return X_selected, selected_features
```

---

### Step 6: Create Model Trainer (Day 5)

**📖 Course Connection:** Follow `unit1-data-processing/examples/04_linear_regression.ipynb` for model training and evaluation

**File: `src/model_trainer.py`**

```python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd

class ModelTrainer:
    """Trains and evaluates ML models"""
    
    def __init__(self):
        self.models = {}
        self.results = {}
    
    def split_data(self, X, y, test_size=0.2):
        """Split data into train and test sets"""
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, random_state=42
        )
        print(f"✅ Split data: Train {len(X_train)}, Test {len(X_test)}")
        return X_train, X_test, y_train, y_test
    
    def train_models(self, X_train, y_train):
        """Train multiple models"""
        # Linear Regression
        lr = LinearRegression()
        lr.fit(X_train, y_train)
        self.models['Linear Regression'] = lr
        
        # Random Forest
        rf = RandomForestRegressor(n_estimators=100, random_state=42)
        rf.fit(X_train, y_train)
        self.models['Random Forest'] = rf
        
        print("✅ Trained models")
        return self.models
    
    def evaluate_models(self, X_test, y_test):
        """Evaluate all models"""
        results = {}
        
        for name, model in self.models.items():
            y_pred = model.predict(X_test)
            mse = mean_squared_error(y_test, y_pred)
            r2 = r2_score(y_test, y_pred)
            
            results[name] = {
                'MSE': mse,
                'RMSE': np.sqrt(mse),
                'R2': r2
            }
            
            print(f"\n{name}:")
            print(f"  MSE: {mse:.2f}")
            print(f"  RMSE: {np.sqrt(mse):.2f}")
            print(f"  R²: {r2:.4f}")
        
        self.results = results
        return results
    
    def get_best_model(self):
        """Get the best performing model"""
        if not self.results:
            return None
        
        best_name = max(self.results, key=lambda x: self.results[x]['R2'])
        return self.models[best_name], best_name
```

---

### Step 7: Create Pipeline Class (Day 6)

**File: `src/pipeline.py`**

```python
from data_loader import DataLoader
from preprocessor import Preprocessor
from feature_engineer import FeatureEngineer
from model_trainer import ModelTrainer

class MLPipeline:
    """Complete ML Pipeline"""
    
    def __init__(self, data_path):
        self.data_path = data_path
        self.loader = DataLoader(data_path)
        self.preprocessor = Preprocessor()
        self.feature_engineer = FeatureEngineer()
        self.trainer = ModelTrainer()
        self.best_model = None
    
    def run(self, target_column):
        """Run complete pipeline"""
        print("=" * 60)
        print("Starting ML Pipeline")
        print("=" * 60)
        
        # Step 1: Load data
        print("\n[Step 1] Loading data...")
        data = self.loader.load_data()
        self.loader.explore_data()
        
        # Step 2: Preprocess
        print("\n[Step 2] Preprocessing...")
        data = self.preprocessor.handle_missing_values(data)
        
        # Separate features and target
        X = data.drop(columns=[target_column])
        y = data[target_column]
        
        # Encode categorical
        categorical_cols = X.select_dtypes(include=['object']).columns
        if len(categorical_cols) > 0:
            X = self.preprocessor.encode_categorical(X, categorical_cols)
        
        # Step 3: Feature engineering
        print("\n[Step 3] Feature engineering...")
        X = self.feature_engineer.create_features(X)
        
        # Step 4: Split data
        print("\n[Step 4] Splitting data...")
        X_train, X_test, y_train, y_test = self.trainer.split_data(X, y)
        
        # Scale features
        X_train_scaled, X_test_scaled = self.preprocessor.scale_features(X_train, X_test)
        
        # Step 5: Train models
        print("\n[Step 5] Training models...")
        self.trainer.train_models(X_train_scaled, y_train)
        
        # Step 6: Evaluate
        print("\n[Step 6] Evaluating models...")
        results = self.trainer.evaluate_models(X_test_scaled, y_test)
        
        # Get best model
        self.best_model, best_name = self.trainer.get_best_model()
        print(f"\n✅ Best model: {best_name}")
        
        return results
    
    def predict(self, new_data):
        """Make predictions on new data"""
        if self.best_model is None:
            print("❌ No model trained yet")
            return None
        
        predictions = self.best_model.predict(new_data)
        return predictions
```

---

### Step 8: Create Main Program (Day 7)

**File: `main.py`**

```python
from src.pipeline import MLPipeline

def main():
    # Create pipeline
    pipeline = MLPipeline('data/house_prices.csv')
    
    # Run pipeline
    results = pipeline.run(target_column='price')
    
    print("\n" + "=" * 60)
    print("Pipeline Complete!")
    print("=" * 60)
    print("\nYou can now use pipeline.predict() for new predictions")

if __name__ == "__main__":
    main()
```

---

## 🔗 Course Content Connections

### How This Project Connects to Course Content

| Project Step | Course Notebook | What You Learn |
|-------------|----------------|----------------|
| **Data Loading** | `unit1-data-processing/examples/01_data_loading_exploration.ipynb` | How to load and explore data |
| **Data Cleaning** | `unit1-data-processing/examples/02_data_cleaning.ipynb` | How to handle missing values and outliers |
| **Preprocessing** | `unit1-data-processing/examples/03_data_preprocessing.ipynb` | How to encode and scale features |
| **Model Training** | `unit1-data-processing/examples/04_linear_regression.ipynb` | How to train and evaluate models |
| **Pipeline** | `unit1-data-processing/examples/05_polynomial_regression.ipynb` | How to create reusable pipelines |

### Learning Path
1. Complete Unit 1 examples first
2. Understand each step individually
3. Then build the complete pipeline
4. Apply to your own dataset

---

## 🐛 Troubleshooting

### Problem: Data Loading Fails
**Error:** `FileNotFoundError` or `UnicodeDecodeError`  
**Solution:**
- Check file path is correct
- Ensure file is CSV format
- Check file encoding (try `encoding='utf-8'`)

### Problem: Missing Values Cause Errors
**Error:** `ValueError: Input contains NaN`  
**Solution:**
- Use `handle_missing_values()` before training
- Check which columns have missing values
- Choose appropriate strategy (mean, median, mode)

### Problem: Model Training is Slow
**Error:** Takes too long  
**Solution:**
- Reduce dataset size for testing
- Use simpler models first
- Check for memory issues

### Problem: Low Model Performance
**Error:** R² score is very low  
**Solution:**
- Try feature engineering
- Check for data quality issues
- Try different models
- Tune hyperparameters

### Problem: Pipeline Breaks
**Error:** Pipeline fails at certain step  
**Solution:**
- Test each step individually
- Check data types between steps
- Ensure all dependencies are installed

---

## 🎓 Learning Checklist

### Week 1: Foundation
- [ ] Day 1: Understand ML pipeline concept
- [ ] Day 2: Create data loader
- [ ] Day 3: Create preprocessor
- [ ] Day 4: Create feature engineer

### Week 2: Implementation
- [ ] Day 5: Create model trainer
- [ ] Day 6: Create pipeline class
- [ ] Day 7: Test complete pipeline
- [ ] Day 8: Add visualizations

### Week 3: Enhancement
- [ ] Day 9: Improve error handling
- [ ] Day 10: Write documentation
- [ ] Day 11: Test with different datasets
- [ ] Day 12: Finalize and submit

---

## 📊 Evaluation Criteria

### Functionality (30%)
- Pipeline processes data correctly
- Models train successfully
- Predictions are generated
- All steps work together

### Code Quality (25%)
- Code is well-organized
- Functions are documented
- Error handling included
- Follows best practices

### Model Performance (20%)
- Models achieve reasonable performance
- Evaluation metrics calculated
- Best model selected
- Results documented

### Documentation (15%)
- README explains project
- Code is commented
- Results are documented
- Usage examples provided

### Creativity (10%)
- Additional features added
- Creative solutions
- Improved performance
- Unique approaches

---

## 💡 Tips for Success

1. **Start Simple:** Begin with small dataset
2. **Test Often:** Test each step as you build
3. **Use Course Content:** Reference course notebooks
4. **Ask Questions:** Don't struggle alone
5. **Be Creative:** Add your own improvements

---

## 📖 Resources

### Course Content
- Unit 1: Data Processing & Regression
- Unit 2: Advanced Regression
- Unit 3: Classification Techniques
- Unit 5: Model Selection & Boosting

### External Resources
- scikit-learn Pipeline documentation
- pandas documentation
- NumPy documentation

---

**Good luck building your ML pipeline!** 🚀
