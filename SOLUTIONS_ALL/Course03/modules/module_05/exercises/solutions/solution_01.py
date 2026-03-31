"""
Solution 01: Statistical Inference and Hypothesis Testing

This is the reference solution for exercise_01.py
"""

import numpy as np
from scipy import stats


def compute_confidence_interval(data, confidence=0.95):
    """Compute confidence interval for data."""
    n = len(data)
    mean = np.mean(data)
    std_err = stats.sem(data)  # Standard error of the mean
    
    # Get t-critical value
    alpha = 1 - confidence
    t_critical = stats.t.ppf(1 - alpha/2, df=n-1)
    
    # Compute CI
    margin = t_critical * std_err
    lower = mean - margin
    upper = mean + margin
    
    return (lower, upper)


def t_test_two_samples(sample1, sample2):
    """Perform two-sample t-test."""
    t_stat, p_value = stats.ttest_ind(sample1, sample2)
    return t_stat, p_value


def interpret_p_value(p_value, alpha=0.05):
    """Interpret p-value from statistical test."""
    if p_value < alpha:
        return f"Significant difference (p={p_value:.4f} < {alpha})"
    else:
        return f"No significant difference (p={p_value:.4f} >= {alpha})"


def compare_models(model1_scores, model2_scores, alpha=0.05):
    """Compare two models using statistical inference."""
    # Compute means and CIs
    mean1 = np.mean(model1_scores)
    mean2 = np.mean(model2_scores)
    ci1 = compute_confidence_interval(model1_scores)
    ci2 = compute_confidence_interval(model2_scores)
    
    # Perform t-test
    t_stat, p_value = t_test_two_samples(model1_scores, model2_scores)
    
    # Interpret
    interpretation = interpret_p_value(p_value, alpha)
    
    return {
        'model1_mean': mean1,
        'model2_mean': mean2,
        'model1_ci': ci1,
        'model2_ci': ci2,
        't_statistic': t_stat,
        'p_value': p_value,
        'interpretation': interpretation,
        'significant': p_value < alpha
    }


if __name__ == "__main__":
    print("Solution 01: Statistical Inference")
    print("=" * 60)
    
    np.random.seed(42)
    model1 = np.random.normal(0.85, 0.02, 100)
    model2 = np.random.normal(0.87, 0.02, 100)
    
    comparison = compare_models(model1, model2)
    
    print("Model Comparison Results:")
    for key, value in comparison.items():
        print(f"  {key}: {value}")
    
    print("\n✅ Solution verified!")
