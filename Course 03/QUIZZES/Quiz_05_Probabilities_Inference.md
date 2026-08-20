# Quiz 05: Probabilities and Statistical Inference

**Time Limit:** 45 minutes | **Marks:** 100 points

---

## Part 1: Probability Distributions (30 points)

### Question 1 (5 points)
What is a probability distribution?
- A) A single number
- B) A function that describes the probability of different outcomes
- C) The mean of data
- D) A matrix

---

### Question 2 (5 points)
What is the difference between discrete and continuous distributions?
- A) They are the same
- B) Discrete has countable outcomes, continuous has uncountable outcomes
- C) Discrete is always normal
- D) Continuous is always uniform

---

### Question 3 (5 points)
What is the normal distribution?
- A) A uniform distribution
- B) A bell-shaped distribution with mean μ and variance σ²
- C) An exponential distribution
- D) A discrete distribution

---

### Question 4 (15 points)
Explain three common probability distributions used in machine learning and when each is used.

**1. Normal (Gaussian) Distribution:**
- **Shape:** Bell-shaped, symmetric
- **Parameters:** Mean (μ), variance (σ²)
- **Properties:** Central limit theorem, many natural phenomena
- **ML Use:**
  - Assumption in linear regression (errors normally distributed)
  - Prior distributions in Bayesian methods
  - Noise modeling
  - Initialization in neural networks

**2. Bernoulli Distribution:**
- **Shape:** Discrete, two outcomes (0 or 1)
- **Parameters:** Probability p of success
- **Properties:** Models binary events
- **ML Use:**
  - Binary classification (logistic regression)
  - Loss functions (binary cross-entropy)
  - Activation functions (sigmoid outputs probabilities)

**3. Multinomial Distribution:**
- **Shape:** Discrete, multiple outcomes
- **Parameters:** Probabilities for each category
- **Properties:** Generalization of Bernoulli
- **ML Use:**
  - Multi-class classification
  - Softmax outputs (probabilities for each class)
  - Categorical data modeling

**4. Uniform Distribution:**
- **Shape:** Constant probability over range
- **Parameters:** Lower and upper bounds
- **ML Use:**
  - Random initialization
  - Prior when no information available
  - Sampling

**5. Exponential Distribution:**
- **Shape:** Right-skewed, models waiting times
- **Parameters:** Rate parameter λ
- **ML Use:**
  - Survival analysis
  - Time-to-event modeling
  - Some regularization techniques

---

## Part 2: Statistical Inference (25 points)

### Question 5 (5 points)
What is statistical inference?
- A) Describing data
- B) Drawing conclusions about populations from samples
- C) Calculating means
- D) Plotting data

---

### Question 6 (5 points)
What is a confidence interval?
- A) A single number
- B) A range of values that likely contains the true parameter
- C) The mean
- D) The variance

---

### Question 7 (15 points)
Explain hypothesis testing and how it's used in machine learning.

**Hypothesis Testing:**

**Concept:**
- Test whether observed data supports a hypothesis
- Null hypothesis (H₀): Default assumption (e.g., no effect)
- Alternative hypothesis (H₁): What we want to prove
- Use sample data to decide whether to reject H₀

**Process:**
1. **State Hypotheses:** H₀ and H₁
2. **Choose Significance Level:** α (e.g., 0.05)
3. **Calculate Test Statistic:** From sample data
4. **Find P-value:** Probability of observing data if H₀ is true
5. **Make Decision:**
   - If p-value < α: Reject H₀ (evidence for H₁)
   - If p-value ≥ α: Fail to reject H₀ (insufficient evidence)

**ML Applications:**

1. **Feature Selection:**
   - Test if feature is significantly related to target
   - t-test, chi-square test
   - Example: Is age significantly related to income?

2. **Model Comparison:**
   - Test if one model is significantly better
   - Paired t-test on cross-validation scores
   - Example: Is model A significantly better than model B?

3. **A/B Testing:**
   - Test if new model version improves performance
   - Compare metrics between versions
   - Example: Does new recommendation algorithm increase clicks?

4. **Assumption Checking:**
   - Test if data meets model assumptions
   - Normality tests, independence tests
   - Example: Are residuals normally distributed?

5. **Effect Size:**
   - Determine if effect is practically significant
   - Not just statistical significance
   - Example: Small but significant improvement may not be useful

**Example:**
- **H₀:** New feature doesn't improve model (AUC difference = 0)
- **H₁:** New feature improves model (AUC difference > 0)
- **Test:** Compare models with/without feature
- **Result:** If p < 0.05, feature is significant

---

## Part 3: Bayesian Inference (25 points)

### Question 8 (5 points)
What is Bayesian inference?
- A) Only using prior knowledge
- B) Updating beliefs using both prior knowledge and observed data
- C) Only using observed data
- D) Ignoring uncertainty

---

### Question 9 (5 points)
What is Bayes' theorem?
- A) P(A|B) = P(B|A) × P(A) / P(B)
- B) P(A) = P(B)
- C) P(A|B) = P(A)
- D) P(A and B) = P(A) + P(B)

---

### Question 10 (15 points)
Explain Bayesian inference and how it differs from frequentist inference. Give an ML example.

