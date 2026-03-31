# 📚 AI Diploma - Detailed Unit Descriptions
## Complete Curriculum Extracted from Official PDF

---

# 🎓 SEMESTER 1 - COURSES

---

## 📘 COURSE 1: AIAT 111 - Introduction to AI & Applications
**مقدمة في الذكاء الاصطناعي وتطبيقاته**

| Info | Details |
|------|---------|
| Credit Hours | 3 |
| Lecture Hours | 2/week |
| Practical Hours | 2/week |
| Total Training Hours | 64 (32 theory + 32 practical) |

### Course Description
This course provides an introduction to Artificial Intelligence (AI), covering fundamental concepts, historical context, and modern applications. Students will study the difference between traditional AI approaches (rule-based and search algorithms) and modern AI (data and statistics-based). The course focuses on understanding knowledge representation, logical reasoning, probabilistic modeling, and the basics of machine learning and deep learning.

### Course Learning Outcomes (CLOs)
1. **CLO1**: Distinguish between traditional AI (rule-based) and modern AI (data-driven), explaining key historical milestones and philosophical discussions (like Turing objections)
2. **CLO2**: Apply fundamental AI techniques such as search algorithms (uninformed, heuristic, adversarial) and understand rational agent design (PEAS framework)
3. **CLO3**: Demonstrate knowledge of cognitive systems, including knowledge representation, ontology, and cognitive agent engineering
4. **CLO4**: Use Bayesian probabilities and other probabilistic models to handle uncertainty in AI problems, distinguishing between rule-based and data-driven systems
5. **CLO5**: Implement supervised and unsupervised machine learning pipelines, understanding data preprocessing, encoding, hypothesis space, and loss/optimization
6. **CLO6**: Build and train basic feedforward neural networks for classification or regression tasks, understanding the mathematics of individual neurons and activation functions
7. **CLO7**: Compare different deep learning architectures (CNN, RNN, LSTM), evaluate overfitting vs underfitting, and apply techniques to improve model generalization
8. **CLO8**: Explore generative AI concepts and frameworks, discussing ethical implications and creative applications of models like GANs, Transformers, and Large Language Models

### Unit Structure

#### 📖 Unit 1: Introduction to AI and Applications (12 hours: 6 theory + 6 practical)

**Theoretical Content:**
1. Introduction to Artificial Intelligence
   - What is AI?
   - Weak AI vs Strong AI
   - Typical intelligent systems
   - Brief history of AI
2. Intelligent Agents and Rationality
   - Definition of intelligent agents
   - Components of AI agents
   - Rationality in AI
3. Philosophy of AI
   - Turing's key contributions
   - The Turing Test and its implications
   - Objections to AI
4. Search Algorithms in AI
   - Traditional search techniques (uninformed and heuristic)
   - Greedy search algorithm and applications
5. Adversarial Search and Game Theory
   - Introduction to adversarial search
   - MiniMax algorithm
   - Alpha-Beta pruning
6. Knowledge Representation and Reasoning
   - Knowledge theory in AI
   - Knowledge models and representation
   - Structure of knowledge-based agents
7. Python for AI Development
   - Python basics (lists, dictionaries, loops, if statements)
   - NumPy matrices
   - Reading and writing files in Python
8. Introduction to Generative AI
   - Overview of generative AI frameworks
   - Applications and ethical considerations

**Practical Content:**
- Lectures on AI history and evolution
- Discussions on Weak vs Strong AI and their real-world implications
- Case studies on intelligent agents and rational decision-making
- Explanation of traditional and adversarial search algorithms
- Introduction to knowledge representation and reasoning models in AI
- Overview of generative AI and its applications
- Applied workshops on Python basics for AI
- Implementing search algorithms (uninformed, heuristic, greedy)
- Developing simple intelligent agents using MiniMax and Alpha-Beta pruning
- Exercises on knowledge representation and rule-based systems
- Working with NumPy for data processing in AI applications
- Introduction to generative AI frameworks with simple applications

---

#### 📖 Unit 2: AI Concepts, Terminology, and Application Domains (12 hours: 6 theory + 6 practical)

**Theoretical Content:**
1. Python Basics Review
   - Review of Python basics (lists, dictionaries, loops, functions)
   - Advanced file handling and data processing
   - Working with AI-specific libraries (NumPy, Pandas)
2. Expert Systems
   - Definition and applications of expert systems
   - Components of expert systems
   - Rule-based systems vs machine learning-based systems
   - Forward and backward reasoning in expert systems
3. Knowledge Representation and Reasoning
   - Introduction to ontology and knowledge graphs
   - Working with RDF (Resource Description Framework)
   - Querying knowledge graphs using SPARQL
4. Probabilistic Reasoning and Uncertainty in AI
   - Understanding uncertainty in AI and its challenges
   - Introduction to Bayes' rule in AI
   - Concept and applications of Bayesian statistics
   - Bayes' theorem: formula, interpretation, real-world use cases
   - Practical examples of Bayes' rule with step-by-step solutions
5. Introduction to Machine Learning
   - Overview of machine learning and its importance
   - Types of machine learning:
     - Supervised learning
     - Unsupervised learning
     - Reinforcement learning
   - Data in supervised learning: features, labels, preprocessing
   - Encoding categorical features for ML models
   - Understanding the data generation process in ML

**Practical Content:**
- Applied review of Python basics (lists, dictionaries, file handling)
- Implementing a simple expert system using Python
- Working with RDF and SPARQL for knowledge graph queries
- Applying Bayes' theorem to real-world problems using Python
- Encoding categorical features for ML models
- Developing simple supervised and unsupervised learning models
- Exploring the data generation process using Python and Pandas

---

#### 📖 Unit 3: AI Concepts, Terminology, and Application Domains Part 2 (12 hours: 6 theory + 6 practical)

**Theoretical Content:**
1. Regression vs Classification
   - Definition and key differences
   - When to use each
   - Common models and applications
2. Prediction vs Explanation in ML
   - Accuracy vs interpretability
   - Interpretation methods (SHAP, LIME)
   - Practical use cases
3. Hypothesis Space and Parameters
   - Understanding hypothesis space
   - Parametric vs non-parametric models
   - Model complexity and generalization
4. The Learner and Loss Functions
   - Role of the learner in ML
   - Common loss functions (MSE, Cross-Entropy)
   - Impact on model performance
5. Optimization in ML
   - Optimization basics
   - Gradient descent and its variants
   - Overfitting and local minima
6. Introduction to Deep Learning
   - Overview of neural networks
   - Machine learning vs deep learning
   - Key applications
7. The Neuron and Perceptron
   - Neuron structure and mathematics
   - Activation functions (Sigmoid, ReLU)
   - Types of perceptrons
   - Single-layer vs multi-layer perceptrons
   - Limitations of the perceptron
8. XOR Problem in Neural Networks
   - Why the single neuron fails
   - Importance of non-linearity
   - Solving XOR using neural networks
   - Using hidden layers
   - Implementing XOR with Keras

**Practical Content:**
- Implementing regression and classification models using Python
- Building a perceptron and testing activation functions
- Solving the XOR problem using a neural network in Keras

---

#### 📖 Unit 4: Neural Networks Fundamentals (14 hours: 7 theory + 7 practical)

**Theoretical Content:**
1. The Neuron and Activation Functions
   - Role of activation functions in neural networks
   - Common activation functions (Sigmoid, ReLU, Tanh, Softmax)
   - Mathematical representation and implementation
2. Multi-class Classification and Multi-layer Networks
   - Introduction to multi-class classification problems
   - Multi-layer networks for multi-class classification
   - Implementing multi-class classification with Keras
3. Multi-Layer Perceptrons (MLP)
   - Structure of multi-layer perceptrons (MLP)
   - Forward and backward propagation
   - Training deep neural networks
4. Deep Neural Networks (DNNs)
   - Understanding deep learning and its benefits
   - Challenges in training deep networks
   - Techniques for improving deep learning performance
5. Introduction to Convolutional Neural Networks (CNNs)
   - Structure and components of CNN (convolution, pooling, fully connected layers)
   - Feature extraction in CNNs
   - Real-world applications of CNNs
6. Advanced Deep Learning Architectures
   - Introduction to Recurrent Neural Networks (RNNs)
   - Long Short-Term Memory (LSTM) and Gated Recurrent Units (GRU)
   - Comparison of CNNs and RNNs for different applications
7. Trends in Deep Learning Training
   - Recent developments in neural network training
   - Innovations in hardware and software for AI
   - Transfer learning and pre-trained models
8. Overfitting and Underfitting in Deep Learning
   - Causes and effects of overfitting and underfitting
   - Techniques to prevent overfitting (dropout, regularization)
   - Early stopping as a regularization technique

**Practical Content:**
- Implementing a single neuron with different activation functions using Python
- Building a multi-class classification model with Keras
- Training a multi-layer perceptron (MLP) for classification tasks
- Implementing a CNN for image classification using TensorFlow/Keras
- Experimenting with RNN, LSTM, GRU for sequential data
- Applying early stopping and regularization to prevent overfitting

---

#### 📖 Unit 5: Introduction to Generative AI and Course Summary (14 hours: 7 theory + 7 practical)

**Theoretical Content:**
1. Understanding Binary Classification Problems
   - Definition and examples of binary classification
   - Challenges in binary classification
   - Metrics for evaluating binary classification models (Accuracy, Precision, Recall, F1-score)
2. Diabetes Classification using Feedforward Neural Networks (FFNN)
   - Introduction to medical data classification
   - Role of FFNNs in predicting diseases
   - Challenges and considerations in medical AI
3. Building and Training FFNN for Diabetes Classification
   - Dataset selection and feature engineering
   - Model structure and hyperparameter tuning
   - Training, evaluation, and performance measurement
4. Exploratory Data Analysis (EDA) and Data Preprocessing
   - Understanding and cleaning medical datasets
   - Feature scaling and encoding categorical data
   - Handling missing data and imbalanced classes
5. Introduction to Generative Models
   - What are generative models?
   - Overview of Generative Adversarial Networks (GANs)
   - Transformers and Large Language Models (LLMs)
6. Ethical Implications and Future Trends of Generative AI
   - Bias and fairness in generative AI
   - Concerns about misuse and deepfakes
   - Future of AI-generated content

**Practical Content:**
- EDA and data preprocessing for medical datasets
- Building and training an FFNN for diabetes classification using Python
- Implementing feature scaling, encoding, and handling missing data in a medical dataset
- Experimenting with a simple GAN model or Transformer model for generative AI applications

---

## 📘 COURSE 2: AIAT 112 - Python for AI
**بايثون للذكاء الاصطناعي**

| Info | Details |
|------|---------|
| Credit Hours | 4 |
| Lecture Hours | 2/week |
| Practical Hours | 4/week |
| Total Training Hours | 96 (32 theory + 64 practical) |

### Course Description
This course provides a comprehensive introduction to fundamental concepts of AI, including basic algorithms, data structures, and theoretical foundations. Students will develop practical skills in applying AI techniques in Python through practical projects. The curriculum explores real-world AI applications such as game engines, handwriting recognition, and machine translation, providing insights into their practical impacts.

### Course Learning Outcomes (CLOs)
1. **CLO1**: Implement and demonstrate at least three main AI algorithms (such as A* search, k-nearest neighbors, decision trees) using Python
2. **CLO2**: Complete a practical project applying machine learning techniques to a real problem, demonstrating ability to integrate AI concepts in practical applications
3. **CLO3**: Evaluate AI model performance using appropriate metrics (accuracy, precision, recall, F1-score), and discuss the implications of these metrics in project context
4. **CLO4**: Analyze case studies of AI applications, identifying algorithms used and evaluating their effectiveness in solving specific problems
5. **CLO5**: Design and implement a prototype of an intelligent system incorporating at least two different AI techniques (such as NLP and machine learning), demonstrating creativity and technical competence

### Unit Structure

#### 📖 Unit 1: Course Introduction and Search Algorithms (18 hours: 6 theory + 12 practical)

**Theoretical Content:**
1. Introduction to AI Applications
   - Defining the scope of AI
   - Overview of AI in different industries (healthcare, finance, autonomous systems)
   - Ethical and social dimensions of AI
2. Fundamental Algorithms in AI
   - Search algorithms (Depth-First Search, Breadth-First Search, Greedy Best-First Search, A*)
   - Adversarial search (Minimax, Alpha-Beta pruning)
   - Optimization algorithms in AI
