# Complete Project Guide: Privacy-Preserving ML System

---

## 🎯 Real-World Application

### Example: Healthcare Data Analysis with Privacy
**Imagine you're building an ML system for hospitals to analyze patient data while protecting privacy, like systems used for medical research.**

**Problem:** Healthcare organizations need to:
- Train ML models on sensitive patient data
- Share insights without exposing individual records
- Comply with GDPR, HIPAA privacy regulations
- Protect patient identities while maintaining model accuracy

**Solution:** Your privacy-preserving ML system:
1. **Applies** differential privacy to protect individual records
2. **Anonymizes** data before training
3. **Uses** federated learning concepts (train without sharing raw data)
4. **Ensures** GDPR compliance
5. **Balances** privacy and model utility

**Real-World Impact:**
- ✅ Patient privacy protected
- ✅ Legal compliance (GDPR, HIPAA)
- ✅ Medical research enabled
- ✅ Trust in healthcare AI

**Similar Systems:**
- Healthcare AI (patient diagnosis)
- Financial services (fraud detection)
- Government analytics (census data)
- Social media (user behavior analysis)

---

## 🚀 Quick Start (For Experienced Students)

> 💡 **New to privacy-preserving ML?** Skip to [Complete Tutorial](#-complete-tutorial-for-beginners) section below.

### Project Structure
```
privacy_ml_system/
├── privacy_techniques.py  # Differential privacy, anonymization
├── private_ml.py          # Privacy-preserving ML models
├── compliance.py           # GDPR compliance checks
├── evaluator.py            # Privacy-utility tradeoff
├── main.py                 # Main program
└── README.md
```

### Key Functions to Implement

**privacy_techniques.py:**
```python
def add_laplace_noise(data, epsilon):
    """Add Laplace noise for differential privacy"""
    pass

def k_anonymize(data, k):
    """Apply k-anonymity"""
    pass

def differential_privacy_query(query_result, epsilon):
    """Apply differential privacy to query"""
    pass
```

**private_ml.py:**
```python
from diffprivlib.models import LogisticRegression

class PrivateML:
    def train_private_model(self, X, y, epsilon):
        """Train model with differential privacy"""
        pass
    
    def evaluate_privacy_loss(self, model):
        """Calculate privacy budget used"""
        pass
```

**compliance.py:**
```python
class GDPRCompliance:
    def check_consent(self, data):
        """Check if data has consent"""
        pass
    
    def anonymize_pii(self, data):
        """Remove personally identifiable information"""
        pass
```

---

## 📚 Complete Tutorial (For Beginners)

> 💡 **Already familiar with privacy-preserving ML?** See [Quick Start](#-quick-start-for-experienced-students) section above.

### Step 1: Understand Privacy in ML (Day 1)

**📖 Course Connection:** Review `unit1-ethics-foundations/examples/02_privacy_ethics.ipynb` to understand privacy concepts

**What is Privacy-Preserving ML?**
Machine learning that protects individual data while still learning useful patterns:
- **Differential Privacy:** Add noise to protect individual records
- **K-Anonymity:** Generalize data so individuals can't be identified
- **Federated Learning:** Train models without sharing raw data
- **Homomorphic Encryption:** Compute on encrypted data

**Example:**
A hospital wants to train a model to predict disease risk:
- **Without Privacy:** Share all patient records (privacy violation!)
- **With Privacy:** Add noise, anonymize, or train locally

**Why It Matters:**
- ✅ Legal compliance (GDPR, HIPAA)
- ✅ Ethical responsibility
- ✅ User trust
- ✅ Enables data sharing

---

### Step 2: Set Up Project (Day 1)

**Create structure:**
```
privacy_ml_system/
├── privacy_techniques.py
├── private_ml.py
├── compliance.py
├── evaluator.py
├── main.py
└── README.md
```

**Install libraries:**
```bash
pip install pandas numpy scikit-learn diffprivlib matplotlib seaborn
```

---

### Step 3: Implement Differential Privacy (Day 2-3)

**📖 Course Connection:** Review `unit2-privacy-techniques/examples/01_differential_privacy.ipynb` for differential privacy

**File: `privacy_techniques.py`**

```python
import numpy as np
import pandas as pd

def add_laplace_noise(data, epsilon, sensitivity):
    """
    Add Laplace noise for differential privacy
    
    epsilon: Privacy parameter (smaller = more private)
    sensitivity: Maximum change in output
    """
    # Calculate noise scale
    scale = sensitivity / epsilon
    
    # Generate Laplace noise
    noise = np.random.laplace(0, scale, data.shape)
    
    # Add noise to data
    noisy_data = data + noise
    
    return noisy_data

def differential_privacy_query(query_result, epsilon, sensitivity):
    """
    Apply differential privacy to query result
    """
    noise = np.random.laplace(0, sensitivity / epsilon)
    private_result = query_result + noise
    
    return private_result

def k_anonymize(df, k, quasi_identifiers):
    """
    Apply k-anonymity
    
    k: Minimum number of records with same attributes
    quasi_identifiers: Columns that could identify individuals
    """
    df_anon = df.copy()
    
    # Generalize quasi-identifiers
    for col in quasi_identifiers:
        if df_anon[col].dtype in ['int64', 'float64']:
            # Generalize numeric: round to nearest 10
            df_anon[col] = (df_anon[col] / 10).astype(int) * 10
        else:
            # Generalize categorical: use first letter
            df_anon[col] = df_anon[col].astype(str).str[0]
    
    # Check k-anonymity
    groups = df_anon.groupby(quasi_identifiers).size()
    if (groups < k).any():
        # Further generalize if needed
        for col in quasi_identifiers:
            if df_anon[col].dtype in ['int64', 'float64']:
                df_anon[col] = (df_anon[col] / 100).astype(int) * 100
    
    return df_anon
```

---

### Step 4: Create Privacy-Preserving ML Models (Day 4-5)

**File: `private_ml.py`**

```python
from diffprivlib.models import LogisticRegression, GaussianNB
from sklearn.model_selection import train_test_split
import numpy as np

class PrivateML:
    """Privacy-preserving machine learning"""
    
    def __init__(self, epsilon=1.0):
        """
        epsilon: Privacy parameter
        Smaller epsilon = more privacy, less accuracy
        """
        self.epsilon = epsilon
        self.models = {}
        self.privacy_budget = epsilon
    
    def train_private_model(self, X, y, model_type='logistic'):
        """
        Train model with differential privacy
        """
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        # Use half of privacy budget for training
        training_epsilon = self.epsilon / 2
        
        if model_type == 'logistic':
            model = LogisticRegression(epsilon=training_epsilon)
        elif model_type == 'naive_bayes':
            model = GaussianNB(epsilon=training_epsilon)
        else:
            raise ValueError(f"Unknown model type: {model_type}")
        
        # Train model
        model.fit(X_train, y_train)
        
        # Evaluate
        accuracy = model.score(X_test, y_test)
        
        self.models[model_type] = {
            'model': model,
            'accuracy': accuracy,
            'epsilon_used': training_epsilon
        }
        
        return model, accuracy
    
    def evaluate_privacy_loss(self):
        """Calculate privacy budget used"""
        total_used = sum(m['epsilon_used'] for m in self.models.values())
        remaining = self.epsilon - total_used
        
        return {
            'total_budget': self.epsilon,
            'used': total_used,
            'remaining': remaining,
            'percentage_used': (total_used / self.epsilon) * 100
        }
    
    def compare_with_non_private(self, X, y, model_type='logistic'):
        """Compare private vs non-private model"""
        from sklearn.linear_model import LogisticRegression as LR
        
        # Train non-private model
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        non_private = LR()
        non_private.fit(X_train, y_train)
        non_private_acc = non_private.score(X_test, y_test)
        
        # Train private model
        private_model, private_acc = self.train_private_model(X, y, model_type)
        
        return {
            'non_private_accuracy': non_private_acc,
            'private_accuracy': private_acc,
            'accuracy_loss': non_private_acc - private_acc,
            'privacy_gain': self.epsilon
        }
```

---

### Step 5: Implement GDPR Compliance (Day 6)

**File: `compliance.py`**

```python
import pandas as pd
import re

class GDPRCompliance:
    """GDPR compliance checks and utilities"""
    
    # PII patterns
    EMAIL_PATTERN = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    PHONE_PATTERN = r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'
    SSN_PATTERN = r'\b\d{3}-\d{2}-\d{4}\b'
    
    def check_consent(self, data, consent_column='consent'):
        """Check if data has proper consent"""
        if consent_column in data.columns:
            has_consent = data[consent_column].all()
            return {
                'has_consent': has_consent,
                'consent_rate': data[consent_column].mean()
            }
        return {'has_consent': False, 'consent_rate': 0.0}
    
    def detect_pii(self, data):
        """Detect personally identifiable information"""
        pii_found = {}
        
        for col in data.columns:
            col_data = data[col].astype(str)
            
            # Check for emails
            emails = col_data.str.contains(self.EMAIL_PATTERN, regex=True).sum()
            if emails > 0:
                pii_found[col] = {'type': 'email', 'count': emails}
            
            # Check for phones
            phones = col_data.str.contains(self.PHONE_PATTERN, regex=True).sum()
            if phones > 0:
                pii_found[col] = {'type': 'phone', 'count': phones}
            
            # Check for SSN
            ssns = col_data.str.contains(self.SSN_PATTERN, regex=True).sum()
            if ssns > 0:
                pii_found[col] = {'type': 'ssn', 'count': ssns}
        
        return pii_found
    
    def anonymize_pii(self, data):
        """Remove or anonymize PII"""
        data_anon = data.copy()
        pii_columns = []
        
        # Detect PII
        pii_found = self.detect_pii(data)
        
        for col, info in pii_found.items():
            if info['type'] == 'email':
                # Replace with generic email
                data_anon[col] = 'user@example.com'
            elif info['type'] == 'phone':
                # Replace with generic phone
                data_anon[col] = '000-000-0000'
            elif info['type'] == 'ssn':
                # Replace with generic SSN
                data_anon[col] = '000-00-0000'
            
            pii_columns.append(col)
        
        return data_anon, pii_columns
    
    def generate_privacy_impact_assessment(self, data, model_info):
        """Generate privacy impact assessment report"""
        pii_found = self.detect_pii(data)
        consent_info = self.check_consent(data)
        
        report = []
        report.append("=" * 60)
        report.append("PRIVACY IMPACT ASSESSMENT (PIA)")
        report.append("=" * 60)
        report.append("")
        
        report.append("## Data Analysis")
        report.append(f"Total records: {len(data)}")
        report.append(f"PII columns found: {len(pii_found)}")
        if pii_found:
            for col, info in pii_found.items():
                report.append(f"  - {col}: {info['type']} ({info['count']} instances)")
        
        report.append("")
        report.append("## Consent")
        report.append(f"Has consent: {consent_info['has_consent']}")
        report.append(f"Consent rate: {consent_info['consent_rate']:.2%}")
        
        report.append("")
        report.append("## Privacy Measures")
        report.append(f"Privacy technique: Differential Privacy")
        report.append(f"Epsilon (privacy parameter): {model_info.get('epsilon', 'N/A')}")
        report.append(f"Privacy budget used: {model_info.get('epsilon_used', 'N/A')}")
        
        report.append("")
        report.append("## Compliance Status")
        if consent_info['has_consent'] and len(pii_found) == 0:
            report.append("✅ GDPR Compliant")
        else:
            report.append("⚠️  Requires attention:")
            if not consent_info['has_consent']:
                report.append("  - Missing consent")
            if pii_found:
                report.append("  - PII detected, needs anonymization")
        
        return "\n".join(report)
```

---

### Step 6: Evaluate Privacy-Utility Tradeoff (Day 7)

**File: `evaluator.py`**

```python
import matplotlib.pyplot as plt
import numpy as np

class PrivacyUtilityEvaluator:
    """Evaluate privacy-utility tradeoff"""
    
    def evaluate_epsilon_range(self, X, y, epsilon_range=[0.1, 0.5, 1.0, 2.0, 5.0]):
        """Evaluate model performance at different epsilon values"""
        from private_ml import PrivateML
        from sklearn.model_selection import train_test_split
        
        results = []
        
        for epsilon in epsilon_range:
            private_ml = PrivateML(epsilon=epsilon)
            model, accuracy = private_ml.train_private_model(X, y)
            
            results.append({
                'epsilon': epsilon,
                'accuracy': accuracy,
                'privacy': 1.0 / epsilon  # Higher epsilon = less privacy
            })
        
        return results
    
    def plot_privacy_utility_tradeoff(self, results):
        """Plot privacy vs utility tradeoff"""
        epsilons = [r['epsilon'] for r in results]
        accuracies = [r['accuracy'] for r in results]
        privacy_scores = [r['privacy'] for r in results]
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        
        # Accuracy vs Epsilon
        ax1.plot(epsilons, accuracies, marker='o')
        ax1.set_xlabel('Epsilon (Privacy Parameter)')
        ax1.set_ylabel('Model Accuracy')
        ax1.set_title('Privacy vs Accuracy Tradeoff')
        ax1.grid(True)
        ax1.invert_xaxis()  # Lower epsilon = more privacy
        
        # Privacy Score vs Accuracy
        ax2.scatter(privacy_scores, accuracies, s=100, alpha=0.6)
        ax2.set_xlabel('Privacy Score (1/epsilon)')
        ax2.set_ylabel('Model Accuracy')
        ax2.set_title('Privacy-Utility Tradeoff')
        ax2.grid(True)
        
        plt.tight_layout()
        return fig
```

---

### Step 7: Create Main Program (Day 8)

**File: `main.py`**

```python
from privacy_techniques import add_laplace_noise, k_anonymize
from private_ml import PrivateML
from compliance import GDPRCompliance
from evaluator import PrivacyUtilityEvaluator
import pandas as pd
import numpy as np

def main():
    # Load sample data (replace with your data)
    # For demonstration, create synthetic healthcare data
    np.random.seed(42)
    n_samples = 1000
    
    data = pd.DataFrame({
        'age': np.random.randint(18, 80, n_samples),
        'blood_pressure': np.random.randint(90, 160, n_samples),
        'cholesterol': np.random.randint(150, 300, n_samples),
        'disease': np.random.randint(0, 2, n_samples),
        'email': [f'patient{i}@hospital.com' for i in range(n_samples)],
        'consent': np.random.choice([True, False], n_samples, p=[0.9, 0.1])
    })
    
    print("=" * 60)
    print("Privacy-Preserving ML System")
    print("=" * 60)
    
    # Step 1: GDPR Compliance Check
    print("\n[Step 1] Checking GDPR Compliance...")
    compliance = GDPRCompliance()
    pii_found = compliance.detect_pii(data)
    consent_info = compliance.check_consent(data)
    
    print(f"PII columns found: {len(pii_found)}")
    print(f"Consent rate: {consent_info['consent_rate']:.2%}")
    
    # Step 2: Anonymize PII
    print("\n[Step 2] Anonymizing PII...")
    data_anon, pii_cols = compliance.anonymize_pii(data)
    print(f"Anonymized columns: {pii_cols}")
    
    # Step 3: Prepare data for ML
    X = data_anon[['age', 'blood_pressure', 'cholesterol']]
    y = data_anon['disease']
    
    # Step 4: Train Privacy-Preserving Model
    print("\n[Step 3] Training Privacy-Preserving Model...")
    private_ml = PrivateML(epsilon=1.0)
    model, accuracy = private_ml.train_private_model(X, y)
    print(f"Model accuracy: {accuracy:.4f}")
    
    # Step 5: Evaluate Privacy Loss
    privacy_info = private_ml.evaluate_privacy_loss()
    print(f"\nPrivacy Budget:")
    print(f"  Total: {privacy_info['total_budget']}")
    print(f"  Used: {privacy_info['used']:.4f}")
    print(f"  Remaining: {privacy_info['remaining']:.4f}")
    
    # Step 6: Compare with Non-Private
    print("\n[Step 4] Comparing with Non-Private Model...")
    comparison = private_ml.compare_with_non_private(X, y)
    print(f"Non-private accuracy: {comparison['non_private_accuracy']:.4f}")
    print(f"Private accuracy: {comparison['private_accuracy']:.4f}")
    print(f"Accuracy loss: {comparison['accuracy_loss']:.4f}")
    print(f"Privacy gain: epsilon = {comparison['privacy_gain']}")
    
    # Step 7: Generate PIA Report
    print("\n[Step 5] Generating Privacy Impact Assessment...")
    model_info = {'epsilon': 1.0, 'epsilon_used': 0.5}
    pia_report = compliance.generate_privacy_impact_assessment(data, model_info)
    print(pia_report)
    
    print("\n" + "=" * 60)
    print("Privacy-Preserving ML System Complete!")
    print("=" * 60)

if __name__ == "__main__":
    main()
```

---

## 🔗 Course Content Connections

### How This Project Connects to Course Content

| Project Step | Course Notebook | What You Learn |
|-------------|----------------|----------------|
| **Privacy Ethics** | `unit1-ethics-foundations/examples/02_privacy_ethics.ipynb` | Understanding privacy |
| **Differential Privacy** | `unit2-privacy-techniques/examples/01_differential_privacy.ipynb` | Differential privacy |
| **K-Anonymity** | `unit2-privacy-techniques/examples/02_k_anonymity.ipynb` | Data anonymization |
| **GDPR Compliance** | `unit3-privacy-compliance/examples/01_gdpr_compliance.ipynb` | Legal compliance |

---

## 🐛 Troubleshooting

### Problem: Model accuracy too low
**Error:** Private model performs poorly  
**Solution:** Increase epsilon (less privacy, more accuracy) or use more data

### Problem: Privacy budget exhausted
**Error:** No privacy budget remaining  
**Solution:** Use smaller epsilon values, or allocate budget more carefully

### Problem: PII detection fails
**Error:** PII not detected  
**Solution:** Check regex patterns, verify data format

### Problem: GDPR compliance issues
**Error:** Missing consent or PII present  
**Solution:** Anonymize data, ensure consent is obtained

---

## 🎓 Learning Checklist

- [ ] Day 1: Understand privacy in ML
- [ ] Day 2-3: Implement differential privacy
- [ ] Day 4-5: Create privacy-preserving models
- [ ] Day 6: Implement GDPR compliance
- [ ] Day 7: Evaluate privacy-utility tradeoff
- [ ] Day 8: Test complete system
- [ ] Day 9: Test with different datasets
- [ ] Day 10: Write documentation

---

## 💡 Tips for Success

1. **Start with High Epsilon:** Begin with epsilon=5.0, then reduce
2. **Balance Privacy and Utility:** Find sweet spot for your use case
3. **Test Compliance:** Always check GDPR compliance
4. **Document Everything:** Keep track of privacy budget usage
5. **Compare Models:** Always compare private vs non-private

---

**Good luck building your privacy-preserving ML system!** 🚀