**Bayesian vs Frequentist:**

**Frequentist Inference:**
- Parameters are fixed (unknown constants)
- Use maximum likelihood estimation (MLE)
- Confidence intervals: "If we repeated experiment many times, 95% of intervals would contain true parameter"
- No prior knowledge incorporated
- Example: Maximum likelihood in linear regression

**Bayesian Inference:**
- Parameters are random variables with distributions
- Use Bayes' theorem to update beliefs
- Credible intervals: "95% probability parameter is in this range"
- Incorporates prior knowledge
- Example: Bayesian linear regression with prior on weights

**Bayes' Theorem:**
P(θ|data) = P(data|θ) × P(θ) / P(data)

- **Posterior:** P(θ|data) - Updated belief after seeing data
- **Likelihood:** P(data|θ) - How likely data is given parameter
- **Prior:** P(θ) - Belief before seeing data
- **Evidence:** P(data) - Normalizing constant

**ML Example: Bayesian Linear Regression:**

**Frequentist Approach:**
- Find weights w that maximize likelihood: w = argmax P(data|w)
- No prior on weights
- Point estimate: w = (X^T X)^(-1) X^T y

**Bayesian Approach:**
- Start with prior on weights: P(w) ~ N(0, αI) (regularization)
- Update with data: P(w|data) ∝ P(data|w) × P(w)
- Get posterior distribution over weights
- Predictions include uncertainty: P(y_new|x_new, data)

**Advantages of Bayesian:**
- Quantifies uncertainty
- Incorporates prior knowledge
- Regularization naturally (prior acts as regularizer)
- Handles small datasets better

**Challenges:**
- Computationally expensive
- Prior selection can be subjective
- Complex posterior distributions

---

## Part 4: Applications (20 points)

### Question 11 (10 points)
How is probability theory used in machine learning? Give at least 3 examples.

**Applications:**

1. **Probabilistic Models:**
   - Models that output probabilities, not just predictions
   - Example: Logistic regression outputs P(y=1|x)
   - Use: Uncertainty quantification, decision making

2. **Loss Functions:**
   - Many based on probability theory
   - Example: Cross-entropy = -Σ log P(y_true|prediction)
   - Use: Classification, measures probability of correct prediction

3. **Bayesian Methods:**
   - Bayesian neural networks, Gaussian processes
   - Example: Bayesian optimization for hyperparameter tuning
   - Use: Uncertainty estimation, incorporating prior knowledge

4. **Generative Models:**
   - Models that learn data distribution P(x)
   - Example: GANs, VAEs, Naive Bayes
   - Use: Data generation, anomaly detection

5. **Probabilistic Graphical Models:**
   - Represent dependencies using probability
   - Example: Hidden Markov Models, Bayesian networks
   - Use: Sequence modeling, causal inference

6. **Ensemble Methods:**
   - Combine predictions probabilistically
   - Example: Random forests (voting), Bayesian model averaging
   - Use: Improved accuracy, uncertainty estimation

7. **Active Learning:**
   - Select samples based on uncertainty (probability)
   - Example: Query samples with highest prediction uncertainty
   - Use: Efficient data labeling

---

### Question 12 (10 points)
Explain maximum likelihood estimation (MLE) and maximum a posteriori (MAP) estimation. When would you use each?

**Maximum Likelihood Estimation (MLE):**

**Concept:**
- Find parameters that maximize likelihood: θ_MLE = argmax P(data|θ)
- Assumes parameters are fixed (frequentist)
- No prior information

**Example:**
- Linear regression: Find w that maximizes P(y|X, w)
- Assuming y ~ N(Xw, σ²), MLE gives: w = (X^T X)^(-1) X^T y

**Properties:**
- Asymptotically unbiased
- Efficient (lowest variance for large samples)
- Can overfit with small samples

**Maximum A Posteriori (MAP):**

**Concept:**
- Find parameters that maximize posterior: θ_MAP = argmax P(θ|data)
- Uses Bayes' theorem: P(θ|data) ∝ P(data|θ) × P(θ)
- Incorporates prior: θ_MAP = argmax [P(data|θ) × P(θ)]

**Example:**
- Bayesian linear regression with prior: w ~ N(0, αI)
- MAP gives: w = (X^T X + αI)^(-1) X^T y
- Same as ridge regression! (prior = L2 regularization)

**Properties:**
- Regularized (prior prevents overfitting)
- Better for small samples
- Point estimate (not full posterior)

**When to Use:**

**MLE:**
- Large datasets
- No prior knowledge
- Want unbiased estimates
- Example: Large-scale ML with millions of samples

**MAP:**
- Small datasets
- Have prior knowledge
- Want regularization
- Example: Medical diagnosis with limited data, incorporating expert knowledge

**Comparison:**
- **MLE:** Purely data-driven, can overfit
- **MAP:** Data + prior, naturally regularized
- **Full Bayesian:** Full posterior distribution, most information but computationally expensive

**Example:**
- **MLE:** Train neural network on large dataset, no regularization needed
- **MAP:** Train on small dataset, use weight decay (L2 = Gaussian prior)
- **Full Bayesian:** Need uncertainty estimates, have computational resources

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