3. Search Algorithms in AI
   - Depth-First Search (DFS)
   - Breadth-First Search (BFS)
   - Greedy Best-First Search (GBFS)
   - A* Search Algorithm
4. Adversarial Search and Game AI
   - Minimax algorithm
   - Alpha-Beta pruning
5. AI Learning Methodology and Course Structure
   - Practical training in coding and implementation
   - Industrial case studies and practical applications
   - Self-learning and research components
6. AI Model Performance Analysis
   - Evaluating search algorithms (efficiency, completeness)
   - Trade-offs between different AI approaches
   - Comparing model effectiveness in real-world applications

**Practical Content:**
- Real-world AI applications
- Implementing AI algorithms
- Implementing search algorithms
- Implementing adversarial search
- AI learning methods and research
- Evaluating AI models

---

#### 📖 Unit 2: Knowledge Representation (19 hours: 6 theory + 13 practical)

**Theoretical Content:**
1. Introduction to Propositional Logic
   - Definition and importance
   - Basic components: propositions and logical connectives
2. Truth Tables and Logical Operators
   - Building truth tables
   - Logical operators: AND, OR, NOT, IMPLIES, BICONDITIONAL
   - Logical equivalences and simplifications
3. Applications of Propositional Logic
   - Real-world use cases
   - Simple logical reasoning problems
4. Logical Reasoning and Inference Rules
   - Understanding inference: definition and examples
   - Key inference rules:
     - Modus Ponens
     - Modus Tollens
     - Disjunctive Syllogism
   - Proof techniques in propositional logic
5. Building Logical Arguments
   - Valid vs invalid arguments
   - Identifying common logical fallacies
6. Introduction to Model Checking
   - Definition and importance in computer science
   - Overview of model checking process
7. Temporal Logic and Model Checking Systems
   - Basic concepts: states, transitions, properties
   - Examples of model checking systems
8. Inference in Propositional Logic
   - Definition and inference principle
   - Steps for applying inference
   - Applications in AI and theorem proving
9. Introduction to First-Order Logic (FOL)
   - Differences between propositional and first-order logic
   - Syntax and semantics in first-order logic

**Practical Content:**
- Building truth tables for logical propositions using Python
- Implementing logical operators (AND, OR, NOT, IMPLIES, BICONDITIONAL)
- Applying inference rules (Modus Ponens, Modus Tollens, Disjunctive Syllogism) to solve logical problems
- Building logical arguments and validating them programmatically
- Implementing model checking algorithms for temporal logic
- Working with First-Order Logic (FOL) syntax and semantics
- Applying logical reasoning to solve AI problems (like knowledge-based systems)
- Writing code to parse and evaluate FOL formulas

---

#### 📖 Unit 3: Learning Under Uncertainty (19 hours: 6 theory + 13 practical)

**Theoretical Content:**
1. Introduction to Bayesian Networks
   - Motivation for probabilistic reasoning
   - Conditional independence and its role
   - Structure and semantics of Bayesian networks
2. Inference in Bayesian Networks
   - Exact inference methods
   - Approximate inference (sampling methods)
   - Applications in decision-making
3. Hidden Markov Models (HMMs)
   - Structure and components of HMMs
   - Forward-backward algorithm
   - Viterbi algorithm for sequence prediction
4. Applications of HMMs
   - Speech recognition
   - Part-of-speech tagging
   - Biological sequence analysis
5. Introduction to Reinforcement Learning
   - Basic concepts: agents, environments, rewards
   - Markov Decision Processes (MDPs)
   - Policy and value functions

**Practical Content:**
- Building Bayesian networks using Python libraries (pgmpy)
- Implementing inference algorithms for Bayesian networks
- Working with Hidden Markov Models (HMMs) for sequence prediction
- Implementing Viterbi algorithm for sequence decoding
- Applying HMMs to practical problems (speech recognition, POS tagging)
- Introduction to reinforcement learning: setting up environments and agents
- Implementing simple MDPs and value iteration algorithms

---

#### 📖 Unit 4: Optimization Techniques (20 hours: 7 theory + 13 practical)

**Theoretical Content:**
1. Gradient Descent Optimization
   - Basic gradient descent algorithm
   - Variants: batch, stochastic, mini-batch
   - Learning rate scheduling
2. Advanced Optimization Algorithms
   - Momentum-based methods
   - Adam optimizer
   - RMSprop
3. Regularization Techniques
   - L1 and L2 regularization
   - Dropout
   - Early stopping
4. Hyperparameter Tuning
   - Grid search and random search
   - Cross-validation techniques
   - Bayesian optimization

**Practical Content:**
- Implementing gradient descent algorithms (batch, stochastic, mini-batch)
- Applying advanced optimizers (Adam, RMSprop) in neural networks
- Implementing regularization techniques (L1, L2, Dropout, Early Stopping)
- Performing hyperparameter tuning using grid search and random search
- Using cross-validation to select optimal hyperparameters
- Comparing different optimization algorithms on real datasets
- Implementing Bayesian optimization for hyperparameter search

---

#### 📖 Unit 5: AI-Based Learning Models (20 hours: 7 theory + 13 practical)

**Theoretical Content:**
1. Neural Network Architectures
   - Feedforward networks
   - Convolutional neural networks
   - Recurrent neural networks
2. Transfer Learning
   - Pre-trained models
   - Fine-tuning strategies
   - Domain adaptation
3. Model Evaluation and Selection
   - Performance metrics
   - Cross-validation
   - Model comparison techniques
4. Deploying AI Models
   - Model serialization
   - API development
   - Production considerations

**Practical Content:**
- Implementing different neural network architectures (feedforward, CNN, RNN)
- Applying transfer learning with pre-trained models (VGG, ResNet, BERT)
- Fine-tuning pre-trained models for domain-specific tasks
- Performing model evaluation and comparison using cross-validation
- Implementing model selection techniques
- Serializing and saving models for deployment
- Building simple APIs for model serving (Flask, FastAPI)
- Working on end-to-end projects integrating multiple AI techniques

---

## 📘 COURSE 3: AIAT 113 - Mathematics & Probability for ML
**الرياضيات والاحتمالات لتعلم الآلة**

| Info | Details |
|------|---------|
| Credit Hours | 3 |
| Lecture Hours | 2/week |
| Practical Hours | 2/week |
| Total Training Hours | 64 (32 theory + 32 practical) |

### Course Learning Outcomes (CLOs)
1. **CLO1**: Apply linear algebra concepts (vectors, matrices, transformations) to machine learning problems
2. **CLO2**: Use calculus and multivariate calculus for optimization in ML
3. **CLO3**: Apply probability theory and statistical inference to ML models
4. **CLO4**: Implement dimensionality reduction techniques (PCA, SVD, t-SNE)
5. **CLO5**: Understand and apply Bayesian inference methods
6. **CLO6**: Connect mathematical foundations to practical ML implementations

### Unit Structure

#### 📖 Unit 1: Linear Algebra for Machine Learning and Data Transformations (12 hours: 6 theory + 6 practical)

**Theoretical Content:**
1. Machine Learning and Linear Algebra Fundamentals
   - Relationship between ML, vectors, and matrices
   - Impact of parameter changes on model fit to training data
   - Understanding model parameters as vectors on the response surface
   - Concept of vectors beyond physical space
2. Vector Operations and Linear Algebra Fundamentals
   - Vector addition and scalar multiplication
   - Solving linear algebra problems using substitution and elimination
   - Dot product, magnitude, and negation of vectors
   - Concept of basis change
   - Linear independence and basis selection
3. Matrix Operations and Transformations
   - Defining matrices as transformations
   - Computing inverse matrix and determinant
   - Methods for computing inverse matrix and potential issues
4. Matrices as Factors and Basis Transformations
   - Transformation matrices and their relation to new basis vectors
   - Programming map transformations using transformation matrices
   - Computational method for finding orthogonal basis sets
5. Eigenvectors and Eigenvalues
   - Geometric interpretation of eigenvectors and eigenvalues
   - Mathematical formulation and application in simple cases
   - Intuitive understanding of eigenvector systems in higher dimensions
   - Programming solutions for high-dimensional eigenvalue problems

**Practical Content:**
- Performing vector and matrix operations using Python/NumPy
- Implementing substitution/elimination techniques for solving linear equations
- Computing determinants and inverse matrices computationally
- Writing code to apply transformation matrices and compute orthogonal basis sets
- Solving eigenvalue problems programmatically and applying eigenvalue analysis on large-dimensional matrices
- Experimenting with changes in ML model parameters and observing changes in model fit

---

#### 📖 Unit 2: Calculus and Multivariate Calculus for Machine Learning (12 hours: 6 theory + 6 practical)

**Theoretical Content:**
1. Calculus Fundamentals
   - Definition and importance of calculus
   - Basic rules and techniques of differentiation
   - Applying differentiation to simple functions
   - Time-saving rules in differentiation
   - Applications of sum rule, product rule, and chain rule
2. Multivariate Calculus
   - Differentiation with multiple variables
   - Partial derivatives and their importance
   - Representation of vectors and matrices in multivariate calculus
   - Jacobian matrix and its applications in optimization
3. Calculus in Neural Networks
   - Applying multivariate chain rule to nested functions
   - Understanding neural network structure and function
   - Using multivariate calculus to link network parameters to outputs
   - Implementing backpropagation in a simple neural network
4. Power Series and Function Approximations
   - Understanding function approximation using power series
   - Power series behavior for complex and ill-conditioned functions
   - Concept and importance of function flattening
   - Choosing appropriate representations for multivariate approximations

**Practical Content:**
- Solving differentiation problems using symbolic computation tools
- Implementing gradient computations for multivariate functions
- Programming backpropagation in neural networks using differentiation techniques
- Applying function approximation on real-world ML models

---

#### 📖 Unit 3: Optimization and Statistical Foundations for Machine Learning (12 hours: 6 theory + 6 practical)

**Theoretical Content:**
1. Gradient Descent and Model Optimization
   - Principles of gradient descent
   - Optimization challenges and local minima issues
   - Constrained optimization using Lagrange multipliers
   - Cases where gradient descent fails
2. Regression and Model Fitting
   - Regression as an error minimization problem
   - Choosing appropriate models for different data types
   - Applying multivariate calculus in regression computation
   - Implementing gradient descent for non-linear function fitting
3. Statistical Analysis and Data Transformations
   - Computing means, variances, and covariances
   - Impact of linear transformations on statistical measures
   - Statistical representations for image data
   - Writing code for data analysis and transformations
4. Inner Product and Distance Measures
   - Understanding inner product and its properties
   - Computing angles and distances in high-dimensional spaces
   - Applications of inner product in data comparison
   - Implementing image similarity measures
5. Orthogonal Projections and Dimensionality Reduction
   - Computing orthogonal projections using inner product
   - Understanding reconstruction errors and their impact
   - Practical applications of projections in data compression
   - Writing code for dimensionality reduction of image datasets

**Practical Content:**
- Implementing gradient descent for optimization problems
- Applying regression techniques to fit models on real datasets
- Writing code to compute basic statistical properties of datasets
- Representing images as vectors and computing angles and distances between them
- Implementing projection and dimensionality reduction techniques in ML

---

#### 📖 Unit 4: Dimensionality Reduction and Data Representation Techniques (14 hours: 7 theory + 7 practical)

**Theoretical Content:**
1. Principal Component Analysis (PCA)
   - Concept and mathematical basis of PCA
   - Properties of PCA in high-dimensional spaces
   - Implementing PCA in Python
   - Applications of PCA in data compression and visualization
2. Singular Value Decomposition (SVD)
   - Understanding SVD fundamentals
   - Implementing SVD in Python
   - Analyzing properties and importance of SVD
   - Comparing SVD and PCA in data analysis
3. t-SNE (t-distributed Stochastic Neighbor Embedding)
   - Introduction to t-SNE and its use in non-linear dimensionality reduction
   - Implementing t-SNE in Python for data visualization
   - Analyzing properties and effectiveness of t-SNE
   - Comparing t-SNE with PCA and SVD for high-dimensional data analysis

**Practical Content:**
- Implementing PCA using Python for dimensionality reduction of datasets
- Applying SVD for matrix decomposition, data compression, and noise reduction
- Using t-SNE for visualizing high-dimensional data in 2D or 3D dimensions
- Comparing PCA, SVD, and t-SNE for different data analysis tasks
- Writing code to apply these dimensionality reduction techniques on real-world datasets including images and text data

