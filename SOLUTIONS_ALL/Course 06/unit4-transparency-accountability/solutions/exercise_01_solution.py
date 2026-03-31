"""
Unit 4: Interpretability, Transparency, and Accountability
Exercise 1 Solution: SHAP and LIME Explanations

Complete solution for the SHAP/LIME exercise.
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge

def generate_dataset(n_samples=1000):
    np.random.seed(42)
    age = np.random.randint(25, 70, n_samples)
    income = np.random.normal(60000, 25000, n_samples)
    credit_score = np.random.normal(650, 100, n_samples)
    approval = (credit_score / 850 * 0.5 + income / 100000 * 0.3 + np.random.normal(0, 0.05, n_samples) > 0.5).astype(int)
    return pd.DataFrame({'age': age, 'income': income, 'credit_score': credit_score, 'approved': approval})

def calculate_shap_values(model, X_sample, X_train, feature_names):
    baseline = model.predict_proba(X_train)[:, 1].mean()
    sample_pred = model.predict_proba(X_sample)[0, 1]
    shap_values = []
    for i in range(len(feature_names)):
        X_perm = X_train.copy()
        X_perm[:, i] = X_sample[0, i]
        perm_pred = model.predict_proba(X_perm)[:, 1].mean()
        shap_values.append(sample_pred - perm_pred)
    return np.array(shap_values)

def calculate_lime_explanation(model, X_sample, X_train, feature_names):
    perturbations = np.random.normal(0, 0.1, (1000, X_sample.shape[1]))
    X_pert = X_sample + perturbations
    y_pert = model.predict_proba(X_pert)[:, 1]
    distances = np.exp(-np.sum((X_pert - X_sample) ** 2, axis=1))
    linear_model = Ridge(alpha=0.1)
    linear_model.fit(X_pert, y_pert, sample_weight=distances)
    return linear_model.coef_

if __name__ == "__main__":
    print("="*80)
    print("Unit 4 - Exercise 1 Solution: SHAP and LIME Explanations")
    print("="*80)
    
    df = generate_dataset()
    X = df[['age', 'income', 'credit_score']].values
    y = df['approved'].values
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train_scaled, y_train)
    
    sample = X_test_scaled[0:1]
    feature_names = ['age', 'income', 'credit_score']
    
    shap_vals = calculate_shap_values(model, sample, X_train_scaled, feature_names)
    lime_vals = calculate_lime_explanation(model, sample, X_train_scaled, feature_names)
    
    print("\nSHAP Values:")
    for name, val in zip(feature_names, shap_vals):
        print(f"  {name}: {val:.4f}")
    
    print("\nLIME Values:")
    for name, val in zip(feature_names, lime_vals):
        print(f"  {name}: {val:.4f}")
    
    print("\n✅ Solution completed!")

