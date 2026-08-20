# Complete Project Guide: 02 Classification System

---

## 🎯 Real-World Application

---

## 🚀 Quick Start (For Experienced Students)

> 💡 **New to this project?** Skip to [Complete Tutorial](#-complete-tutorial-for-beginners) section below.

## Step-by-Step Implementation

---

## 📚 Complete Tutorial (For Beginners)

> 💡 **Already familiar with this?** See [Quick Start](#-quick-start-for-experienced-students) section above.

### Step 1: Understand Classification (Day 1)

**What is Classification?**
Predicting which category something belongs to:
- Email → Spam or Not Spam?
- Image → Cat, Dog, or Bird?
- Customer → Will Buy or Won't Buy?

**Example:**
```
Email features:
- Has "FREE" in subject → Likely spam
- From known sender → Likely not spam
- Has links → Could be spam
- Short message → Could be spam

Classification: Spam (95% confidence)
```

---

### Step 2: Set Up Project (Day 1)

**Create structure:**
```
classification_project/
├── data/
│   └── emails.csv
├── src/
│   ├── data_loader.py
│   ├── classifier.py
│   └── evaluator.py
├── models/
├── results/
├── main.py
└── README.md
```

**Install:**
```bash
pip install pandas numpy scikit-learn matplotlib seaborn
```

---

### Step 3: Load and Explore Data (Day 2)

**File: `src/data_loader.py`**

```python
import pandas as pd
from sklearn.model_selection import train_test_split

class DataLoader:
    def load_data(self, filepath):
        """Load classification dataset"""
        df = pd.read_csv(filepath)
        print(f"✅ Loaded {len(df)} samples")
        return df
    
    def prepare_data(self, df, target_column):
        """Prepare features and target"""
        X = df.drop(columns=[target_column])
        y = df[target_column]
        
        # Split data
        # random_state=123: Any number works (42, 123, 2024, etc.) - ensures reproducibility
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=123, stratify=y
        )
        
        print(f"✅ Train: {len(X_train)}, Test: {len(X_test)}")
        return X_train, X_test, y_train, y_test
```

---

### Step 4: Implement Classifiers (Day 3)

**File: `src/classifier.py`**

```python
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier

class ClassifierSystem:
    """Multiple classification algorithms"""
    
    def __init__(self):
        self.models = {}
    
    def train_all(self, X_train, y_train):
        """Train all classifiers"""
        
        # 1. Logistic Regression
        # random_state=123: Any number works - ensures reproducibility
        # max_iter=1000: Allow more iterations for convergence
        # Note: Logistic Regression uses sigmoid function to output probabilities (0-1)
        # - .predict() returns classes (0 or 1) using threshold 0.5
        # - .predict_proba() returns probabilities [P(Class 0), P(Class 1)]
        lr = LogisticRegression(random_state=123, max_iter=1000)
        lr.fit(X_train, y_train)
        self.models['Logistic Regression'] = lr
        
        # 2. Decision Tree
        # random_state=123: Ensures same results every run
        dt = DecisionTreeClassifier(random_state=123)
        dt.fit(X_train, y_train)
        self.models['Decision Tree'] = dt
        
        # 3. SVM
        # random_state=123: Ensures reproducibility
        # probability=True: Enables .predict_proba() method
        svm = SVC(random_state=123, probability=True)
        svm.fit(X_train, y_train)
        self.models['SVM'] = svm
        
        # 4. Random Forest
        # random_state=123: Ensures reproducibility
        rf = RandomForestClassifier(n_estimators=100, random_state=123)
        rf.fit(X_train, y_train)
        self.models['Random Forest'] = rf
        
        print("✅ Trained all models")
        return self.models
```

---

### Step 5: Evaluate Models (Day 4)

**File: `src/evaluator.py`**

```python
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score,
    f1_score, confusion_matrix, classification_report
)
import matplotlib.pyplot as plt
import seaborn as sns

class ModelEvaluator:
    """Evaluate classification models"""
    
    def evaluate_all(self, models, X_test, y_test):
        """
        Evaluate all models
        
        ⚠️ IMPORTANT: Metrics are calculated AFTER training!
        - Step 1: Models were trained (in previous step)
        - Step 2: Models make predictions on test data
        - Step 3: NOW we calculate metrics by comparing predictions to actual labels
        - Step 4: Metrics tell us how well each model performs
        """
        results = {}
        
        for name, model in models.items():
            # Make predictions (AFTER training)
            y_pred = model.predict(X_test)
            
            # Calculate metrics (AFTER predictions exist)
            results[name] = {
                'accuracy': accuracy_score(y_test, y_pred),
                'precision': precision_score(y_test, y_pred, average='weighted'),
                'recall': recall_score(y_test, y_pred, average='weighted'),
                'f1': f1_score(y_test, y_pred, average='weighted')
            }
            
            print(f"\n{name}:")
            print(f"  Accuracy: {results[name]['accuracy']:.4f}")
            print(f"  Precision: {results[name]['precision']:.4f}")
            print(f"  Recall: {results[name]['recall']:.4f}")
            print(f"  F1-Score: {results[name]['f1']:.4f}")
        
        return results
    
    def plot_confusion_matrix(self, model, X_test, y_test, name):
        """
        Plot confusion matrix
        
        Understanding the confusion matrix:
        - TP (True Positive): Correctly predicted Class 1
        - TN (True Negative): Correctly predicted Class 0
        - FP (False Positive): Predicted Class 1, but actual is Class 0 (false alarm)
        - FN (False Negative): Predicted Class 0, but actual is Class 1 (missed detection)
        
        Matrix layout:
                Predicted
              Class 0  Class 1
        Actual  Class 0   TN     FP
                Class 1   FN     TP
        """
        y_pred = model.predict(X_test)
        cm = confusion_matrix(y_test, y_pred)
        
        plt.figure(figsize=(8, 6))
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                   xticklabels=['Class 0', 'Class 1'],
                   yticklabels=['Class 0', 'Class 1'])
        plt.title(f'Confusion Matrix - {name}')
        plt.ylabel('Actual Label')
        plt.xlabel('Predicted Label')
        plt.savefig(f'results/confusion_matrix_{name}.png')
        plt.close()
        
        # Print interpretation
        if cm.shape == (2, 2):  # Binary classification
            tn, fp, fn, tp = cm.ravel()
            print(f"\n{name} Confusion Matrix:")
            print(f"  TN (True Negative): {tn} - Correctly predicted Class 0")
            print(f"  FP (False Positive): {fp} - Predicted Class 1, but actual is Class 0")
            print(f"  FN (False Negative): {fn} - Predicted Class 0, but actual is Class 1")
            print(f"  TP (True Positive): {tp} - Correctly predicted Class 1")
```

---

### Step 6: Compare Models (Day 5)

**File: `main.py`**

```python
from src.data_loader import DataLoader
from src.classifier import ClassifierSystem
from src.evaluator import ModelEvaluator

def main():
    # Load data
    loader = DataLoader()
    df = loader.load_data('data/emails.csv')
    
    # Prepare data
    X_train, X_test, y_train, y_test = loader.prepare_data(df, 'label')
    
    # Train models
    classifier = ClassifierSystem()
    models = classifier.train_all(X_train, y_train)
    
    # Evaluate
    evaluator = ModelEvaluator()
    results = evaluator.evaluate_all(models, X_test, y_test)
    
    # Find best model
    best_model = max(results, key=lambda x: results[x]['f1'])
    print(f"\n✅ Best model: {best_model}")
    
    # Plot confusion matrices
    for name, model in models.items():
        evaluator.plot_confusion_matrix(model, X_test, y_test, name)

if __name__ == "__main__":
    main()
```

---

### Step 7: Understand and Use Metrics (Day 6)

**After evaluating models, use metrics to improve them!**

**The Improvement Cycle:**
1. Train model → Get metrics
2. Analyze metrics → Identify problems
3. Take action → Improve model
4. Re-train → Get new metrics
5. Compare → Better? Deploy! Worse? Try different approach

**Actions Based on Metrics:**

**If Accuracy is Low (< 70%):**
- Check data quality (missing values, outliers)
- Add more features
- Try different algorithms
- Check if problem is non-linear

**If Precision is Low (many false positives):**
- Increase classification threshold (make model more conservative)
- Add features that help distinguish false positives
- Use class weights if classes are imbalanced

**If Recall is Low (many false negatives):**
- Decrease classification threshold (make model more aggressive)
- Use `class_weight='balanced'` for imbalanced classes
- Add features that help catch missed cases

**Understanding TP, FP, TN, FN:**
- **TP (True Positive)**: Correctly predicted Class 1 ✅
- **TN (True Negative)**: Correctly predicted Class 0 ✅
- **FP (False Positive)**: Predicted Class 1, but actual is Class 0 ❌ (false alarm)
- **FN (False Negative)**: Predicted Class 0, but actual is Class 1 ❌ (missed detection)

**When to Use Which Metric:**
- **Accuracy**: When classes are balanced, equal cost of errors
- **Precision**: When false positives are costly (e.g., spam detection)
- **Recall**: When false negatives are costly (e.g., disease detection)
- **F1 Score**: When you need both precision and recall balanced

---

---