---

#### 📖 Unit 5: Probability, Sampling, and Statistical Inference (14 hours: 7 theory + 7 practical)

**Theoretical Content:**
1. Probability and Distributions
   - Basic concepts: sample spaces, events, discrete vs continuous distributions
   - Common probability distributions (Gaussian, Bernoulli, Poisson)
   - Central Limit Theorem and its applications
2. Sampling and Estimation
   - Sampling methods and their properties
   - Point estimation and confidence intervals
   - Maximum Likelihood Estimation (MLE)
3. Bayesian Inference
   - Bayes' theorem and posterior distributions
   - Prior selection and conjugate priors
   - Markov Chain Monte Carlo (MCMC) methods
4. Hypothesis Testing
   - Null and alternative hypotheses
   - Type I and Type II errors
   - p-values and significance testing

**Practical Content:**
- Implementing probability distributions in Python (Gaussian, Bernoulli, Poisson)
- Applying Central Limit Theorem with simulations
- Performing sampling and point estimation
- Implementing Maximum Likelihood Estimation (MLE) for different distributions
- Applying Bayesian inference using Python (PyMC3, Stan)
- Implementing hypothesis testing procedures
- Computing p-values and confidence intervals
- Connecting probability theory to ML model implementations

---

## 📘 COURSE 4: AIAT 114 - ML Algorithms & Applications
**خوارزميات تعلم الآلة وتطبيقاتها**

| Info | Details |
|------|---------|
| Credit Hours | 4 |
| Lecture Hours | 2/week |
| Practical Hours | 4/week |
| Total Training Hours | 96 (32 theory + 64 practical) |

### Course Learning Outcomes (CLOs)
1. **CLO1**: Implement and evaluate regression algorithms for predictive modeling
2. **CLO2**: Apply classification algorithms and understand their decision boundaries
3. **CLO3**: Implement and compare clustering algorithms for unsupervised learning
4. **CLO4**: Apply dimensionality reduction techniques in practical scenarios
5. **CLO5**: Use ensemble methods and boosting techniques to improve model performance
6. **CLO6**: Evaluate models using appropriate metrics and cross-validation
7. **CLO7**: Apply hyperparameter tuning and model selection techniques

### Unit Structure

#### 📖 Unit 1: Regression Algorithms (12 hours: 6 theory + 6 practical)

**Theoretical Content:**
1. Introduction to Regression
   - Simple linear regression
   - Multiple linear regression
   - Polynomial regression
2. Regularization in Regression
   - Ridge regression (L2 regularization)
   - Lasso regression (L1 regularization)
   - Elastic Net
3. Advanced Regression Techniques
   - Support Vector Regression (SVR)
   - Decision tree regression
   - Random forest regression

**Practical Content:**
- Implementing simple and multiple linear regression using scikit-learn
- Applying polynomial regression for non-linear relationships
- Implementing Ridge and Lasso regression with regularization
- Building SVR models with different kernels
- Implementing decision tree and random forest regression
- Comparing regression algorithms on real datasets
- Visualizing regression results and residuals

---

#### 📖 Unit 2: Regression and Model Evaluation (12 hours: 6 theory + 6 practical)

**Theoretical Content:**
1. Model Evaluation Metrics
   - Mean Squared Error (MSE), Root MSE
   - Mean Absolute Error (MAE)
   - R-squared and Adjusted R-squared
2. Cross-Validation
   - K-fold cross-validation
   - Leave-one-out cross-validation
   - Stratified cross-validation
3. Bias-Variance Tradeoff
   - Understanding bias and variance
   - Overfitting and underfitting
   - Model complexity selection

**Practical Content:**
- Computing regression evaluation metrics (MSE, RMSE, MAE, R²)
- Implementing k-fold cross-validation for regression models
- Performing leave-one-out and stratified cross-validation
- Analyzing bias-variance tradeoff through learning curves
- Identifying and handling overfitting/underfitting
- Selecting optimal model complexity using validation sets
- Comparing model performance across different algorithms

---

#### 📖 Unit 3: Classification Algorithms (19 hours: 6 theory + 13 practical)

**Theoretical Content:**
1. Logistic Regression
   - Sigmoid function and decision boundaries
   - One-vs-Rest (OvR) strategies for multi-class classification
   - Understanding binary and multi-class classification problems
2. Decision Trees and Random Forests
   - Decision tree structure and splitting criteria (Entropy, Gini impurity)
   - Overfitting in decision trees and pruning techniques
   - Introduction to ensemble methods and how random forests improve stability
   - Concept of bagging and feature importance in random forests
3. Support Vector Machines (SVM) for Classification
   - Concept of hyperplanes and margins in SVM
   - Role of kernels (linear, polynomial, RBF) in non-linear classification
   - Tuning model parameters (C and gamma) to improve classification performance
   - Comparing SVM with other classifiers
4. Naive Bayes Classifier
   - Understanding conditional probabilities and Bayes' theorem
   - Types of Naive Bayes classifiers (Gaussian, Multinomial, Bernoulli)
   - Assumptions and when to use Naive Bayes in real-world applications
   - Strengths and weaknesses of Naive Bayes
5. Model Evaluation Metrics for Classification
   - Understanding confusion matrices and their components (TP, FP, TN, FN)
   - Precision, True Positive Rate, Recall, and F1-score
   - ROC curves, AUC, and Precision-Recall curves for performance evaluation
   - Choosing appropriate metrics for different classification problems
6. Ensemble Learning and Advanced Techniques
   - Introduction to ensemble methods (Bagging, Boosting, Stacking)
   - Exploring random forests as a Bagging method
   - Introduction to boosting algorithms (AdaBoost, Gradient Boosting)
   - Comparing ensemble models with independent classifiers

**Practical Content:**
- Implementing logistic regression for binary and multi-class classification using Python (scikit-learn)
- Building decision tree models and understanding pruning techniques to avoid overfitting
- Applying random forest classifiers to improve prediction accuracy
- Using SVM with different kernels (linear, polynomial, RBF) to handle complex classification tasks
- Implementing Naive Bayes for text classification tasks like spam filtering
- Evaluating classification models using confusion matrices, ROC curves, and analyzing precision and recall
- Experimenting with ensemble techniques (Bagging, Boosting) to improve classification performance

---

#### 📖 Unit 4: Clustering and Dimensionality Reduction (20 hours: 7 theory + 13 practical)

**Theoretical Content:**
1. Clustering Techniques
   - Introduction to clustering and its applications
   - K-Means clustering
   - Algorithm and optimization techniques
   - Choosing the correct number of clusters (Elbow method, Silhouette score)
2. Hierarchical Clustering
   - Agglomerative vs divisive approaches
   - Linkage criteria (single, complete, average)
3. DBSCAN (Density-Based Spatial Clustering of Applications with Noise)
   - Handling noise and outliers
   - Advantages compared to K-Means and hierarchical clustering
4. Dimensionality Reduction
   - Need for dimensionality reduction in ML
   - Principal Component Analysis (PCA)
   - Eigenvalues, eigenvectors, and explained variance
   - Application in data compression and noise reduction
5. Linear Discriminant Analysis (LDA)
   - Comparison with PCA
   - Application in classification problems
6. Visualization and Model Evaluation
   - Choosing appropriate distance metrics (Euclidean, Manhattan, Cosine similarity)
   - Evaluating clustering performance (Silhouette score, Davies-Bouldin index)
   - Visualizing high-dimensional data in low-dimensional spaces using t-SNE and UMAP

**Practical Content:**
- Implementing K-Means, hierarchical clustering, and DBSCAN in Python
- Using Elbow method and Silhouette score to determine optimal number of clusters
- Applying PCA for dimensionality reduction and visualization of high-dimensional data
- Implementing LDA for improving classification performance
- Evaluating clustering models using appropriate metrics
- Visualizing transformed data using tools like t-SNE and UMAP

---

#### 📖 Unit 5: Model Selection and Boosting (20 hours: 7 theory + 13 practical)

**Theoretical Content:**
1. Model Selection and Hyperparameter Tuning
   - Importance of model selection in ML
   - Cross-validation techniques (k-fold, stratified, leave-one-out)
   - Hyperparameter tuning: Grid Search vs Random Search
   - Automatic tuning methods and Bayesian optimization
2. Boosting Techniques for Performance Improvement
   - Boosting fundamentals and its impact on model performance
   - AdaBoost: working mechanism and practical applications
   - Gradient Boosting: key principles and advantages
   - XGBoost: optimized boosting for large-scale data
   - Comparing boosting with other ensemble methods
3. Comprehensive Model Evaluation
   - Importance of comprehensive evaluation in ML
   - Metrics for different model types (classification, regression)
   - Precision, Recall, F1-score, ROC-AUC for classification models
   - RMSE, R², MAE for regression models
   - Balance between bias and variance and its impact on model performance
4. Final Project and Course Summary
   - Review of key concepts covered during the course
   - Best practices in model selection and evaluation
   - Presentation of final projects and feedback session
   - Real-world applications and future trends in ML

**Practical Content:**
- Implementing cross-validation and hyperparameter tuning using Python
- Using Grid Search and Random Search in scikit-learn to optimize parameters
- Building and training boosting models using libraries like XGBoost and LightGBM
- Comparing performance with traditional methods
- Evaluating models on real datasets using performance metrics
- Applying confusion matrices, plotting ROC curves for classification models
- Tuning models for optimal performance and documenting improvements
- Implementing final project: applying learned techniques on real dataset, evaluating results, presenting key insights

---

## 📘 COURSE 5: AIAT 115 - Scalable Data Science
**علوم البيانات القابلة للتوسع**

| Info | Details |
|------|---------|
| Credit Hours | 4 |
| Lecture Hours | 2/week |
| Practical Hours | 4/week |
| Total Training Hours | 96 (32 theory + 64 practical) |

### Course Description
This is an immersive course aimed at equipping learners with the skills necessary to analyze and interpret complex datasets effectively using Python. The course begins with fundamental concepts in data science and progresses to scalable techniques for handling large datasets. Students will explore fundamental libraries, tools, and methodologies that enable them to build solutions that are powerful, efficient, and scalable. By the end of the course, participants will be ready to handle real-world data challenges with confidence.

### Course Learning Outcomes (CLOs)
1. **CLO1**: Demonstrate ability to analyze and visualize data using Python with confidence in various contexts
2. **CLO2**: Identify and implement strategies to scale data processing tasks effectively
3. **CLO3**: Clean and prepare raw datasets to make them suitable for analysis and modeling
4. **CLO4**: Build, evaluate, and deploy machine learning models using Python in scalable environments
5. **CLO5**: Complete a data science project that includes large-scale data and models

### Unit Structure

#### 📖 Unit 1: Introduction to Data Science (18 hours: 6 theory + 12 practical)

**Theoretical Content:**
1. Overview of Data Science and Applications
   - What is data science?
   - Basic components of data science: data collection, cleaning, analysis, and visualization
   - Types of data science problems (supervised, unsupervised, reinforcement learning)
   - Data science applications across industries (healthcare, finance, e-commerce, etc.)
   - Importance of data science in decision-making and business strategy
2. Python Basics for Data Science
   - Introduction to Python for data science
   - Basic Python rules and structures (variables, operations, expressions)
   - Control flow: if statements, loops (for, while)
   - Functions in Python: defining and using functions
   - Introduction to list comprehensions and lambda functions
   - Handling exceptions and debugging in Python
3. Introduction to Jupyter Notebooks
   - What are Jupyter Notebooks?
   - Installing and setting up Jupyter Notebooks
   - Creating, running, and saving notebooks
   - Basic notebook structure: cells (code vs markdown)
   - Importing and using Python libraries in Jupyter
   - Best practices for using Jupyter Notebooks for documentation and reproducibility
4. Data Types and Structures in Python
   - Primitive data types: integers, floats, strings, booleans
   - Collections: lists, tuples, sets, dictionaries
   - Data structures for data science: matrices, DataFrames, Series
   - Working with DataFrames in Pandas and cuDF
   - Indexing, slicing, and manipulating data in lists and matrices
   - Understanding immutability in tuples and strings
