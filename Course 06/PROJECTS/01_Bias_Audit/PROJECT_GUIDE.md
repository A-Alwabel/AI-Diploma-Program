# Complete Project Guide: AI Bias Audit Tool

---

## 🎯 Real-World Application

### Example: Hiring System Bias Detection
**Imagine you're building a tool to audit AI systems used in hiring, like those used by companies to screen job applicants.**

**Problem:** AI hiring systems can be biased against certain groups:
- May favor certain demographics
- Can discriminate based on gender, race, age
- May have unfair accuracy differences across groups
- Need to detect and fix these biases

**Solution:** Your bias audit tool:
1. **Detects** bias in ML models
2. **Measures** fairness across different groups
3. **Visualizes** bias patterns
4. **Mitigates** bias using various techniques
5. **Reports** findings and recommendations

**Real-World Impact:**
- ✅ Fair hiring practices
- ✅ Legal compliance (anti-discrimination laws)
- ✅ Better model performance for all groups
- ✅ Trust in AI systems

**Similar Systems:**
- Hiring platforms (LinkedIn, Indeed)
- Loan approval systems (banks)
- Healthcare AI (diagnosis systems)
- Criminal justice (risk assessment)

---

## 🚀 Quick Start (For Experienced Students)

> 💡 **New to bias detection?** Skip to [Complete Tutorial](#-complete-tutorial-for-beginners) section below.

### Project Structure
```
bias_audit_tool/
├── bias_detector.py      # Bias detection
├── fairness_metrics.py   # Fairness calculations
├── mitigator.py          # Bias mitigation
├── reporter.py           # Report generation
├── visualizer.py         # Visualizations
├── main.py               # Main program
└── README.md
```

### Key Functions to Implement

**fairness_metrics.py:**
```python
def demographic_parity(y_pred, protected_attribute):
    """Calculate demographic parity"""
    pass

def equalized_odds(y_true, y_pred, protected_attribute):
    """Calculate equalized odds"""
    pass

def calibration(y_true, y_pred, protected_attribute):
    """Measure calibration"""
    pass
```

**bias_detector.py:**
```python
class BiasDetector:
    def detect_bias(self, model, X, y, protected_attr):
        """Detect bias in model"""
        pass
    
    def analyze_per_group(self, model, X, y, protected_attr):
        """Analyze performance per group"""
        pass
```

**mitigator.py:**
```python
class BiasMitigator:
    def preprocess(self, X, y, protected_attr):
        """Pre-processing mitigation"""
        pass
    
    def inprocess(self, model, X, y, protected_attr):
        """In-processing mitigation"""
        pass
    
    def postprocess(self, model, X, y, protected_attr):
        """Post-processing mitigation"""
        pass
```

---

## 📚 Complete Tutorial (For Beginners)

> 💡 **Already familiar with bias detection?** See [Quick Start](#-quick-start-for-experienced-students) section above.

### Step 1: Understand Bias in AI (Day 1)

**📖 Course Connection:** Review `unit1-ethics-foundations/examples/01_ethical_frameworks.ipynb` to understand AI ethics

**What is Bias in AI?**
Bias occurs when an AI system treats different groups unfairly:
- **Demographic Bias:** Different outcomes for different groups
- **Performance Bias:** Different accuracy for different groups
- **Representation Bias:** Training data doesn't represent all groups

**Example:**
A hiring system that:
- Accepts 80% of male applicants
- Accepts only 40% of female applicants
- Has bias against women

**Why It Matters:**
- ✅ Legal compliance (anti-discrimination laws)
- ✅ Ethical responsibility
- ✅ Better model performance
- ✅ Trust in AI systems

---

### Step 2: Set Up Project (Day 1)

**Create structure:**
```
bias_audit_tool/
├── bias_detector.py
├── fairness_metrics.py
├── mitigator.py
├── reporter.py
├── visualizer.py
├── main.py
└── README.md
```

**Install libraries:**
```bash
pip install pandas numpy scikit-learn matplotlib seaborn
```

---

### Step 3: Implement Fairness Metrics (Day 2-3)

**📖 Course Connection:** Review `unit2-fairness-metrics/examples/01_fairness_metrics.ipynb` for fairness calculations

**File: `fairness_metrics.py`**

```python
import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix

def demographic_parity(y_pred, protected_attribute):
    """
    Calculate demographic parity.
    P(Ŷ=1 | Group=A) = P(Ŷ=1 | Group=B)
    """
    df = pd.DataFrame({
        'pred': y_pred,
        'group': protected_attribute
    })
    
    # Calculate positive rate per group
    positive_rates = df.groupby('group')['pred'].mean()
    
    # Demographic parity = difference in positive rates
    max_rate = positive_rates.max()
    min_rate = positive_rates.min()
    parity = max_rate - min_rate
    
    return {
        'parity': parity,
        'rates': positive_rates.to_dict(),
        'is_fair': parity < 0.1  # Threshold
    }

def equalized_odds(y_true, y_pred, protected_attribute):
    """
    Calculate equalized odds.
    Equal TPR and FPR across groups
    """
    df = pd.DataFrame({
        'true': y_true,
        'pred': y_pred,
        'group': protected_attribute
    })
    
    groups = df['group'].unique()
    results = {}
    
    for group in groups:
        group_data = df[df['group'] == group]
        tn, fp, fn, tp = confusion_matrix(
            group_data['true'], 
            group_data['pred']
        ).ravel()
        
        tpr = tp / (tp + fn) if (tp + fn) > 0 else 0
        fpr = fp / (fp + tn) if (fp + tn) > 0 else 0
        
        results[group] = {
            'TPR': tpr,
            'FPR': fpr
        }
    
    # Equalized odds = max difference in TPR and FPR
    tprs = [r['TPR'] for r in results.values()]
    fprs = [r['FPR'] for r in results.values()]
    
    tpr_diff = max(tprs) - min(tprs)
    fpr_diff = max(fprs) - min(fprs)
    
    return {
        'tpr_difference': tpr_diff,
        'fpr_difference': fpr_diff,
        'is_fair': tpr_diff < 0.1 and fpr_diff < 0.1,
        'per_group': results
    }
```

---

### Step 4: Create Bias Detector (Day 4)

**File: `bias_detector.py`**

```python
from fairness_metrics import demographic_parity, equalized_odds
import pandas as pd

class BiasDetector:
    """Detect bias in ML models"""
    
    def __init__(self):
        self.metrics = {}
    
    def detect_bias(self, model, X, y, protected_attribute):
        """Detect bias in model predictions"""
        # Get predictions
        y_pred = model.predict(X)
        
        # Calculate fairness metrics
        dp_result = demographic_parity(y_pred, protected_attribute)
        eo_result = equalized_odds(y, y_pred, protected_attribute)
        
        self.metrics = {
            'demographic_parity': dp_result,
            'equalized_odds': eo_result
        }
        
        # Determine if biased
        is_biased = not (dp_result['is_fair'] and eo_result['is_fair'])
        
        return {
            'is_biased': is_biased,
            'metrics': self.metrics
        }
    
    def analyze_per_group(self, model, X, y, protected_attribute):
        """Analyze performance per group"""
        y_pred = model.predict(X)
        
        df = pd.DataFrame({
            'true': y,
            'pred': y_pred,
            'group': protected_attribute
        })
        
        results = {}
        for group in df['group'].unique():
            group_data = df[df['group'] == group]
            accuracy = (group_data['true'] == group_data['pred']).mean()
            results[group] = {
                'accuracy': accuracy,
                'count': len(group_data)
            }
        
        return results
```

---

### Step 5: Implement Bias Mitigation (Day 5-6)

**File: `mitigator.py`**

```python
from sklearn.preprocessing import StandardScaler
import pandas as pd

class BiasMitigator:
    """Mitigate bias in ML models"""
    
    def preprocess_reweighing(self, X, y, protected_attribute):
        """
        Pre-processing: Reweighing
        Adjust sample weights to balance groups
        """
        df = pd.DataFrame(X)
        df['target'] = y
        df['group'] = protected_attribute
        
        # Calculate weights
        group_counts = df.groupby(['group', 'target']).size()
        total_counts = df.groupby('target').size()
        
        weights = []
        for idx, row in df.iterrows():
            group = row['group']
            target = row['target']
            weight = total_counts[target] / group_counts[(group, target)]
            weights.append(weight)
        
        return X, y, weights
    
    def postprocess_threshold(self, model, X, y, protected_attribute, threshold=0.5):
        """
        Post-processing: Adjust thresholds per group
        """
        y_proba = model.predict_proba(X)[:, 1]
        
        df = pd.DataFrame({
            'proba': y_proba,
            'group': protected_attribute
        })
        
        # Adjust thresholds per group to achieve fairness
        adjusted_preds = []
        for group in df['group'].unique():
            group_proba = df[df['group'] == group]['proba']
            # Use group-specific threshold
            group_threshold = group_proba.quantile(1 - threshold)
            group_preds = (group_proba >= group_threshold).astype(int)
            adjusted_preds.extend(group_preds)
        
        return adjusted_preds
```

---

### Step 6: Create Visualizations (Day 7)

**File: `visualizer.py`**

```python
import matplotlib.pyplot as plt
import seaborn as sns

class BiasVisualizer:
    """Visualize bias patterns"""
    
    def plot_fairness_metrics(self, metrics):
        """Plot fairness metrics"""
        fig, axes = plt.subplots(1, 2, figsize=(12, 5))
        
        # Demographic Parity
        dp = metrics['demographic_parity']
        groups = list(dp['rates'].keys())
        rates = list(dp['rates'].values())
        
        axes[0].bar(groups, rates)
        axes[0].set_title('Demographic Parity')
        axes[0].set_ylabel('Positive Rate')
        axes[0].axhline(y=dp['rates'][groups[0]], color='r', linestyle='--', label='Target')
        
        # Equalized Odds
        eo = metrics['equalized_odds']
        groups = list(eo['per_group'].keys())
        tprs = [eo['per_group'][g]['TPR'] for g in groups]
        fprs = [eo['per_group'][g]['FPR'] for g in groups]
        
        x = range(len(groups))
        width = 0.35
        axes[1].bar([i - width/2 for i in x], tprs, width, label='TPR')
        axes[1].bar([i + width/2 for i in x], fprs, width, label='FPR')
        axes[1].set_title('Equalized Odds')
        axes[1].set_xticks(x)
        axes[1].set_xticklabels(groups)
        axes[1].legend()
        
        plt.tight_layout()
        return fig
```

---

### Step 7: Generate Report (Day 8)

**File: `reporter.py`**

```python
class BiasReporter:
    """Generate bias audit reports"""
    
    def generate_report(self, detector, mitigator_results=None):
        """Generate comprehensive audit report"""
        report = []
        report.append("=" * 60)
        report.append("BIAS AUDIT REPORT")
        report.append("=" * 60)
        report.append("")
        
        # Bias Detection Results
        report.append("## Bias Detection Results")
        metrics = detector.metrics
        
        dp = metrics['demographic_parity']
        report.append(f"\nDemographic Parity: {dp['parity']:.4f}")
        report.append(f"Fair: {dp['is_fair']}")
        report.append(f"Rates per group: {dp['rates']}")
        
        eo = metrics['equalized_odds']
        report.append(f"\nEqualized Odds:")
        report.append(f"TPR Difference: {eo['tpr_difference']:.4f}")
        report.append(f"FPR Difference: {eo['fpr_difference']:.4f}")
        report.append(f"Fair: {eo['is_fair']}")
        
        # Recommendations
        report.append("\n## Recommendations")
        if not dp['is_fair']:
            report.append("- Apply demographic parity constraints")
        if not eo['is_fair']:
            report.append("- Use equalized odds optimization")
        
        if mitigator_results:
            report.append("\n## Mitigation Results")
            report.append(f"Bias reduced: {mitigator_results['improvement']}")
        
        return "\n".join(report)
```

---

## 🔗 Course Content Connections

### How This Project Connects to Course Content

| Project Step | Course Notebook | What You Learn |
|-------------|----------------|----------------|
| **Ethics Foundations** | `unit1-ethics-foundations/examples/01_ethical_frameworks.ipynb` | Understanding AI ethics |
| **Fairness Metrics** | `unit2-fairness-metrics/examples/01_fairness_metrics.ipynb` | Calculating fairness |
| **Bias Detection** | `unit2-fairness-metrics/examples/02_bias_detection.ipynb` | Detecting bias |
| **Bias Mitigation** | `unit3-bias-mitigation/examples/01_mitigation_techniques.ipynb` | Fixing bias |

---

## 🐛 Troubleshooting

### Problem: Metrics calculation fails
**Error:** Division by zero or NaN values  
**Solution:** Check for groups with no samples, handle edge cases

### Problem: Mitigation doesn't work
**Error:** Bias still present after mitigation  
**Solution:** Try different mitigation techniques, adjust parameters

### Problem: Visualizations don't show
**Error:** Plots not displaying  
**Solution:** Call `plt.show()` or save figures

---

## 🎓 Learning Checklist

- [ ] Day 1: Understand bias in AI
- [ ] Day 2-3: Implement fairness metrics
- [ ] Day 4: Create bias detector
- [ ] Day 5-6: Implement mitigation techniques
- [ ] Day 7: Create visualizations
- [ ] Day 8: Generate reports
- [ ] Day 9: Test with different datasets
- [ ] Day 10: Write documentation

---

**Good luck building your bias audit tool!** 🚀