# Module 04 Quiz: Dimensionality Reduction

**Instructions**: Answer the following questions. Check your answers with the solutions provided.

## Part 1: Conceptual Questions

### Question 1
**What is the curse of dimensionality?**
- [ ] A) High dimensions require exponentially more data
- [ ] B) Dimensions are hard to understand
- [ ] C) Dimensions are expensive
- [ ] D) Dimensions are optional

**Answer**: A

**Explanation**: As dimensions increase, the amount of data needed grows exponentially.

---

### Question 2
**What does PCA (Principal Component Analysis) do?**
- [ ] A) Adds dimensions
- [ ] B) Reduces dimensions while preserving variance
- [ ] C) Deletes data
- [ ] D) Copies data

**Answer**: B

**Explanation**: PCA reduces dimensions by finding directions of maximum variance.

---

### Question 3
**What mathematical concept from Module 01 does PCA use?**
- [ ] A) Matrix addition
- [ ] B) Eigenvalues and eigenvectors
- [ ] C) Matrix subtraction
- [ ] D) Random operations

**Answer**: B

**Explanation**: PCA uses eigenvalue decomposition to find principal components.

---

### Question 4
**What does "variance explained" mean in PCA?**
- [ ] A) How much data is deleted
- [ ] B) How much information is preserved
- [ ] C) How much data is added
- [ ] D) Random concept

**Answer**: B

**Explanation**: Variance explained tells us how much information is preserved after reduction.

---

### Question 5
**Why do we need dimensionality reduction?**
- [ ] A) It's required
- [ ] B) Improves efficiency, visualization, and can reduce noise
- [ ] C) It makes code faster
- [ ] D) It's optional

**Answer**: B

**Explanation**: Dimensionality reduction improves computational efficiency, enables visualization, and can reduce noise.

---

## Part 2: Code Understanding

### Question 6
**What does this code do?**
```python
pca = PCA(n_components=2)
data_reduced = pca.fit_transform(data)
```

- [ ] A) Adds 2 dimensions
- [ ] B) Reduces data to 2 dimensions using PCA
- [ ] C) Deletes 2 dimensions
- [ ] D) Copies data

**Answer**: B

**Explanation**: This reduces the data to 2 principal components using PCA.

---

### Question 7
**What are principal components?**
- [ ] A) Random directions
- [ ] B) Directions of maximum variance (eigenvectors)
- [ ] C) Directions of minimum variance
- [ ] D) Original features

**Answer**: B

**Explanation**: Principal components are eigenvectors pointing in directions of maximum variance.

---

## Part 3: Application Questions

### Question 8
**Which modules does PCA combine concepts from?**
- [ ] A) Module 01 only
- [ ] B) Module 01 (eigenvalues) + Module 03 (optimization)
- [ ] C) Module 02 only
- [ ] D) Module 05 only

**Answer**: B

**Explanation**: PCA combines eigenvalues (Module 01) with optimization (Module 03).

---

### Question 9
**If PCA reduces 100 features to 5 components and explains 90% variance, is this good?**
- [ ] A) No, too much information lost
- [ ] B) Yes, preserved 90% with 95% fewer dimensions
- [ ] C) Maybe
- [ ] D) Can't tell

**Answer**: B

**Explanation**: Preserving 90% variance while reducing from 100 to 5 dimensions (95% reduction) is excellent.

---

### Question 10
**What is the main goal of dimensionality reduction?**
- [ ] A) Delete data
- [ ] B) Reduce dimensions while preserving important information
- [ ] C) Add dimensions
- [ ] D) Make data larger

**Answer**: B

**Explanation**: The goal is to reduce dimensions while keeping the most important information.

---

## Scoring

- **9-10 correct**: Excellent! You understand dimensionality reduction.
- **7-8 correct**: Good! Review the concepts you missed.
- **5-6 correct**: Review the module and try again.
- **Below 5**: Study the module more carefully before proceeding.

---

## Next Steps

After completing this quiz:
1. Review any questions you got wrong
2. Complete the exercises in `exercises/`
3. Move to Module 05 when ready