5. Introduction to Libraries: NumPy, Pandas, cuDF, Numba
   - NumPy: Introduction to NumPy arrays, matrix manipulation, mathematical operations
   - Pandas: Working with Series and DataFrames, data cleaning and processing, handling missing data
   - cuDF: Overview of cuDF for data manipulation using GPU acceleration, comparing cuDF with Pandas
   - Numba: Introduction to Numba for accelerating Python code using JIT (Just-In-Time) compilation
   - Performance optimization: When to use NumPy, Pandas, cuDF, and Numba in data science workflow
   - Basic visualization using Matplotlib and Seaborn with data from Pandas and cuDF

**Practical Content:**
- Python Programming: Executing Python code to solve basic tasks like arithmetic operations, loops, and conditions
- Using Jupyter Notebooks: Writing and executing code in Jupyter Notebooks, combining explanation and code to ensure reproducibility
- Working with Data Structures: Performing tasks like indexing, slicing, and transforming data using lists and dictionaries
- NumPy, Pandas, cuDF: Practicing data manipulation tasks like handling missing data and aggregation using NumPy and Pandas
- Data Science Applications: Working on small real-world projects using data science principles to solve industry-specific problems

---

#### 📖 Unit 2: Data Cleaning and Preparation (19 hours: 6 theory + 13 practical)

**Theoretical Content:**
1. Data Import and Export
   - Importing data from CSV, Parquet, and other file formats using cuDF
   - Exporting processed data to different file formats for later analysis
   - Integrating cuDF with other data sources like SQL databases or cloud storage
2. Data Cleaning Techniques
   - Identifying and removing duplicate data in datasets
   - Handling inconsistent or incorrect inputs
   - Data normalization to achieve consistency and accuracy
3. Handling Missing Data
   - Identifying missing values and understanding their impact
   - Techniques for imputing missing values using statistical methods
   - Removing or replacing missing values based on context
4. Data Transformation and Feature Engineering
   - Transforming raw data to useful features (e.g., scaling, encoding)
   - Creating new features using domain knowledge and existing variables
   - Feature extraction techniques for unstructured data (e.g., text or images)
5. Exploratory Data Analysis (EDA)
   - Visualizing distributions and relationships within data
   - Using statistical summaries to extract insights about data patterns
   - Identifying outliers and extreme values using statistical methods
6. GPU-Accelerated Data Processing
   - Understanding how GPU accelerates data manipulation tasks for large datasets

**Practical Content:**
- Import/Export using cuDF: Importing and exporting data in different formats using cuDF functions
- Data Cleaning: Discovering and fixing data issues like duplication and inconsistency using cuDF
- Handling Missing Data: Applying techniques to manage missing values including imputation and removal
- Feature Transformation: Transforming data (e.g., scaling, encoding) to prepare it for analysis
- Performing EDA: Visualizing data distributions and relationships to discover insights
- Optimization using cuDF: Using GPU acceleration from cuDF to process data faster

---

#### 📖 Unit 3: Data Visualization (19 hours: 6 theory + 13 practical)

**Theoretical Content:**
1. Using Matplotlib and Seaborn
   - Matplotlib: Introduction to creating static, animated, and interactive visualizations
   - Creating charts using Seaborn: Leveraging Seaborn to create advanced statistical charts
   - Customizing visualizations: Adjusting labels, colors, themes, and adding annotations in Matplotlib and Seaborn
2. Creating Different Types of Visualizations
   - Line and bar charts: Creating line charts, bar charts, and histograms
   - Scatter plots and heatmaps: Creating scatter plots for relationships and heatmaps for correlations
   - Pair plots: Using Seaborn's pairplot for multi-variable visualization
   - Box plots and violin plots: Creating box plots and violin plots for distribution visualization
3. Interactive Visualizations with Plotly
   - Introduction to Plotly for interactive data visualization
   - Creating interactive dashboards with Plotly
   - Comparing static vs interactive visualizations
4. Building Dashboards with Plotly
   - Creating interactive dashboards using Plotly
   - Exploring basic integration techniques for web-based use

**Practical Content:**
- Creating various chart types using Matplotlib and Seaborn
- Building interactive visualizations and dashboards with Plotly
- Customizing and annotating visualizations for presentations
- Applying visualization best practices for data storytelling

---

#### 📖 Unit 4: Introduction to Machine Learning (20 hours: 7 theory + 13 practical)

**Theoretical Content:**
1. Overview of Machine Learning Concepts
   - Definition and types of machine learning
   - Machine learning workflow
   - Practical applications of machine learning
2. Supervised vs Unsupervised Learning
   - Supervised learning: classification and regression
   - Unsupervised learning: clustering and dimensionality reduction
   - Key differences between supervised and unsupervised learning
3. Introduction to Scikit-learn
   - Installing and setting up Scikit-learn
   - Main modules and functions in Scikit-learn
   - Practical application using Scikit-learn
4. Building and Evaluating Machine Learning Models
   - Data preparation and feature engineering
   - Model training and validation
   - Model evaluation metrics
5. Hyperparameter Optimization
   - Understanding hyperparameters and model tuning
   - Grid Search and Random Search
   - Regularization and the overfitting problem

**Practical Content:**
- Working with data using Python libraries like Pandas
- Cleaning and preparing data for ML tasks (handling missing values, encoding categorical variables)
- Implementing ML models using Scikit-learn library (regression, classification)
- Applying supervised learning algorithms on labeled data (e.g., logistic regression)
- Applying unsupervised learning techniques (e.g., K-means clustering) on unlabeled data
- Model selection and evaluation: Training models on training datasets and evaluating them on test datasets
- Hyperparameter tuning using techniques like Grid Search and Random Search
- Real-world problem solving using a mix of supervised and unsupervised learning algorithms

---

#### 📖 Unit 5: Extending the Scope of Data Science (20 hours: 7 theory + 13 practical)

**Theoretical Content:**
1. Introduction to Big Data Concepts
   - Big data characteristics (Volume, Variety, Velocity, Veracity)
   - Big data technologies
   - Big data challenges
2. Using Dask and PySpark for Scaling
   - Introduction to Dask
   - PySpark basics
   - Dask vs PySpark
3. Distributed Computing Fundamentals
   - Distributed systems
   - Parallel computing and MapReduce
   - Fault tolerance
4. NVIDIA RAPIDS Framework
   - Overview of RAPIDS: Introduction to RAPIDS for GPU-powered data science
   - GPU-accelerated processing: Accelerating data processing with GPU support
   - RAPIDS integration: Using RAPIDS with libraries like Pandas and Scikit-learn
5. Deploying Machine Learning Models
   - Deployment methodology
   - APIs (Application Programming Interfaces) for model serving
   - Scaling and monitoring

**Practical Content:**
- Working with Dask: Using Dask to distribute operations on large datasets, allowing faster data processing and analysis across multiple cores or machines
- Data Processing using PySpark: Implementing PySpark to perform distributed data processing on large datasets and integrating with existing Python workflows
- Accelerated Data with GPU using RAPIDS: Using RAPIDS libraries (like cuDF data frame) to accelerate data processing tasks like filtering, merging, and aggregation on large datasets
- Deploying Models using API Interfaces: Deploying machine learning models using frameworks like Flask or FastAPI to serve predictions in real-time, making them integrable with web applications
- Scaling and Monitoring for Deployed Models: Implementing strategies for monitoring models, tracking real-time performance, and scaling model deployment to handle larger data loads

---

## 📘 COURSE 6: AIAT 116 - AI Ethics
**أخلاقيات الذكاء الاصطناعي**

| Info | Details |
|------|---------|
| Credit Hours | 3 |
| Lecture Hours | 2/week |
| Practical Hours | 2/week |
| Total Training Hours | 64 (32 theory + 32 practical) |

### Course Description
This course explores the ethical implications, societal impacts, and responsible development of AI and data-driven technologies. Students will interact with ethical frameworks, regulatory guidelines, and case studies to analyze biases, privacy concerns, transparency, accountability, and fairness in AI systems critically. Through discussions and practical activities, learners will develop ethical decision-making skills and understand how to align AI applications with human values, legal requirements, and industry best practices.

### Course Learning Outcomes (CLOs)
1. **CLO1**: Explain ethical frameworks (e.g., utilitarianism, deontology, virtue ethics) and their relevance to AI development; analyze case studies of AI ethics violations.
2. **CLO2**: Identify and analyze bias, fairness, and discrimination in AI systems; apply bias detection and mitigation techniques and fairness metrics.
3. **CLO3**: Assess privacy, security, and data protection risks in AI applications; apply relevant regulations (e.g., GDPR, CCPA) and privacy-preserving techniques.
4. **CLO4**: Evaluate transparency, interpretability, and accountability in AI systems; apply XAI techniques (e.g., LIME, SHAP) and accountability frameworks.
5. **CLO5**: Analyze AI governance, regulations, and future challenges; formulate ethics policies and comply with legal frameworks.

### Unit Structure

#### 📖 Unit 1: Foundations of AI Ethics (12 hours: 6 theory + 6 practical)

**Theoretical Content:**
1. Introduction to Ethics in AI
   - Definition of ethics and its importance in AI and data science
   - Ethical considerations vs legal considerations in AI development
   - The role of ethics in responsible AI development and data-driven decision-making
2. Ethical Theories and Frameworks
   - Utilitarianism, Deontology, and Virtue Ethics in AI
   - Consequentialism vs duty-based ethics in algorithmic decisions
   - The principle of beneficence and minimizing harm in AI applications
3. Ethical Challenges in AI
   - Unintended consequences of AI systems
   - Ethical dilemmas in autonomous decision-making
   - AI impact on employment, inequality, and human rights
4. Ethical Responsibility in AI Development
   - Who is responsible for AI decisions? Developers, organizations, or users?
   - Ethics of autonomy and decision-making in AI
   - Ethical considerations of AI for social good
5. Case Studies on AI Ethics Violations
   - AI in crime prediction: racial bias in algorithms
   - Ethical concerns in facial recognition technologies
   - Cambridge Analytica scandal: data misuse and privacy violation
   - Bias in hiring algorithms: case studies from industry

**Practical Content:**
- Case Studies Analysis: Investigating real ethical failures in AI systems
- Detecting Bias in AI Models: Identifying biases in datasets and algorithms and applying mitigation strategies
- Privacy Simulation: Assessing privacy risks in AI applications
- Debate on Ethical Dilemmas: Discussing ethical conflicts related to AI and associated responsibilities
- Ethics Review Board (Simulation): Evaluating an AI system in terms of ethical risks and regulatory compliance
- Algorithmic Fairness Testing: Applying fairness metrics and interpreting AI decisions
- Policy Writing Exercise: Formulating an AI ethics policy for a company or organization

---

#### 📖 Unit 2: Bias, Fairness, and Discrimination in AI (12 hours: 6 theory + 6 practical)

**Theoretical Content:**
1. Understanding Bias in AI
   - Definition of bias types (data bias, algorithmic bias, human bias)
   - Sources of bias in AI models (data collection, feature selection, model training)
   - Real examples of biased AI systems
2. Fairness in AI Decision-Making
   - Defining fairness: group fairness vs individual fairness
   - Fairness criteria (demographic parity, equal opportunity, equal odds)
   - Balance between accuracy and fairness in AI models
3. Discrimination and Ethical Implications
   - Discriminatory outcomes in AI (hiring, lending, healthcare, policing)
   - Legal and ethical frameworks to prevent discrimination in AI
   - Regulatory guidelines (GDPR, AI Act, Equal Credit Opportunity Act)
4. Bias Detection and Mitigation Techniques
   - Methods for detecting bias in data and models
   - Bias mitigation techniques: pre-processing, in-processing, post-processing
   - Fair learning and adversarial debiasing
5. Transparency and Interpretability in AI Models
   - Importance of Explainable AI (XAI) in fairness
   - Techniques for improving model interpretability (LIME, SHAP, counterfactual analysis)
   - Challenges in achieving transparent and accountable AI
6. Case Studies on Bias and Fairness
   - Facial recognition and racial bias
   - Gender bias in hiring algorithms
   - Crime prediction and AI use in criminal justice
   - Discrimination in credit scoring and lending algorithms
7. Practical Approaches for Developing Fair AI
   - Ethical principles in model design
   - Inclusive data collection and bias-aware algorithms
   - "Human-in-the-loop" approaches for fairness evaluation

