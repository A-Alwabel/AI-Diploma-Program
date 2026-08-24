# Quiz 04: Dimensionality Reduction

**Time Limit:** 45 minutes | **Marks:** 100 points

---

## Part 1: PCA Basics (30 points)

### Question 1 (5 points)
What does PCA stand for?
- A) Primary Component Algorithm
- B) Principal Component Analysis
- C) Principal Calculation Algorithm
- D) Primary Calculation Analysis

---

### Question 2 (5 points)
What is the main goal of PCA?
- A) Increase dimensionality
- B) Remove noise
- C) Reduce dimensionality while preserving maximum variance
- D) Add features

---

### Question 3 (5 points)
What are principal components?
- A) Original features
- B) The mean of the data
- C) Random directions
- D) New orthogonal directions that capture maximum variance

---

### Question 4 (15 points)
Explain how PCA works step by step.

**PCA Steps:**

1. **Standardize the Data:**
   - Mean-center the data: subtract mean from each feature
   - Scale to unit variance (optional but recommended)
   - Ensures all features are on same scale

2. **Compute Covariance Matrix:**
   - Calculate covariance matrix of standardized data
   - Shows relationships between features
   - Size: d×d where d is number of features

3. **Eigenvalue Decomposition:**
   - Find eigenvalues and eigenvectors of covariance matrix
   - Eigenvectors are principal components (directions of maximum variance)
   - Eigenvalues indicate variance explained by each component

4. **Select Principal Components:**
   - Sort eigenvectors by eigenvalues (descending)
   - Choose top k components that explain desired variance (e.g., 95%)
   - k < original dimensionality

5. **Transform Data:**
   - Project data onto selected principal components
   - New data: X_new = X_standardized × W
   - W is matrix of selected eigenvectors

**Result:** Reduced dimensionality data preserving maximum variance.

---

## Part 2: Curse of Dimensionality (25 points)

### Question 5 (5 points)
What is the curse of dimensionality?
- A) Problems that arise when working with high-dimensional data
- B) High-dimensional data is easier to work with
- C) Data with many samples
- D) Low-dimensional data

---

### Question 6 (5 points)
What happens to distances in high-dimensional spaces?
- A) All points become approximately equidistant
- B) They become more meaningful
- C) They become smaller
- D) Nothing changes

---

### Question 7 (15 points)
Explain the main problems caused by the curse of dimensionality and how dimensionality reduction helps.

**Problems:**

1. **Distance Concentration:**
   - In high dimensions, all distances become similar
   - Nearest and farthest neighbors have similar distances
   - Makes distance-based methods (k-NN, clustering) less effective
   - **Solution:** Reduce dimensions to make distances meaningful

2. **Sparse Data:**
   - Data becomes sparse in high-dimensional space
   - Need exponentially more samples to cover space
   - Most regions are empty
   - **Solution:** Reduce to lower-dimensional manifold

3. **Overfitting:**
   - More features than samples leads to overfitting
   - Model memorizes training data
   - Poor generalization
   - **Solution:** Feature selection/reduction reduces overfitting

4. **Computational Complexity:**
   - Algorithms scale poorly with dimensions
   - Storage and computation costs increase
   - **Solution:** Fewer dimensions = faster computation

5. **Noise Accumulation:**
   - Each dimension adds noise
   - Signal-to-noise ratio decreases
   - **Solution:** Keep only informative dimensions

**How Dimensionality Reduction Helps:**
- Reduces to essential information
- Removes noise and redundancy
- Makes distances meaningful
- Prevents overfitting
- Improves computational efficiency
- Often improves model performance

---

## Part 3: Feature Selection (25 points)

### Question 8 (5 points)
What is feature selection?
- A) Creating new features
- B) Scaling features
- C) Removing all features
- D) Choosing a subset of relevant features

---

### Question 9 (5 points)
What is the difference between feature selection and feature extraction?
- A) They are the same
- B) Selection keeps original features, extraction creates new features
- C) Selection creates new features, extraction keeps original
- D) Selection removes features, extraction adds features

---

### Question 10 (15 points)
Describe three feature selection methods and when to use each.

**1. Filter Methods:**
- **How:** Select features based on statistical measures
- **Examples:**
  - Correlation with target
  - Mutual information
  - Chi-square test
  - Variance threshold
- **Pros:** Fast, independent of model
- **Cons:** May miss feature interactions
- **Use:** Quick initial selection, large datasets

