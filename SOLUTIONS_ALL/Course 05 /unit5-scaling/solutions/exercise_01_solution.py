"""
Unit 5 - Exercise 1: Solution
"""

import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt

# Generate large dataset
np.random.seed(42)
print("Generating large dataset...")
large_data = pd.DataFrame({
    'id': range(1, 100001),
    'value1': np.random.randn(100000),
    'value2': np.random.randn(100000),
    'category': np.random.choice(['A', 'B', 'C', 'D'], 100000),
    'score': np.random.uniform(0, 100, 100000)
})

# Task 1: Efficient Processing
print("=" * 60)
print("Task 1: Efficient Processing")
print("=" * 60)

# Process in chunks
chunk_size = 10000
start_time = time.time()

results = []
for chunk in np.array_split(large_data, len(large_data) // chunk_size):
    chunk_result = chunk['score'].mean()
    results.append(chunk_result)

overall_mean = np.mean(results)
processing_time = time.time() - start_time

print(f"Processed in chunks: {processing_time:.4f} seconds")
print(f"Overall mean score: {overall_mean:.4f}")

# Task 2: Aggregation
print("\n" + "=" * 60)
print("Task 2: Aggregation")
print("=" * 60)

start_time = time.time()
category_stats = large_data.groupby('category').agg({
    'score': ['mean', 'std', 'min', 'max'],
    'value1': 'mean'
})
agg_time = time.time() - start_time

print(f"Aggregation time: {agg_time:.4f} seconds")
print("\nCategory Statistics:")
print(category_stats)

# Task 3: Memory Optimization
print("\n" + "=" * 60)
print("Task 3: Memory Optimization")
print("=" * 60)

print(f"Original memory usage: {large_data.memory_usage(deep=True).sum() / 1024**2:.2f} MB")

# Optimize data types
large_data['id'] = large_data['id'].astype('int32')
large_data['category'] = large_data['category'].astype('category')
large_data['score'] = large_data['score'].astype('float32')

optimized_memory = large_data.memory_usage(deep=True).sum() / 1024**2
print(f"Optimized memory usage: {optimized_memory:.2f} MB")
print(f"Memory saved: {(large_data.memory_usage(deep=True).sum() / 1024**2) - optimized_memory:.2f} MB")

# Task 4: Performance Profiling
print("\n" + "=" * 60)
print("Task 4: Performance Profiling")
print("=" * 60)

operations = {
    'Mean': lambda: large_data['score'].mean(),
    'GroupBy': lambda: large_data.groupby('category')['score'].mean(),
    'Filter': lambda: large_data[large_data['score'] > 50],
    'Sort': lambda: large_data.sort_values('score')
}

results = {}
for op_name, op_func in operations.items():
    start = time.time()
    result = op_func()
    elapsed = time.time() - start
    results[op_name] = elapsed
    print(f"{op_name}: {elapsed:.4f} seconds")

# Visualize
plt.figure(figsize=(10, 6))
plt.bar(results.keys(), results.values(), color='steelblue')
plt.title('Operation Performance')
plt.ylabel('Time (seconds)')
plt.xlabel('Operation')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('unit5-scaling/examples/performance.png', dpi=150)
plt.close()

print("\n" + "=" * 60)
print("Solution Complete!")
print("=" * 60)