**Practical Content:**
- Detecting Bias in AI Models: Identifying biases in datasets and algorithms
- Fairness Testing: Using fairness metrics to evaluate AI decisions
- Implementing Bias Mitigation Techniques: Applying correction techniques and evaluating impact
- Case Studies Analysis: Investigating bias incidents in AI in real world
- AI Fairness Auditing: Evaluating and improving ethical compliance in AI systems
- Developing AI Ethics Policies: Formulating guidelines for responsible AI use
- Policy Writing Exercise: Formulating an AI ethics policy for a company or organization

---

#### 📖 Unit 3: Privacy, Security, and Data Protection (12 hours: 6 theory + 6 practical)

**Theoretical Content:**
1. Introduction to Privacy and Security in Data Science
   - Definition and importance of data privacy and security
   - Basic principles of data protection: confidentiality, integrity, availability
   - The role of AI and data science in securing personal data
2. Privacy Legal Regulations and Laws
   - General Data Protection Regulation (GDPR)
   - California Consumer Privacy Act (CCPA)
   - Data Protection Act and other international privacy laws
   - Legal responsibilities for developers and organizations in AI
3. Threats to Data Privacy and Security
   - Data breaches, unauthorized access, and malicious attacks
   - Risks in cloud computing, IoT, and AI systems
   - Privacy concerns in sensitive sectors (healthcare, financial, governmental)
4. Data Protection Strategies and Techniques
   - Encryption techniques and secure data storage
   - Anonymization and pseudonymization of personal data
   - Secure multi-party computation and homomorphic encryption
5. Privacy and Security by Design
   - Building privacy and security into AI systems from the start
   - Privacy Enhancing Technologies (PETs)
   - Implementing secure software development practices (e.g., secure coding, testing)
6. Ethical Implications and Risk Management
   - Balancing privacy with innovation and benefit from AI
   - Ethical dilemmas in data sharing and surveillance
   - Risk assessment, mitigation, and compliance strategies
7. Real-World Applications and Case Studies
   - Privacy breaches in technology companies (e.g., Facebook, Google)
   - Security failures in AI applications (e.g., healthcare, banks)
   - Best practices from organizations that excel in data protection

**Practical Content:**
- Data Encryption: Implementing encryption techniques for data protection
- Anonymization Techniques: Applying anonymization and pseudonymization methods
- Privacy Risk Assessment: Evaluating privacy risks in AI applications
- Security Auditing: Conducting security audits on AI systems
- Compliance Testing: Ensuring AI systems comply with GDPR and other regulations
- Case Study Analysis: Investigating real-world privacy breaches and security failures

---

#### 📖 Unit 4: Interpretability, Transparency, and Accountability (14 hours: 7 theory + 7 practical)

**Theoretical Content:**
1. Introduction to Interpretability in AI
   - Importance, challenges, and difference between interpretability and understandability
2. Explainable AI (XAI) Techniques
   - Local and global interpretations, post-hoc methods (LIME, SHAP)
3. Model Transparency and Interpretability
   - Transparent models (decision trees, linear regression, etc.)
   - Balance between transparency and performance
   - Tools and techniques for interpreting black-box models
4. Legal and Ethical Aspects of Transparency
   - Legal requirements for transparency (GDPR, AI regulations)
   - Ethical responsibility for transparency and user understanding of models
5. Accountability in AI Decision-Making
   - Defining accountability in AI systems
   - Who is responsible for AI decisions? Developers, users, organizations?
   - Mechanisms for determining accountability (auditing, certifications, ethics councils)
6. Case Studies on Interpretability, Transparency, and Accountability
   - Real examples of transparency failures in AI (e.g., biased loan approvals, incorrect medical diagnoses)
   - Impact of transparent AI systems in industries (finance, healthcare, legal systems)
   - Lessons learned from prominent accountability issues in AI
7. Building Accountable AI Systems
   - Designing AI systems with clear accountability frameworks
   - Mechanisms for tracking and auditing decision-making in AI
   - "Human-in-the-loop" approaches to maintain control over AI decisions

**Practical Content:**
- Implementing XAI Techniques: Applying techniques like LIME and SHAP to interpret black-box models
- Evaluating Model Transparency: Evaluating and interpreting AI model transparency using different tools
- Case Studies Analysis: Analyzing success and failure in transparency and accountability in real-world AI
- Building Accountable AI Systems: Designing AI models with clear accountability frameworks and auditing mechanisms
- Ethical Review and Compliance: Conducting ethical review of AI models to ensure transparency and compliance with legal standards

---

#### 📖 Unit 5: AI Governance, Regulations, and Future Challenges (14 hours: 7 theory + 7 practical)

**Theoretical Content:**
1. Introduction to AI Governance
   - Definition and importance of AI governance
   - Key stakeholders in AI governance (governments, organizations, researchers, public)
   - Principles of responsible AI (transparency, fairness, accountability)
2. Regulations and Legal Frameworks for AI
   - Overview of global AI regulations (AI Act in EU, executive orders in US)
   - GDPR and AI: regulations related to privacy and data protection
   - Industry-specific AI regulations (healthcare, finance, self-driving cars)
3. Legal and Ethical Considerations in AI
   - AI and human rights (privacy, freedom, anti-discrimination)
   - Responsibility and accountability in AI decisions
   - Legal frameworks for AI-based decision-making
4. Transparency and Accountability in AI
   - Role of interpretability in AI governance
   - Transparency tools in AI (explainable AI, model auditing)
   - Accountability mechanisms in AI systems (auditing, monitoring)
5. Emerging Challenges in AI Governance
   - Ethical challenges in AI deployment (bias, fairness, security)
   - Regulatory challenges: global standards vs local regulations
   - The role of AI in vital sectors (healthcare, justice, finance)
6. Future Trends and Opportunities in AI Governance
   - AI governance in the age of autonomous systems
   - Future of AI regulation: international cooperation and evolving standards
   - Impact of AI governance on innovation and societal well-being
7. Case Studies in AI Regulation and Governance
   - Case Study 1: AI Act in EU and its impacts
   - Case Study 2: Privacy and data protection in AI (GDPR and beyond)
   - Case Study 3: AI in self-driving cars and regulatory challenges

**Practical Content:**
- AI Governance Frameworks: Analyzing and comparing different AI governance models
- Regulatory Compliance Auditing: Evaluating AI systems to ensure compliance with global regulations (GDPR, AI Act in EU)
- Transparency and Interpretability Tools: Implementing and testing interpretability techniques like LIME and SHAP
- Case Studies Evaluation: Evaluating regulatory challenges and AI in real world
- Accountability Practices in AI: Developing and simulating monitoring systems for AI decisions
- Predictive Analysis for Future Challenges: Identifying and predicting upcoming challenges in AI regulation

---

# 🎓 SEMESTER 2 - COURSES

---

## 📘 COURSE 7: AIAT 121 - Natural Language Processing
**معالجة اللغة الطبيعية**

| Info | Details |
|------|---------|
| Credit Hours | 3 |
| Lecture Hours | 2/week |
| Practical Hours | 2/week |
| Total Training Hours | 64 (32 theory + 32 practical) |

### Course Learning Outcomes (CLOs)
1. **CLO1**: Understand NLP fundamentals and challenges
2. **CLO2**: Apply text preprocessing techniques
3. **CLO3**: Implement text representation methods (BoW, TF-IDF, Word2Vec, BERT)
4. **CLO4**: Build text classification models
5. **CLO5**: Implement Named Entity Recognition (NER) and POS tagging
6. **CLO6**: Apply topic modeling techniques
7. **CLO7**: Build deep learning models for NLP (RNN, LSTM, Transformers)
8. **CLO8**: Implement text summarization and chatbots
9. **CLO9**: Understand ethical considerations in NLP
10. **CLO10**: Apply transfer learning with pre-trained models

### Unit Structure

#### 📖 Unit 1: Introduction to Natural Language Processing (12 hours: 6 theory + 6 practical)

**Theoretical Content:**
1. NLP Fundamentals
   - Definition and meaning of NLP
   - Historical evolution of NLP
   - Challenges in NLP (ambiguity, context understanding, etc.)
2. NLP Applications
   - Chatbots and virtual assistants
   - Machine translation (Google Translate, DeepL)
   - Sentiment analysis in social media and reviews
   - Speech recognition and text-to-speech
   - Information retrieval (search engines)
3. NLP Tools and Libraries
   - Overview of NLTK, spaCy, and Gensim
   - Introduction to Hugging Face Transformers
   - Differences between rule-based and ML-based approaches in learning
4. Basic Text Processing
   - Tokenization (word and sentence tokenization)
   - Stop word removal
   - Stemming vs Lemmatization
   - Regular expressions (Regex) for text processing

**Practical Content:**
- Implementing basic text processing techniques using NLTK and spaCy
- Performing tokenization, stemming, and lemmatization on sample datasets
- Writing a simple text conversion script using Python
- Exploring and analyzing real datasets like movie reviews or news articles

---

#### 📖 Unit 2: Text Representation and Feature Engineering (12 hours: 6 theory + 6 practical)

**Theoretical Content:**
1. Word-Based Text Representations
   - One-Hot Encoding
   - Bag of Words (BoW)
   - TF-IDF (Term Frequency-Inverse Document Frequency)
2. Word Embeddings
   - Word2Vec (CBOW vs Skip-gram)
   - GloVe (Global Vectors for Word Representation)
   - FastText (character-level representations)
3. Contextual Embeddings
   - ELMo (Embeddings from Language Models)
   - BERT (Bidirectional Encoder Representations from Transformers)
   - GPT (Generative Pre-trained Transformer)
4. Dimensionality Reduction Techniques
   - PCA (Principal Component Analysis)
   - t-SNE (t-distributed Stochastic Neighbor Embedding)
   - UMAP (Uniform Manifold Approximation and Projection)

**Practical Content:**
- Converting text to numerical representations using TF-IDF and Word2Vec
- Training and representing word embeddings using Word2Vec from Gensim
- Implementing BERT embeddings using Hugging Face Transformers
- Applying dimensionality reduction on high-dimensional vectors and visualizing results

---

#### 📖 Unit 3: Machine Learning for NLP (12 hours: 6 theory + 6 practical)

**Theoretical Content:**
1. Text Classification
   - Sentiment analysis
   - Spam detection (email, SMS)
   - Intent recognition in chatbots
2. Named Entity Recognition (NER) and Part-of-Speech (POS) Tagging
   - Rule-based vs ML-based NER
   - POS tagging using Hidden Markov Models (HMM)
   - Dependency parsing
3. Topic Modeling
   - Latent Dirichlet Allocation (LDA)
   - Non-negative Matrix Factorization (NMF)
4. Model Evaluation Metrics
   - Precision, Recall, and F1-score
   - Confusion matrix
   - ROC curve and AUC score

**Practical Content:**
- Training a spam detection model using Naive Bayes and Scikit-learn
- Building a sentiment analysis model for customer reviews using logistic regression
- Implementing NER and POS tagging using spaCy
- Applying topic modeling (LDA, NMF) on news article datasets

---

#### 📖 Unit 4: Deep Learning for NLP (14 hours: 7 theory + 7 practical)

**Theoretical Content:**
1. Neural Networks for NLP
2. Introduction to Recurrent Neural Networks (RNNs)
3. Long Short-Term Memory (LSTM) Networks
4. Gated Recurrent Units (GRUs)
5. Transformer Models
6. Attention Mechanism
7. Introduction to Transformer Architecture
8. Overview of BERT, GPT, and T5 models
9. Sequence-to-Sequence Models
10. Encoder-Decoder Architectures
11. Machine Translation Models (e.g., Google Neural Machine Translation)
12. Transfer Learning in NLP
13. Fine-tuning Pre-trained Models
14. Zero-shot and Few-shot Learning

**Practical Content:**
- Building an LSTM-based text classifier using TensorFlow/Keras
- Fine-tuning BERT model for text classification using Hugging Face Transformers
- Implementing machine translation model using seq2seq with attention mechanisms
- Experimenting with GPT-3/GPT-4 for text generation using OpenAI API

---

#### 📖 Unit 5: NLP Applications and Ethics Standards (14 hours: 7 theory + 7 practical)

**Theoretical Content:**
1. Text Summarization
   - Extractive vs Generative summarization
   - Applications in news aggregation
2. Building Conversational AI and Chatbots
   - Rule-based chatbots vs AI-powered chatbots
   - Intent discovery and response generation