**2. Wrapper Methods:**
- **How:** Use model performance to select features
- **Examples:**
  - Forward selection
  - Backward elimination
  - Recursive feature elimination (RFE)
- **Pros:** Considers feature interactions, model-specific
- **Cons:** Computationally expensive, can overfit
- **Use:** When model performance is critical, smaller datasets

**3. Embedded Methods:**
- **How:** Feature selection built into model training
- **Examples:**
  - Lasso regression (L1 regularization)
  - Decision trees (feature importance)
  - Random forests (feature importance)
- **Pros:** Efficient, model-specific, considers interactions
- **Cons:** Tied to specific model type
- **Use:** When using models with built-in selection, balanced approach

**Comparison:**
- **Filter:** Fastest, model-agnostic, good for initial screening
- **Wrapper:** Most accurate for specific model, but slow
- **Embedded:** Good balance, efficient, model-specific

---

## Part 4: Applications (20 points)

### Question 11 (10 points)
Give three real-world applications of dimensionality reduction and explain why it's useful in each case.

**1. Image Compression:**
- **Application:** Compress images for storage/transmission
- **Why:** Images have high dimensionality (e.g., 1000×1000 = 1M pixels)
- **Method:** PCA to reduce to fewer components
- **Benefit:** Smaller file size, faster transmission, preserves main features
- **Example:** JPEG uses similar principle (DCT)

**2. Face Recognition:**
- **Application:** Identify faces from images
- **Why:** Face images have many pixels but lie on lower-dimensional manifold
- **Method:** PCA (Eigenfaces) or more advanced methods
- **Benefit:** Reduces computation, removes noise, focuses on important features
- **Example:** Eigenfaces method projects faces onto principal components

**3. Gene Expression Analysis:**
- **Application:** Analyze gene expression data
- **Why:** Thousands of genes (features), few samples
- **Method:** PCA to reduce to key gene expression patterns
- **Benefit:** Identifies key patterns, removes noise, visualizes data
- **Example:** Identify cancer subtypes from gene expression

**4. Recommendation Systems:**
- **Application:** Recommend products/movies
- **Why:** Many users and items create high-dimensional space
- **Method:** Matrix factorization, dimensionality reduction
- **Benefit:** Finds latent factors, reduces sparsity, improves recommendations
- **Example:** Netflix recommendations

**5. Natural Language Processing:**
- **Application:** Text analysis, topic modeling
- **Why:** High-dimensional word/document spaces
- **Method:** Latent Semantic Analysis (LSA), topic models
- **Benefit:** Finds topics, reduces noise, improves similarity
- **Example:** Document clustering, search engines

---

### Question 12 (10 points)
What are the limitations of PCA? When might you choose an alternative method?

**Limitations of PCA:**

1. **Linear Assumption:**
   - Assumes linear relationships
   - Cannot capture non-linear patterns
   - **Alternative:** Kernel PCA, t-SNE, UMAP

2. **Variance Focus:**
   - Maximizes variance, not necessarily class separation
   - May not preserve important class information
   - **Alternative:** Linear Discriminant Analysis (LDA)

3. **Interpretability:**
   - Principal components are linear combinations
   - Hard to interpret original features
   - **Alternative:** Feature selection methods

4. **Scale Sensitivity:**
   - Results depend on feature scaling
   - Must standardize before PCA
   - **Alternative:** Methods that handle different scales

5. **Outlier Sensitivity:**
   - Sensitive to outliers
   - Outliers can dominate principal components
   - **Alternative:** Robust PCA, outlier removal

**When to Use Alternatives:**

- **Non-linear Data:** Use Kernel PCA, t-SNE, UMAP
- **Supervised Learning:** Use LDA (preserves class separation)
- **Interpretability Needed:** Use feature selection
- **Outliers Present:** Use robust methods
- **Sparse Data:** Use methods designed for sparsity
- **Very High Dimensions:** Use random projections, feature hashing

**Example:**
- **PCA:** Good for linear data, visualization, noise reduction
- **t-SNE:** Good for non-linear visualization, clustering
- **LDA:** Good for classification with class labels
- **Feature Selection:** Good when interpretability is critical

---

## Grading Rubric

- **90-100 points:** Excellent understanding
- **80-89 points:** Good understanding
- **70-79 points:** Satisfactory
- **60-69 points:** Needs improvement
- **Below 60:** Review required

---

**Created:** 2025  
**For:** 113 AIAT - Mathematics and Probabilities for Machine Learning
