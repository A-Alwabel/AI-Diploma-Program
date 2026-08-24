# Quiz 5: Extending the Scope of Data Science (Scaling and Production)

**Time Limit:** 30 minutes | **Marks:** 30 points

---

## Part 1: Multiple Choice (10 points)

### Question 1 (2 points)
What is Dask used for?
- A) Data visualization
- B) Model training only
- C) Data cleaning
- D) Distributed computing and parallel processing

---

### Question 2 (2 points)
What is NVIDIA RAPIDS?
- A) A CPU-only library
- B) A visualization tool
- C) A GPU-accelerated data science library
- D) A database system

---

### Question 3 (2 points)
What is the main advantage of GPU computing over CPU for data science?
- A) Parallel processing of many operations simultaneously
- B) Lower cost
- C) Easier to use
- D) Better for small datasets

---

### Question 4 (2 points)
What is a production pipeline?
- A) A model training script
- B) An automated system that processes data and makes predictions
- C) A data visualization
- D) A testing framework

---

### Question 5 (2 points)
What is model deployment?
- A) Training a model
- B) Evaluating a model
- C) Making a model available for use in production
- D) Visualizing model results

---

## Part 2: Code Writing (10 points)

### Question 6 (5 points)
Write code to create a Dask DataFrame and perform operations:
1. Import dask
2. Create a Dask DataFrame from a CSV
3. Perform a computation (e.g., groupby)

```python
import dask.dataframe as dd

# Create Dask DataFrame
df = dd.read_csv('large_data.csv')

# Perform computation
result = df.groupby('category').sum().compute()
print(result)
```

---

### Question 7 (5 points)
Write code to save and load a trained model:
1. Import joblib or pickle
2. Save a trained model
3. Load the model back

```python
import joblib
from sklearn.linear_model import LogisticRegression

# Assuming model is trained
model = LogisticRegression()
# ... train model ...

# Save model
joblib.dump(model, 'model.pkl')

# Load model
loaded_model = joblib.load('model.pkl')
predictions = loaded_model.predict(X_new)
```

---

## Part 3: Short Answer (10 points)

### Question 8 (5 points)
Explain the key considerations for deploying ML models in production.

**Key Considerations:**
1. **Model Versioning**: Track different model versions
2. **Monitoring**: Monitor model performance and data drift
3. **Scalability**: Handle varying loads (horizontal scaling)
4. **Latency**: Ensure fast prediction times
5. **Reliability**: Error handling and fallback mechanisms
6. **Security**: Protect models and data
7. **Reproducibility**: Ensure consistent results
8. **Documentation**: Clear API documentation
9. **Testing**: Comprehensive testing before deployment
10. **CI/CD**: Automated deployment pipelines

---

### Question 9 (5 points)
What are the main challenges when scaling data science workflows? How can they be addressed?

**Main Challenges:**
1. **Memory Limitations**: Large datasets don't fit in memory
   - Solution: Use chunking, Dask, or distributed systems
   
2. **Computation Time**: Processing takes too long
   - Solution: Parallel processing, GPU acceleration, distributed computing
   
3. **Data Distribution**: Data stored across multiple locations
   - Solution: Distributed file systems (HDFS, S3), data partitioning
   
4. **Model Complexity**: Complex models are slow to train/predict
   - Solution: Model optimization, quantization, hardware acceleration
   
5. **Real-time Requirements**: Need fast predictions
   - Solution: Model optimization, caching, dedicated inference servers

**Tools:**
- Dask for distributed computing
- RAPIDS for GPU acceleration
- Spark for big data processing
- Kubernetes for container orchestration

---

## Grading Rubric

- **90-100% (27-30 points):** Excellent understanding
- **80-89% (24-26 points):** Good understanding
- **70-79% (21-23 points):** Satisfactory
- **60-69% (18-20 points):** Needs improvement
- **Below 60% (<18 points):** Requires additional study