3. Ethical Considerations in NLP
   - Bias in language models
   - Fake news and misinformation detection
   - Privacy concerns in text data
4. Future Trends in NLP and AI
   - Developments in multimodal NLP
   - Interpretable AI in NLP
   - Processing low-resource languages

**Practical Content:**
- Building an LSTM-based text classifier using TensorFlow/Keras
- Fine-tuning BERT model for text classification using Hugging Face Transformers
- Implementing text summarization
- Building a simple chatbot

---

## 📘 COURSE 8: AIAT 122 - Deep Learning
**التعلم العميق**

| Info | Details |
|------|---------|
| Credit Hours | 3 |
| Lecture Hours | 2/week |
| Practical Hours | 2/week |
| Total Training Hours | 64 (32 theory + 32 practical) |

### Course Learning Outcomes (CLOs)
1. **CLO1**: Understand deep neural network architectures and their components
2. **CLO2**: Implement CNNs for computer vision tasks including image classification and object detection
3. **CLO3**: Build RNN/LSTM/GRU models for sequential data and NLP applications
4. **CLO4**: Apply transfer learning and fine-tuning with pre-trained models
5. **CLO5**: Implement regularization, optimization techniques, and deploy deep learning models

### Unit Structure

#### 📖 Unit 1: Introduction to Deep Learning and Neural Networks (12 hours: 6 theory + 6 practical)

**Theoretical Content:**
1. Deep Learning Fundamentals
   - Difference between machine learning and deep learning
   - Deep learning applications (healthcare, finance, NLP, etc.)
2. Artificial Neural Networks (ANNs)
   - Biological inspiration for neural networks
   - Perceptron structure and Multi-Layer Perceptrons (MLPs)
   - Activation functions (ReLU, Sigmoid, Tanh, Softmax)
3. Training Neural Networks
   - Forward propagation and loss calculation
   - Backpropagation and gradient descent optimization
   - Optimization algorithms (SGD, Adam, RMSprop)
4. Deep Learning Frameworks
   - Introduction to TensorFlow and PyTorch
   - Setting up deep learning environment (Google Colab, Jupyter Notebook)

**Practical Content:**
- Deep learning fundamentals compared to traditional ML
- Neural network structure and operation
- Activation functions and optimization algorithms
- Forward and backward propagation
- Setting up TensorFlow and PyTorch
- Implementing basic perceptron and MLP
- Training a neural network on simple dataset (e.g., MNIST handwritten digits)

---

#### 📖 Unit 2: Convolutional Neural Networks (CNNs) for Computer Vision (12 hours: 6 theory + 6 practical)

**Theoretical Content:**
1. Image Processing Fundamentals
   - Understanding images as data (pixels, channels, RGB, grayscale)
   - Image transformations (rescaling, normalization, augmentation)
2. CNN Architecture
   - Convolutional layers and feature maps
   - Pooling layers (max pooling, average pooling)
   - Fully connected layers
3. Famous CNN Architectures
   - LeNet, AlexNet, VGG, ResNet, Inception
   - Comparison between different architectures
4. Advanced CNN Applications
   - Object detection (YOLO, SSD, Faster R-CNN)
   - Image segmentation (U-Net, Mask R-CNN)
5. Building CNNs with TensorFlow and PyTorch
   - Writing and training CNN models
   - Model performance evaluation (confusion matrix, ROC, AUC)

**Practical Content:**
- Image processing fundamentals and feature extraction
- CNN architecture: convolutional layers, pooling layers, fully connected layers
- Introduction to pre-trained CNN architectures (ResNet, VGG, Inception)
- Implementing a CNN from scratch using TensorFlow/PyTorch
- Training a CNN on image datasets (e.g., CIFAR-10, ImageNet)
- Transfer learning using a pre-trained model for object detection

---

#### 📖 Unit 3: Recurrent Neural Networks (RNNs) and Transformers for Sequential Data (12 hours: 6 theory + 6 practical)

**Theoretical Content:**
1. Understanding Sequential Data
   - Temporal, audio, and textual data
   - Difference between feedforward networks and recurrent networks
2. Recurrent Neural Networks (RNNs)
   - How RNNs work
   - Challenges: vanishing and exploding gradients
3. LSTM and GRU Networks
   - Structure and benefits of LSTM and GRU
   - Applications in text generation and speech recognition
4. Attention Mechanism and Transformers
   - Introduction to attention mechanism
   - Transformer architecture (self-attention, multi-head attention)
   - BERT and GPT and their applications in NLP
5. NLP Models
   - Sentiment analysis and text classification
   - Machine translation using Seq2Seq models

**Practical Content:**
- Understanding sequential data and time series prediction
- RNN structure and challenges (vanishing gradients problem)
- Advanced architectures: LSTM, GRU, Transformers, attention mechanism
- Applications in NLP
- Implementing RNN, LSTM, and GRU for text generation
- Using Transformer models like BERT and GPT for NLP tasks
- Performing sentiment analysis, machine translation, and speech recognition

---

#### 📖 Unit 4: Advanced Deep Learning Techniques (14 hours: 7 theory + 7 practical)

**Theoretical Content:**
1. Generative Adversarial Networks (GANs)
   - How generator and discriminator networks work
   - GAN applications: image generation, Deepfakes, style transfer
2. Autoencoders and Variational Autoencoders (VAEs)
   - Applications: image compression, anomaly detection
3. Reinforcement Learning Fundamentals
   - Understanding reward-based learning
   - Deep Q-Networks (DQN) and policy gradient methods
4. Transfer Learning
   - How to use pre-trained models (VGG, ResNet, BERT)
   - Fine-tuning for domain-specific applications
5. Ethical Considerations in Deep Learning
   - Bias and fairness in AI models
   - Interpretability and explainability of deep learning models

**Practical Content:**
- GANs and Autoencoders (VAEs)
- Reinforcement learning fundamentals (Deep Q-Networks, policy gradients)
- Transfer learning and fine-tuning models
- Ethical concerns in AI (bias, fairness, interpretability)
- Building and training GANs for image generation
- Implementing a VAE (Variational Autoencoder) for anomaly detection
- Fine-tuning a pre-trained model (e.g., using BERT for text classification)
- Exploring reinforcement learning using OpenAI Gym

---

#### 📖 Unit 5: Model Optimization and Deployment (14 hours: 7 theory + 7 practical)

**Theoretical Content:**
1. Regularization and Hyperparameter Tuning
   - Techniques like Dropout, Batch Normalization, L1/L2 Regularization
   - Optimizing learning rates and batch sizes
2. Model Compression and Efficiency
   - Pruning techniques
   - Quantization for lightweight models on edge devices
3. Deploying Deep Learning Models
   - Exporting models in TensorFlow SavedModel and ONNX formats
   - Serving models using Flask, FastAPI, TensorFlow Serving
   - Cloud deployment on Google Cloud, AWS, and Azure
4. Running Deep Learning on Mobile Devices
   - TensorFlow Lite for mobile deployment
5. End-to-End Deep Learning Project
   - Building a complete deep learning pipeline: model selection, training, evaluation, and deployment

**Practical Content:**
- Regularization and hyperparameter tuning
- Regularization techniques (Dropout, Batch Normalization)
- Model compression for edge devices
- Cloud deployment of deep learning models
- Optimizing deep learning models using regularization
- Deploying models using Flask, FastAPI, and TensorFlow Serving
- Running models on cloud platforms (Google Cloud, AWS)
- Implementing deep learning on mobile devices (TensorFlow Lite, ONNX)

---

## 📘 COURSE 9: AIAT 123 - Reinforcement Learning
**التعلم المعزز**

| Info | Details |
|------|---------|
| Credit Hours | 3 |
| Lecture Hours | 2/week |
| Practical Hours | 4/week |
| Total Training Hours | 80 (32 theory + 48 practical) |

### Course Learning Outcomes (CLOs)
1. **CLO1**: Understand RL fundamentals and MDPs
2. **CLO2**: Implement value-based methods (Q-learning, SARSA)
3. **CLO3**: Apply policy gradient methods
4. **CLO4**: Implement Deep RL algorithms (DQN, A2C, PPO)
5. **CLO5**: Apply exploration-exploitation strategies
6. **CLO6**: Build RL agents for practical applications

### Unit Structure

#### 📖 Unit 1: Introduction to Reinforcement Learning (18 hours: 6 theory + 12 practical)

**Theoretical Content:**
1. Introduction to Reinforcement Learning
   - Difference between supervised, unsupervised, and reinforcement learning
   - Learning through trial and error
   - Real-world applications: robotics, healthcare, gaming, finance
2. Basic Concepts
   - Agent, environment, reward system, action, state, policy
   - Value function and discount factor for long-term rewards
3. Markov Decision Processes (MDPs)
   - Components: states, actions, transitions, rewards
   - Bellman equation and value iteration
4. Exploration vs Exploitation
   - Balancing strategies: Epsilon-Greedy, UCB, Thompson Sampling
5. Applications
   - Robotics, self-driving cars, healthcare, finance, recommendation systems
6. Setting Up RL Problems
   - Defining state and action spaces, designing reward functions
   - Discrete vs continuous environments, fully vs partially observable environments

**Practical Content:**
- Setting up RL environment: installing OpenAI Gym and using Python-based frameworks for RL
- Implementing MDPs: solving simple MDPs using Value Iteration and Policy Iteration algorithms
- Exploration strategies: programming Epsilon-Greedy strategy and visualizing its impact
- Solving RL problems: defining states, actions, and rewards, running RL simulations
- Mini projects: applying RL in games like CartPole and FrozenLake, implementing Q-learning and DQN

---

#### 📖 Unit 2: Prediction and Control without a Model (19 hours: 6 theory + 13 practical)

**Theoretical Content:**
1. Dynamic Programming (DP)
   - Bellman equations for prediction and control
   - Value iteration vs policy iteration
   - Limitations of DP in large state spaces
2. Monte Carlo Methods
   - Prediction using Monte Carlo (estimating value functions)
   - Control using Monte Carlo (exploring starts, soft-epsilon policies)
   - First-visit vs every-visit Monte Carlo
3. Temporal Difference (TD) Learning
   - TD(0) and n-step TD methods
   - Difference between TD and Monte Carlo
4. Q-Learning
   - Q-table and update rules
   - Off-policy learning
   - Convergence properties
5. SARSA (State-Action-Reward-State-Action)
   - On-policy approach to learning
   - Difference between SARSA and Q-learning
   - Implementing SARSA in real-world problems
6. Policy Iteration and Value Iteration
   - Bellman optimality equation in policy iteration
   - Computational efficiency and trade-offs

**Practical Content:**
- Implementing Monte Carlo methods for estimating value functions
- Applying Q-learning and SARSA in OpenAI Gym (CartPole, FrozenLake)
- Using Python to update Q-tables and display agent learning progress
- Running TD(0) and n-step TD algorithms in simple RL environments
- Comparing policy iteration vs value iteration through code-based experiments

---

#### 📖 Unit 3: Deep Reinforcement Learning (19 hours: 6 theory + 13 practical)

**Theoretical Content:**
1. Introduction to Deep RL
   - What is Deep Reinforcement Learning (DRL)?
   - Why Deep RL?
2. Deep Q-Learning (DQN)
   - Overview of Q-learning
   - DQN architecture
   - Experience replay and target networks
   - DQN applications
3. Policy Gradient Methods
   - Introduction to policy gradient methods
   - REINFORCE algorithm
   - Challenges and improvements
4. Actor-Critic Methods
   - Actor-Critic structure
   - Advantage Actor-Critic (A2C)
   - Proximal Policy Optimization (PPO)
5. DDPG (Deep Deterministic Policy Gradient)
   - Overview of DDPG
   - DDPG architecture
   - DDPG exploration
6. Deep RL Applications
   - Games and simulation
   - Robotics
   - Self-driving cars
   - Healthcare and optimization
7. Challenges in Deep RL
   - Exploration vs exploitation dilemma
   - Sample efficiency
   - Stability and convergence
   - Generalization and overfitting

