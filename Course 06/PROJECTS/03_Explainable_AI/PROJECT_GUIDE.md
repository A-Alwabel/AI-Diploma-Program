# Complete Project Guide: Explainable AI Tool

---

## 🎯 Real-World Application

### Example: Loan Approval Explanation System
**Imagine you're building a system for banks to explain why loan applications are approved or rejected, like systems used by financial institutions.**

**Problem:** Banks use AI to approve loans, but need to:
- Explain decisions to customers (legal requirement)
- Understand why certain features matter
- Debug model behavior
- Build trust with customers

**Solution:** Your explainable AI tool:
1. **Explains** model predictions using SHAP and LIME
2. **Visualizes** feature importance
3. **Generates** human-readable explanations
4. **Shows** decision boundaries
5. **Creates** explanation reports

**Real-World Impact:**
- ✅ Legal compliance (right to explanation)
- ✅ Customer trust
- ✅ Model debugging
- ✅ Better model understanding

**Similar Systems:**
- Loan approval systems (banks)
- Medical diagnosis (hospitals)
- Credit scoring (financial services)
- Hiring decisions (HR systems)

---

## 🚀 Quick Start (For Experienced Students)

> 💡 **New to explainable AI?** Skip to [Complete Tutorial](#-complete-tutorial-for-beginners) section below.

### Project Structure
```
explainable_ai_tool/
├── explainer.py        # SHAP, LIME implementations
├── visualizer.py       # Explanation visualizations
├── reporter.py         # Report generation
├── feature_importance.py  # Feature importance analysis
├── main.py             # Main program
└── README.md
```

### Key Functions to Implement

**explainer.py:**
```python
import shap
from lime.lime_tabular import LimeTabularExplainer

def explain_with_shap(model, X, feature_names):
    """Generate SHAP explanations"""
    pass

def explain_with_lime(model, X, instance, feature_names):
    """Generate LIME explanations"""
    pass
```

**visualizer.py:**
```python
def plot_shap_summary(shap_values, X, feature_names):
    """Plot SHAP summary"""
    pass

def plot_feature_importance(importance_dict):
    """Plot feature importance"""
    pass
```

**reporter.py:**
```python
def generate_explanation_report(explanation, instance, prediction):
    """Generate human-readable report"""
    pass
```

---

## 📚 Complete Tutorial (For Beginners)

> 💡 **Already familiar with explainable AI?** See [Quick Start](#-quick-start-for-experienced-students) section above.

### Step 1: Understand Explainable AI (Day 1)

**📖 Course Connection:** Review `unit1-ethics-foundations/examples/03_explainability_ethics.ipynb` to understand explainability

**What is Explainable AI?**
AI systems that can explain their decisions:
- **Global Explanations:** How the model works overall
- **Local Explanations:** Why a specific prediction was made
- **Feature Importance:** Which features matter most
- **Decision Boundaries:** How the model separates classes

**Example:**
A loan approval model:
- **Without Explanation:** "Loan denied" (no reason!)
- **With Explanation:** "Loan denied because: low credit score (400), high debt-to-income ratio (0.8), insufficient income ($30k)"

**Why It Matters:**
- ✅ Legal requirement (GDPR right to explanation)
- ✅ User trust
- ✅ Model debugging
- ✅ Fairness verification

---

### Step 2: Set Up Project (Day 1)

**Create structure:**
```
explainable_ai_tool/
├── explainer.py
├── visualizer.py
├── reporter.py
├── feature_importance.py
├── main.py
└── README.md
```

**Install libraries:**
```bash
pip install pandas numpy scikit-learn shap lime matplotlib seaborn
```

---

### Step 3: Implement SHAP Explanations (Day 2-3)

**📖 Course Connection:** Review `unit2-explainability-methods/examples/01_shap_explanations.ipynb` for SHAP

**File: `explainer.py`**

```python
import shap
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

class ExplainableAI:
    """Explainable AI using SHAP and LIME"""
    
    def __init__(self, model, X_train, feature_names=None):
        self.model = model
        self.X_train = X_train
        self.feature_names = feature_names or [f'Feature_{i}' for i in range(X_train.shape[1])]
        self.shap_explainer = None
    
    def explain_with_shap(self, X_explain, explanation_type='tree'):
        """
        Generate SHAP explanations
        
        explanation_type: 'tree' for tree models, 'kernel' for others
        """
        if explanation_type == 'tree':
            # For tree-based models (Random Forest, XGBoost)
            self.shap_explainer = shap.TreeExplainer(self.model)
        else:
            # For other models
            self.shap_explainer = shap.KernelExplainer(
                self.model.predict_proba,
                self.X_train[:100]  # Sample for speed
            )
        
        # Calculate SHAP values
        shap_values = self.shap_explainer.shap_values(X_explain)
        
        return {
            'shap_values': shap_values,
            'explainer': self.shap_explainer,
            'feature_names': self.feature_names
        }
    
    def explain_with_lime(self, X_explain, num_features=5):
        """
        Generate LIME explanations for specific instances
        """
        from lime.lime_tabular import LimeTabularExplainer
        
        # Create LIME explainer
        lime_explainer = LimeTabularExplainer(
            self.X_train,
            feature_names=self.feature_names,
            mode='classification'
        )
        
        explanations = []
        for i, instance in enumerate(X_explain):
            # Explain this instance
            explanation = lime_explainer.explain_instance(
                instance,
                self.model.predict_proba,
                num_features=num_features
            )
            
            explanations.append({
                'instance_idx': i,
                'explanation': explanation,
                'prediction': self.model.predict([instance])[0],
                'probability': self.model.predict_proba([instance])[0]
            })
        
        return explanations
    
    def get_feature_importance(self, shap_values):
        """Extract feature importance from SHAP values"""
        if isinstance(shap_values, list):
            # For multi-class, use first class
            shap_values = shap_values[0]
        
        # Mean absolute SHAP value per feature
        importance = np.abs(shap_values).mean(axis=0)
        
        importance_dict = dict(zip(self.feature_names, importance))
        return dict(sorted(importance_dict.items(), key=lambda x: x[1], reverse=True))
```

---

### Step 4: Create Visualizations (Day 4-5)

**File: `visualizer.py`**

```python
import matplotlib.pyplot as plt
import shap
import numpy as np

class ExplanationVisualizer:
    """Visualize AI explanations"""
    
    def plot_shap_summary(self, shap_values, X, feature_names, max_display=10):
        """Plot SHAP summary plot"""
        if isinstance(shap_values, list):
            shap_values = shap_values[0]  # Use first class for binary
        
        shap.summary_plot(shap_values, X, feature_names=feature_names, max_display=max_display, show=False)
        plt.tight_layout()
        return plt.gcf()
    
    def plot_shap_waterfall(self, shap_values, instance, feature_names, max_display=10):
        """Plot SHAP waterfall for single instance"""
        if isinstance(shap_values, list):
            shap_values = shap_values[0]
        
        shap.waterfall_plot(
            shap.Explanation(
                values=shap_values[instance],
                base_values=0,  # Adjust based on your model
                data=X[instance],
                feature_names=feature_names
            ),
            max_display=max_display,
            show=False
        )
        plt.tight_layout()
        return plt.gcf()
    
    def plot_feature_importance(self, importance_dict, top_n=10):
        """Plot feature importance bar chart"""
        top_features = dict(list(importance_dict.items())[:top_n])
        
        fig, ax = plt.subplots(figsize=(10, 6))
        features = list(top_features.keys())
        importance = list(top_features.values())
        
        ax.barh(features, importance)
        ax.set_xlabel('Importance')
        ax.set_title('Feature Importance (Top 10)')
        ax.invert_yaxis()
        
        plt.tight_layout()
        return fig
    
    def plot_lime_explanation(self, lime_explanation, save_path=None):
        """Plot LIME explanation"""
        fig = lime_explanation.as_pyplot_figure()
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path)
        
        return fig
```

---

### Step 5: Generate Explanation Reports (Day 6)

**File: `reporter.py`**

```python
class ExplanationReporter:
    """Generate explanation reports"""
    
    def generate_text_explanation(self, instance, prediction, shap_values, feature_names, top_n=5):
        """Generate human-readable text explanation"""
        if isinstance(shap_values, list):
            shap_values = shap_values[0]
        
        # Get SHAP values for this instance
        instance_shap = shap_values[instance]
        
        # Sort features by absolute SHAP value
        feature_contributions = list(zip(feature_names, instance_shap))
        feature_contributions.sort(key=lambda x: abs(x[1]), reverse=True)
        
        # Build explanation
        explanation = []
        explanation.append(f"Prediction: {prediction}")
        explanation.append("")
        explanation.append("Top contributing features:")
        
        for i, (feature, contribution) in enumerate(feature_contributions[:top_n], 1):
            direction = "increases" if contribution > 0 else "decreases"
            explanation.append(
                f"{i}. {feature}: {abs(contribution):.4f} ({direction} prediction)"
            )
        
        return "\n".join(explanation)
    
    def generate_lime_text(self, lime_explanation, instance_idx):
        """Generate text from LIME explanation"""
        explanation = []
        explanation.append(f"Explanation for instance {instance_idx}:")
        explanation.append("")
        
        # Get explanation as list
        exp_list = lime_explanation.as_list()
        
        explanation.append("Top contributing features:")
        for i, (feature, weight) in enumerate(exp_list, 1):
            direction = "supports" if weight > 0 else "contradicts"
            explanation.append(f"{i}. {feature}: {weight:.4f} ({direction})")
        
        return "\n".join(explanation)
    
    def generate_full_report(self, model, X, y, X_explain, feature_names):
        """Generate comprehensive explanation report"""
        from explainer import ExplainableAI
        from visualizer import ExplanationVisualizer
        
        explainer = ExplainableAI(model, X, feature_names)
        visualizer = ExplanationVisualizer()
        
        report = []
        report.append("=" * 60)
        report.append("EXPLAINABLE AI REPORT")
        report.append("=" * 60)
        report.append("")
        
        # SHAP Explanations
        report.append("## SHAP Explanations")
        shap_result = explainer.explain_with_shap(X_explain)
        feature_importance = explainer.get_feature_importance(shap_result['shap_values'])
        
        report.append("\nTop 5 Most Important Features:")
        for i, (feature, importance) in enumerate(list(feature_importance.items())[:5], 1):
            report.append(f"{i}. {feature}: {importance:.4f}")
        
        # LIME Explanations
        report.append("\n## LIME Explanations")
        lime_explanations = explainer.explain_with_lime(X_explain[:3])  # First 3 instances
        
        for lime_exp in lime_explanations:
            report.append(f"\nInstance {lime_exp['instance_idx']}:")
            report.append(f"Prediction: {lime_exp['prediction']}")
            report.append(f"Probability: {lime_exp['probability']}")
        
        # Model Performance
        from sklearn.metrics import accuracy_score, classification_report
        y_pred = model.predict(X_explain)
        accuracy = accuracy_score(y[:len(X_explain)], y_pred)
        
        report.append("\n## Model Performance")
        report.append(f"Accuracy: {accuracy:.4f}")
        
        return "\n".join(report)
```

---

### Step 6: Create Main Program (Day 7-8)

**File: `main.py`**

```python
from explainer import ExplainableAI
from visualizer import ExplanationVisualizer
from reporter import ExplanationReporter
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

def main():
    # Generate sample data (replace with your data)
    X, y = make_classification(
        n_samples=1000,
        n_features=10,
        n_informative=5,
        n_redundant=2,
        random_state=42
    )
    
    feature_names = [f'Feature_{i}' for i in range(X.shape[1])]
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    print("=" * 60)
    print("Explainable AI Tool")
    print("=" * 60)
    
    # Step 1: Train Model
    print("\n[Step 1] Training Model...")
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    accuracy = model.score(X_test, y_test)
    print(f"Model accuracy: {accuracy:.4f}")
    
    # Step 2: Create Explainer
    print("\n[Step 2] Creating Explainer...")
    explainer = ExplainableAI(model, X_train, feature_names)
    
    # Step 3: Generate SHAP Explanations
    print("\n[Step 3] Generating SHAP Explanations...")
    X_explain = X_test[:5]  # Explain first 5 instances
    shap_result = explainer.explain_with_shap(X_explain)
    feature_importance = explainer.get_feature_importance(shap_result['shap_values'])
    
    print("\nTop 5 Most Important Features (SHAP):")
    for i, (feature, importance) in enumerate(list(feature_importance.items())[:5], 1):
        print(f"{i}. {feature}: {importance:.4f}")
    
    # Step 4: Generate LIME Explanations
    print("\n[Step 4] Generating LIME Explanations...")
    lime_explanations = explainer.explain_with_lime(X_explain[:3])
    
    for lime_exp in lime_explanations:
        print(f"\nInstance {lime_exp['instance_idx']}:")
        print(f"  Prediction: {lime_exp['prediction']}")
        print(f"  Probability: {lime_exp['probability']}")
    
    # Step 5: Create Visualizations
    print("\n[Step 5] Creating Visualizations...")
    visualizer = ExplanationVisualizer()
    
    # SHAP summary plot
    shap_summary = visualizer.plot_shap_summary(
        shap_result['shap_values'],
        X_explain,
        feature_names
    )
    shap_summary.savefig('shap_summary.png', dpi=300, bbox_inches='tight')
    print("  ✅ Saved: shap_summary.png")
    
    # Feature importance plot
    importance_plot = visualizer.plot_feature_importance(feature_importance)
    importance_plot.savefig('feature_importance.png', dpi=300, bbox_inches='tight')
    print("  ✅ Saved: feature_importance.png")
    
    # Step 6: Generate Report
    print("\n[Step 6] Generating Explanation Report...")
    reporter = ExplanationReporter()
    
    # Text explanation for first instance
    first_prediction = model.predict([X_explain[0]])[0]
    text_explanation = reporter.generate_text_explanation(
        0, first_prediction, shap_result['shap_values'], feature_names
    )
    print("\nText Explanation for First Instance:")
    print(text_explanation)
    
    # Full report
    full_report = reporter.generate_full_report(
        model, X_train, y_train, X_explain, feature_names
    )
    
    with open('explanation_report.txt', 'w') as f:
        f.write(full_report)
    print("\n  ✅ Saved: explanation_report.txt")
    
    print("\n" + "=" * 60)
    print("Explainable AI Tool Complete!")
    print("=" * 60)

if __name__ == "__main__":
    main()
```

---

## 🔗 Course Content Connections

### How This Project Connects to Course Content

| Project Step | Course Notebook | What You Learn |
|-------------|----------------|----------------|
| **Explainability Ethics** | `unit1-ethics-foundations/examples/03_explainability_ethics.ipynb` | Why explainability matters |
| **SHAP Explanations** | `unit2-explainability-methods/examples/01_shap_explanations.ipynb` | SHAP implementation |
| **LIME Explanations** | `unit2-explainability-methods/examples/02_lime_explanations.ipynb` | LIME implementation |
| **Feature Importance** | `unit3-model-interpretation/examples/01_feature_importance.ipynb` | Feature analysis |

---

## 🐛 Troubleshooting

### Problem: SHAP too slow
**Error:** SHAP calculations take too long  
**Solution:** Use TreeExplainer for tree models, sample data for KernelExplainer

### Problem: LIME explanations unclear
**Error:** LIME shows confusing features  
**Solution:** Increase num_features, check data preprocessing

### Problem: Visualizations don't show
**Error:** Plots not displaying  
**Solution:** Call `plt.show()` or save figures with `savefig()`

### Problem: Feature names missing
**Error:** Features shown as numbers  
**Solution:** Provide feature_names when creating explainer

---

## 🎓 Learning Checklist

- [ ] Day 1: Understand explainable AI
- [ ] Day 2-3: Implement SHAP explanations
- [ ] Day 4-5: Create visualizations
- [ ] Day 6: Generate explanation reports
- [ ] Day 7-8: Test complete system
- [ ] Day 9: Test with different models
- [ ] Day 10: Write documentation

---

## 💡 Tips for Success

1. **Start Simple:** Use tree models (easier to explain)
2. **Use SHAP for Global:** Better for overall understanding
3. **Use LIME for Local:** Better for individual predictions
4. **Visualize Everything:** Plots help understanding
5. **Generate Reports:** Text explanations are user-friendly

---

**Good luck building your explainable AI tool!** 🚀