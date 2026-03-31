"""
Unit 3: Privacy, Security, and Data Protection
Exercise 1 Solution: Privacy Techniques

Complete solution for the privacy techniques exercise.
"""

import numpy as np
import pandas as pd
import hashlib

def anonymize_data(df, columns_to_anonymize):
    """Implement data anonymization"""
    df_anonymized = df.copy()
    for col in columns_to_anonymize:
        if col in df_anonymized.columns:
            df_anonymized[col] = [f'ID_{i}' for i in range(len(df_anonymized))]
    return df_anonymized

def pseudonymize_data(df, columns_to_pseudonymize, salt='default_salt'):
    """Implement data pseudonymization using hashing"""
    df_pseudonymized = df.copy()
    for col in columns_to_pseudonymize:
        if col in df_pseudonymized.columns:
            df_pseudonymized[col] = df_pseudonymized[col].apply(
                lambda x: hashlib.sha256((str(x) + salt).encode()).hexdigest()[:16]
            )
    return df_pseudonymized

def add_differential_privacy_noise(value, epsilon=1.0, sensitivity=1.0):
    """Add Laplace noise for differential privacy"""
    scale = sensitivity / epsilon
    noise = np.random.laplace(0, scale)
    return value + noise

if __name__ == "__main__":
    print("="*80)
    print("Unit 3 - Exercise 1 Solution: Privacy Techniques")
    print("="*80)
    
    # Test with sample data
    np.random.seed(42)
    df = pd.DataFrame({
        'name': [f'Person_{i}' for i in range(10)],
        'email': [f'user{i}@example.com' for i in range(10)],
        'value': np.random.normal(100, 20, 10)
    })
    
    print("\nOriginal Data:")
    print(df.head())
    
    print("\nAnonymized Data:")
    df_anon = anonymize_data(df, ['name', 'email'])
    print(df_anon.head())
    
    print("\nPseudonymized Data:")
    df_pseudo = pseudonymize_data(df, ['name', 'email'])
    print(df_pseudo.head())
    
    print("\nDifferential Privacy:")
    true_mean = df['value'].mean()
    noisy_mean = add_differential_privacy_noise(true_mean, epsilon=1.0)
    print(f"True mean: {true_mean:.2f}")
    print(f"Noisy mean: {noisy_mean:.2f}")
    
    print("\n✅ Solution completed!")