**Practical Content:**
- Implementing Deep RL: starting with simple algorithms like DQN and progressing to advanced algorithms like Actor-Critic, DDPG in environments like OpenAI Gym
- Training and evaluation: monitoring learning curves, rewards, and stability to evaluate model performance
- Optimization: experimenting with techniques like experience replay, reward shaping, and hyperparameter tuning to improve learning efficiency
- Applications: applying Deep RL in games, robotics, and optimization tasks in simulation environments
- Handling challenges: working on exploration vs exploitation problems, stability, and experimenting with techniques like intrinsic motivation and curriculum learning

---

#### 📖 Unit 4: Exploration and Exploitation Strategies (14 hours: 7 theory + 7 practical)

**Theoretical Content:**
1. Introduction to Exploration and Exploitation
   - Definition and importance in RL
   - Balancing exploration and exploitation
2. Exploration Strategies
   - Epsilon-Greedy: random action selection
   - Boltzmann Exploration: action selection based on temperature
   - Thompson Sampling: Bayesian approach for action selection
   - Intrinsic Motivation: curiosity-driven exploration
   - Random Network Distillation: exploration through novelty search
3. Exploitation Strategies
   - Greedy action selection: choosing best action
   - Deterministic policies: exploiting known information
4. Balancing Exploration and Exploitation
   - The dilemma: exploration vs exploitation
   - Trade-off strategies in RL
   - Exploration decay (epsilon decay)
5. Adaptive Exploration Strategies
   - UCB (Upper Confidence Bound): balancing exploration and exploitation based on confidence intervals
   - Bayesian Optimization: exploration based on model uncertainty

**Practical Content:**
- Implementing various exploration strategies
- Comparing performance of different exploration methods
- Tuning exploration parameters

---

#### 📖 Unit 5: Advanced Topics and Applications (10 hours: 7 theory + 3 practical)

**Theoretical Content:**
1. Multi-Agent RL
   - Cooperative and competitive settings
   - Communication between agents
2. Hierarchical RL
   - Options framework
   - Goal-conditioned RL
3. Model-Based RL
   - Learning world models
   - Planning with learned models
4. Real-World Applications
   - Robotics and control
   - Game playing (AlphaGo, Atari)
   - Resource optimization

**Practical Content:**
- Implementing multi-agent RL environments and training cooperative/competitive agents
- Experimenting with hierarchical RL using options framework
- Building model-based RL systems with learned world models
- Applying RL in practical scenarios: robotics simulations, game playing, resource optimization
- Comparing model-based vs model-free approaches
- Implementing goal-conditioned RL for complex tasks

---

## 📘 COURSE 10: AIAT 124 - Generative AI
**الذكاء الاصطناعي التوليدي**

| Info | Details |
|------|---------|
| Credit Hours | 3 |
| Lecture Hours | 2/week |
| Practical Hours | 2/week |
| Total Training Hours | 64 (32 theory + 32 practical) |

### Course Learning Outcomes (CLOs)
1. **CLO1**: Understand generative model architectures (GANs, VAEs, Diffusion)
2. **CLO2**: Implement text generation using Transformers
3. **CLO3**: Apply image generation techniques
4. **CLO4**: Build audio and music generation systems
5. **CLO5**: Understand ethical implications of generative AI
6. **CLO6**: Evaluate generative models using appropriate metrics
7. **CLO7**: Apply generative AI in practical applications

### Unit Structure

#### 📖 Unit 1: Foundations of Generative AI (12 hours: 6 theory + 6 practical)

**Theoretical Content:**
1. Introduction to Generative Models
   - Discriminative vs Generative models
   - Types of generative models
2. Deep Learning Foundations for Generative AI
   - Overview of deep learning and neural networks
   - Supervised vs unsupervised learning for generative tasks
   - Deep learning applications in generative AI
3. Variational Autoencoders (VAEs)
   - Autoencoder architecture
   - Variational Autoencoders (VAEs)
   - Latent space representations
   - Applications of VAEs in text and image generation
4. Generative Adversarial Networks (GANs)
   - GAN architecture (generator vs discriminator)
   - Training dynamics and challenges
   - Common GAN variants (DCGAN, StyleGAN, WGAN, WGAN-GP)
   - Loss functions: Kullback-Leibler divergence and adversarial loss
   - Model performance evaluation metrics
5. Training and Evaluation of Generative Models
   - Evaluation metrics: perplexity, BLEU, FID (Fréchet Inception Distance)
   - Training techniques for model stability
   - Regularization and optimization methods

**Practical Content:**
- Building and training a simple GAN using TensorFlow/PyTorch
- Implementing a VAE (Variational Autoencoder) for image generation
- Comparing different generative model architectures (GANs vs VAEs)
- Experimenting with training techniques like gradient penalties and spectral normalization
- Evaluating generative models using metrics like FID and BLEU scores
- Generating samples from trained generative models
- Exploring latent spaces and interpolation in VAEs

---

#### 📖 Unit 2: Text and Language Generation (12 hours: 6 theory + 6 practical)

**Theoretical Content:**
1. Language Models for Text Generation
   - N-gram models and their limitations
   - Neural language models
   - Recurrent Neural Networks (RNNs) for text generation
2. Transformer-based Generation
   - GPT architecture and self-attention mechanism
   - Text generation techniques (autoregressive generation)
   - Beam search and sampling strategies
3. Advanced Language Models
   - GPT models (GPT-2, GPT-3, GPT-4)
   - BERT and encoder-decoder models
   - Text-to-text generation with T5
4. Prompt Engineering
   - Effective prompting strategies
   - Few-shot and zero-shot learning
   - Controlling generation with prompts
5. Applications of Text Generation
   - Conversational AI and chatbots
   - Content creation and summarization
   - Code generation and programming assistance

**Practical Content:**
- Implementing text generation using GPT models
- Fine-tuning language models for specific tasks
- Practicing prompt engineering with OpenAI API or Hugging Face Transformers
- Building a text-to-text generation system using Transformers
- Generating creative text (stories, poems) using language models
- Implementing conversational AI or chatbot using generative models
- Evaluating text generation quality using metrics like BLEU and perplexity

---

#### 📖 Unit 3: Image and Visual Generation (12 hours: 6 theory + 6 practical)

**Theoretical Content:**
1. Image Generation Techniques
   - GANs for image synthesis
   - StyleGAN and variants
2. Diffusion Models
   - Denoising diffusion probabilistic models
   - DALL-E and Stable Diffusion
3. Image-to-Image Translation
   - Pix2Pix and CycleGAN
   - Style transfer

**Practical Content:**
- Generating AI-created images using StyleGAN, DALL-E, or Stable Diffusion
- Experimenting with Deepfake techniques
- Audio and voice synthesis using AI tools like WaveNet or Jukebox
- Creating AI-generated music and human voice synthesis
- Applying models like OpenAI Codex or GitHub Copilot for code generation
- Automating code generation and software development tasks
- Developing comprehensive projects integrating generative AI in real-world applications like marketing, healthcare, or gaming
- Reviewing AI-generated outputs for accuracy, fairness, and potential biases

---

#### 📖 Unit 4: Ethical and Regulatory Considerations (14 hours: 7 theory + 7 practical)

**Theoretical Content:**
1. Bias and Fairness in Generative AI
   - Sources of bias in training data and model outputs
   - Algorithmic fairness and methods to mitigate bias
   - Ethical concerns in AI-generated content (stereotypes, discrimination)
2. Deepfakes and Misinformation
   - Emergence of deepfake technology and its impact on society
   - Recognizing AI-generated misinformation and mitigation
   - Legal and ethical considerations for AI-generated media
3. Intellectual Property Rights
   - Ownership of AI-generated content
   - Challenges in copyright registration for AI-generated works
   - Legal issues and emerging policies regarding AI creativity
4. Regulatory Frameworks for Generative AI
   - Overview of AI regulations in different countries
   - GDPR, AI Act, and relevant global policies
   - Compliance requirements for AI developers and organizations
5. Responsible AI Development and Governance
   - Ethical principles for AI (transparency, explainability, accountability)
   - Role of AI ethics boards and decision-making bodies
   - Industry best practices for ethical AI use
6. Future Ethical and Regulatory Challenges in AI
   - Evolving landscape of AI governance
   - Handling ethical dilemmas in real-world AI deployment
   - Predicting future trends and regulatory challenges

**Practical Content:**
- Implementing techniques for detecting and mitigating bias in generative models
- Experimenting with deepfake creation and using tools to detect AI-generated content
- Discussing real-world cases related to AI-generated content and intellectual property rights
- Applying AI regulatory guidelines (like GDPR) to ensure compliance in model development
- Building ethical AI models with principles like fairness and transparency
- Participating in discussions on ethical issues in AI development and use

---

#### 📖 Unit 5: Future Trends and Research in Generative AI (14 hours: 7 theory + 7 practical)

**Theoretical Content:**
1. New Developments in Generative Models
   - Advances in GANs (StyleGAN3, BigGAN)
   - VAE models and VAE-GAN models
   - Diffusion models (like DALL-E, Imagen, Stable Diffusion)
   - Transformers for text and image generation
2. Multimodal Generative AI
   - Introduction to CLIP and text-to-image models
   - Generating images, text, and audio from different inputs
   - Challenges and opportunities in multimodal AI
   - Multi-input generative systems
3. Applications in Creative Industries
   - AI in digital art and design (DeepDream, RunwayML)
   - AI-generated music and audio (Jukebox, MuseNet)
   - AI for video creation and game design
   - Creative applications in various artistic domains
4. Scientific and Practical Applications
   - Protein structure prediction (AlphaFold)
   - Medical imaging and diagnosis
   - Research data generation
   - Applications in humanities, social sciences, and visual arts
5. Legal and Ethical Challenges
   - Copyright and ownership of AI-generated content
   - Deepfake and misinformation issues
   - Bias and fairness in generative models
   - Regulatory frameworks and future AI governance
6. Research and Future Trends
   - Enhancing stability and efficiency in generative models
   - Overcoming computational challenges in large models
   - Future of generative AI in various industries

**Practical Content:**
- Experimenting with advanced generative models (StyleGAN, Stable Diffusion, DALL-E)
- Building multimodal applications that generate content from multiple inputs
- Generating creative content (images, text, audio) for artistic projects
- Implementing scientific applications using generative AI (e.g., data augmentation for research)
- Evaluating model quality and ethics: testing for bias, fairness, and accuracy in generated content
- Building a comprehensive project integrating generative AI in real-world applications (marketing, healthcare, or gaming)
- Reviewing AI-generated outputs for accuracy, fairness, and potential biases

---

## 📘 COURSE 11: AIAT 125 - Deploying AI Models
**نشر نماذج الذكاء الاصطناعي**

| Info | Details |
|------|---------|
| Credit Hours | 3 |
| Lecture Hours | 2/week |
| Practical Hours | 4/week |
| Total Training Hours | 80 (32 theory + 48 practical) |

### Course Learning Outcomes (CLOs)
1. **CLO1**: Understand AI model deployment lifecycle
2. **CLO2**: Package and serialize models for deployment
3. **CLO3**: Build APIs for model serving
4. **CLO4**: Deploy models on cloud platforms
5. **CLO5**: Implement containerization with Docker and Kubernetes
6. **CLO6**: Monitor and maintain deployed models

### Unit Structure

#### 📖 Unit 1: Introduction to AI Model Deployment (18 hours: 6 theory + 12 practical)

**Theoretical Content:**
1. AI Model Deployment Lifecycle
   - Key stages: development, testing, deployment, monitoring
   - Importance of deployment in real-world applications
   - Feedback loop: monitoring and retraining
2. Deployment Environments
   - Cloud deployment vs local deployment
   - Benefits of cloud platforms (AWS, GCP, Azure)
   - Infrastructure considerations
3. Key Challenges in Model Deployment
   - Managing model performance and scalability
   - Ethical considerations and methods to mitigate bias
   - Security, versioning, and retrieval
4. Model Packaging
   - Serialization formats (Pickle, ONNX, PMML, SavedModel)
   - Tools for packaging AI models
   - Best practices for saving and loading AI models
5. Deployment Tools and Frameworks
   - API interfaces (Flask, FastAPI, TensorFlow Serving)
   - Introduction to containers (Docker)
   - Basic orchestration using Kubernetes

**Practical Content:**
- Preparing AI model for deployment: training and saving a model using TensorFlow or PyTorch
- Building API interface for AI models: implementing a simple API using Flask or FastAPI to serve predictions
- Containerizing AI model: using Docker to package a trained model for scalable deployment
- Deploying model on cloud: hosting a model on AWS, Google Cloud, or Azure
- Model validation and testing: running unit tests and performance evaluations before deployment
- Monitoring and updating deployed models: implementing logs, feedback loops, and retraining strategies

---

#### 📖 Unit 2: Model Packaging and Serving (19 hours: 6 theory + 13 practical)

**Theoretical Content:**
1. Model Packaging and Data Serialization
   - Importance of model packaging for deployment
   - Common serialization formats: Pickle, ONNX, PMML, SavedModel (TensorFlow)
   - Best practices for saving and loading AI models
2. Containerized Packaging Using Containers
   - Introduction to Docker and its role in AI model deployment
   - Creating Docker images for AI models
   - Managing dependencies and environment configurations
3. Building APIs for Model Serving
   - Overview of REST and gRPC APIs
   - Implementing APIs using Flask and FastAPI
   - Exposing model inference through API endpoints
4. Model Serving Frameworks
   - Introduction to TensorFlow Serving, TorchServe, and MLflow
   - Deploying models using ready-made serving solutions
   - Optimizing performance for high-throughput extraction
5. Batch vs Real-time Inference
   - Understanding batch processing vs real-time model serving
   - Optimizing response time and resource usage
   - Implementing streaming inference using Kafka or RabbitMQ
6. Scaling and Managing Model Serving
   - Load balancing and auto-scaling strategies
   - Using Kubernetes for model deployment and scaling
   - Monitoring model performance in production

**Practical Content:**
- Saving and loading AI model using Pickle, ONNX, or SavedModel for TensorFlow
- Containerizing AI model using Docker: creating Docker image for trained AI model and running it as a container
- Building REST API for model serving: implementing a simple API using Flask or FastAPI to serve predictions
- Deploying using TensorFlow Serving or TorchServe: using ready-made frameworks for optimal model inference
- Testing batch vs real-time inference: running batch processing scripts and deploying real-time API for comparison
- Scaling model deployment using Kubernetes: deploying container-based AI model on Kubernetes cluster for load balancing and scalability

---

#### 📖 Unit 3: Cloud Deployment and Infrastructure (19 hours: 6 theory + 13 practical)

**Theoretical Content:**
1. Introduction to Cloud Computing for AI Deployment
   - Benefits of cloud deployment (scalability, cost-effectiveness, flexibility)
   - Public, private, and hybrid cloud models
   - Basic cloud service models: IaaS, PaaS, SaaS
2. Major Cloud Platforms for AI Deployment
   - AWS SageMaker, Lambda, EC2
   - GCP Vertex AI, AI Platform, Cloud Run
   - Microsoft Azure ML, Azure Functions, AKS
3. Containers and Orchestration
   - Containers: packaging AI models using Docker
   - Orchestration: Kubernetes for managing scalable deployment
   - Serverless computing vs container-based deployment
4. Model Deployment Strategies on Cloud
   - Batch inference vs real-time inference
   - Deploying REST API using FastAPI/Flask
   - Edge AI deployment with cloud integration
5. Performance Optimization, Compliance, and Security
   - Data security and compliance in cloud AI deployment
   - Performance optimization: auto-scaling, load balancing, caching
   - Logging, monitoring, and model versioning on cloud

**Practical Content:**
- Deploying model on AWS, GCP, or Azure: hosting an AI model on a cloud platform and testing its functionality
- Creating REST API for AI model inference: using Flask or FastAPI to serve predictions through an endpoint
- Containerizing AI model using Docker: packaging AI model into a container and deploying it on cloud-based container
- Managing AI model deployment using Kubernetes: running and scaling a deployed model using Kubernetes
- Implementing security measures: applying authentication, encryption, and access control in cloud AI services
- Monitoring and logging deployed models on cloud: setting up logging, tracking API usage, and handling model updates

---

#### 📖 Unit 4: Containers and Orchestration (14 hours: 7 theory + 7 practical)

**Theoretical Content:**
1. Introduction to Containers
   - What are containers?
   - Benefits of using containers in AI model deployment
   - Comparison between containers and virtual machines
   - Overview of Docker and its role in packaging AI models
2. Working with Docker for AI Model Deployment
   - Docker basics: images, containers, Dockerfile
   - Creating Docker images for ML models
   - Running and managing containers
   - Best practices for containerizing AI models
3. Introduction to Kubernetes
   - What is Kubernetes and why use it?
   - Kubernetes architecture: pods, nodes, clusters
   - Deploying AI models on Kubernetes
4. Kubernetes for Scaling AI Deployments
   - Horizontal and vertical scaling
   - Load balancing in Kubernetes
   - Auto-scaling based on demand
5. CI/CD for AI Model Deployment
   - Introduction to CI/CD pipelines
   - Automating model deployment with GitHub Actions, Jenkins
   - Versioning and rollback strategies

**Practical Content:**
- Building and running Docker containers for AI models
- Creating Kubernetes deployments
- Setting up CI/CD pipelines

---

#### 📖 Unit 5: Monitoring, Maintenance, and MLOps (10 hours: 7 theory + 3 practical)

**Theoretical Content:**
1. Model Monitoring
   - Tracking model performance in production
   - Detecting model drift
   - Alerting and logging
2. MLOps Best Practices
   - Experiment tracking
   - Model versioning
   - Reproducibility
3. Model Maintenance
   - Retraining strategies
   - A/B testing
   - Canary deployments

**Practical Content:**
- Setting up model monitoring and performance tracking systems
- Implementing drift detection algorithms
- Using experiment tracking tools (MLflow, Weights & Biases)
- Implementing model versioning and reproducibility practices
- Setting up retraining pipelines
- Performing A/B testing for model comparison
- Implementing canary deployment strategies

---

## 📘 COURSE 12: AIAT 126 - Graduation Project
**مشروع التخرج**

| Info | Details |
|------|---------|
| Credit Hours | 3 |
| Lecture Hours | 1/week |
| Practical Hours | 6/week |
| Total Training Hours | 112 (16 theory + 96 practical) |

### Course Learning Outcomes (CLOs)
1. **CLO1**: Define and scope an AI project
2. **CLO2**: Apply research methodology
3. **CLO3**: Implement end-to-end AI solution
4. **CLO4**: Evaluate and document project results
5. **CLO5**: Present and defend project work

### Unit Structure

#### 📖 Unit 1: Project Planning and Proposal (14 hours: 3 theory + 11 practical)

**Theoretical Content:**
1. Identifying Project Scope and Objectives
   - Defining clear project goals and research questions
   - Scoping AI projects: scope definition and feasibility analysis
   - Identifying target problems and use cases
   - Stakeholder analysis and requirement gathering
2. Literature Review and Background Research
   - Conducting comprehensive literature reviews
   - Identifying relevant research papers and methodologies
   - Understanding state-of-the-art approaches
   - Gap analysis: identifying opportunities for contribution
3. Writing Project Proposal
   - Project proposal structure and components
   - Technical approach and methodology
   - Timeline and resource planning
   - Risk assessment and mitigation strategies
4. Defining Success Metrics
   - Identifying appropriate evaluation metrics for different AI tasks
   - Defining project success criteria
   - Establishing baseline performance targets

**Practical Content:**
- Selecting and defining a graduation project topic
- Conducting literature review and compiling relevant research papers
- Writing a comprehensive project proposal document
- Creating project timeline and resource allocation plan
- Defining success metrics and evaluation criteria for the project
- Presenting project proposal to advisors/peers for feedback

---

#### 📖 Unit 2: Data Collection and Preparation (21 hours: 3 theory + 18 practical)

**Theoretical Content:**
1. Data Sourcing Strategies
   - Identifying relevant data sources (public datasets, APIs, web scraping)
   - Data acquisition methods and legal considerations
   - Data collection planning and protocols
   - Ethical considerations in data collection
2. Data Cleaning and Preprocessing
   - Handling missing data and outliers
   - Data normalization and standardization
   - Addressing data quality issues
   - Data validation and verification
3. Feature Engineering
   - Feature selection and extraction
   - Creating meaningful features from raw data
   - Feature transformation and scaling
   - Domain-specific feature engineering techniques
4. Data Validation
   - Data quality assessment
   - Splitting data into train/validation/test sets
   - Ensuring data representativeness and bias detection

**Practical Content:**
- Collecting and acquiring datasets for the graduation project
- Performing data cleaning and preprocessing using Python libraries (Pandas, NumPy)
- Implementing feature engineering techniques
- Validating data quality and preparing train/validation/test splits
- Documenting data collection and preprocessing procedures
- Creating data exploration notebooks with visualizations

---

#### 📖 Unit 3: Model Development and Training (28 hours: 3 theory + 25 practical)

**Theoretical Content:**
1. Model Selection and Architecture Design
   - Choosing appropriate algorithms for the problem type
   - Designing neural network architectures (if applicable)
   - Understanding model complexity vs performance trade-offs
   - Selecting pre-trained models and transfer learning opportunities
2. Training and Validation
   - Setting up training pipelines
   - Implementing proper validation strategies
   - Monitoring training progress and metrics
   - Handling overfitting and underfitting
3. Hyperparameter Optimization
   - Understanding hyperparameters and their impact
   - Grid search, random search, and Bayesian optimization
   - Cross-validation for hyperparameter tuning
   - Automated hyperparameter optimization tools
4. Performance Evaluation
   - Selecting appropriate evaluation metrics
   - Implementing evaluation pipelines
   - Analyzing model performance and failure cases
   - Comparing model variants and iterations

**Practical Content:**
- Implementing model architecture and training pipeline
- Training models with different hyperparameter configurations
- Performing hyperparameter optimization using grid search or automated tools
- Evaluating model performance using appropriate metrics
- Analyzing model outputs and identifying areas for improvement
- Iteratively refining the model based on validation results
- Documenting training procedures and results

#### 📖 Unit 4: Evaluation and Optimization (28 hours: 3 theory + 25 practical)

**Theoretical Content:**
- Understanding evaluation metrics for different AI tasks
- Techniques for model optimization and fine-tuning
- Addressing overfitting and underfitting
- Comparative analysis with baseline models

**Practical Content:**
- Conducting experiments and collecting performance metrics
- Comparing results with baseline or standard models
- Analyzing failure cases and identifying weaknesses in the model
- Visualizing results using graphs, confusion matrices, or heat maps
- Iteratively improving model parameters or retraining with improved data

---

#### 📖 Unit 5: Project Documentation and Final Presentation (21 hours: 4 theory + 17 practical)

**Theoretical Content:**
- Technical writing standards and report structure
- Effective data visualization and storytelling with AI results
- Public speaking principles and presentation design

**Practical Content:**
- Writing final project report (including summary, methodology, results, discussion)
- Designing slide decks or posters for presentation
- Preparing recorded video or live demonstration of project
- Practicing oral presentation or defense of project
- Compiling source code, documents, and final submission package

---

# 📊 SUMMARY STATISTICS

| Metric | Value |
|--------|-------|
| Total Courses | 12 |
| Total CLOs | 75 |
| Total Credit Hours | 41 |
| Total Training Hours | 944 |
| Semester 1 Courses | 6 |
| Semester 2 Courses | 6 |

---

## 📚 References (from PDF)

1. Artificial Intelligence: A Modern Approach, 4th edition - Pearson (2021)
2. Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow, 3rd Edition - Aurélien Géron (2022)
3. Machine Learning and Data Science: Fundamentals, Concepts, Algorithms, and Tools - Dr. Mohammed Al-Qasim (2022)
4. Artificial Intelligence and Expert Systems in Libraries - Zain Abdel-Hadi (2020)
5. Python for Data Analysis - Wes McKinney (2022)
6. Python Data Science Handbook - Jake VanderPlas (2023)
7. Probabilistic Machine Learning: An Introduction - Kevin P. Murphy (2022)
8. Mathematics for Machine Learning - Deisenroth, Faisal, Ong (2020)
9. Linear Algebra for Everyone - Gilbert Strang (2020)
10. Machine Learning Engineering - Andriy Burkov (2020)
11. Introducing MLOps - Treveil & Mané (2020)
12. Machine Learning Design Patterns - O'Reilly (2020)
13. Practical MLOps - O'Reilly (2023)
14. Engineering MLOps - Zhou (2023)

---

*Document extracted from: دبلوم مشارك الذكاء الاصطناعي (اكاديمية طويق للتدريب)*
*Total Pages: 101*
*Extraction Date: January 2026*

