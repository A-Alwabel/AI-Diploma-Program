# Quiz 3: Privacy, Security, and Data Protection

**Time Limit:** 30 minutes | **Marks:** 30 points

---

## Part 1: Multiple Choice (10 points)

### Question 1 (2 points)
What is differential privacy?
- A) Complete data anonymization
- B) A technique that adds noise to protect individual privacy while preserving statistical properties
- C) Data encryption
- D) Data deletion

---

### Question 2 (2 points)
What is the main principle of GDPR?
- A) Companies can use data freely
- B) Individuals have rights over their personal data
- C) Data should be public
- D) No data protection needed

---

### Question 3 (2 points)
What is pseudonymization?
- A) Complete data removal
- B) Replacing identifying information with pseudonyms
- C) Data encryption
- D) Data aggregation

---

### Question 4 (2 points)
What is homomorphic encryption?
- A) Encryption that allows computation on encrypted data
- B) Simple data encryption
- C) Data anonymization
- D) Data deletion

---

### Question 5 (2 points)
What is a privacy-preserving technology?
- A) Technology that completely removes data
- B) Technology that protects individual privacy while allowing useful analysis
- C) Technology that makes data public
- D) Technology that ignores privacy

---

## Part 2: Short Answer (10 points)

### Question 6 (5 points)
Explain the key principles of GDPR and how they apply to AI systems.

**Key GDPR Principles:**

1. **Lawfulness, Fairness, and Transparency:**
   - AI systems must have legal basis for processing
   - Clear about how data is used
   - Fair treatment of individuals

2. **Purpose Limitation:**
   - Data collected for specific, legitimate purposes
   - Cannot use for other purposes without consent
   - AI models should align with stated purpose

3. **Data Minimization:**
   - Collect only necessary data
   - AI should use minimal data required for function
   - Avoid collecting excessive features

4. **Accuracy:**
   - Keep data accurate and up-to-date
   - AI systems should handle data quality issues
   - Regular updates and corrections

5. **Storage Limitation:**
   - Keep data only as long as necessary
   - Delete data when purpose is fulfilled
   - AI models should not retain unnecessary data

6. **Integrity and Confidentiality:**
   - Protect data from unauthorized access
   - Secure AI systems and data storage
   - Encryption and access controls

7. **Accountability:**
   - Organizations responsible for compliance
   - Document AI system decisions
   - Regular audits and assessments

**AI Applications:**
- Explainable AI for transparency
- Privacy-preserving ML techniques
- Data protection by design
- Regular privacy impact assessments

---

### Question 7 (5 points)
Describe three privacy-preserving technologies used in AI/ML.

**1. Differential Privacy:**
- Adds calibrated noise to data/queries
- Protects individual privacy while preserving statistical properties
- Use: Aggregated statistics, ML training
- Example: Apple's privacy-preserving analytics

**2. Federated Learning:**
- Train models without centralizing data
- Models trained locally, only updates shared
- Use: Sensitive data (healthcare, finance)
- Example: Google's Gboard predictions

**3. Homomorphic Encryption:**
- Perform computations on encrypted data
- Results remain encrypted until decryption
- Use: Cloud ML, sensitive computations
- Example: Encrypted model training

**4. Secure Multi-Party Computation (SMPC):**
- Multiple parties compute function without revealing inputs
- Each party sees only their input and final output
- Use: Collaborative ML without data sharing
- Example: Joint model training across organizations

**5. Synthetic Data Generation:**
- Generate artificial data with similar statistical properties
- No real individual data exposed
- Use: Testing, development, sharing
- Example: GANs for synthetic datasets

---

## Part 3: Case Analysis (10 points)

### Question 8 (5 points)
A healthcare AI system needs to train on patient data while protecting privacy. What strategies would you recommend?

**Recommended Strategies:**

1. **Data Minimization:**
   - Collect only necessary features
   - Remove direct identifiers (names, SSNs)
   - Use minimum dataset size needed

2. **Anonymization/Pseudonymization:**
   - Replace identifiers with pseudonyms
   - Remove or generalize quasi-identifiers
   - K-anonymity, l-diversity techniques

3. **Differential Privacy:**
   - Add noise to training data or queries
   - Ensure individual records cannot be identified
   - Balance privacy and utility

4. **Federated Learning:**
   - Train models at hospitals locally
   - Share only model updates, not raw data
   - Aggregate updates centrally

5. **Secure Infrastructure:**
   - Encrypt data at rest and in transit
   - Access controls and audit logs
   - Secure computing environments

6. **Compliance:**
   - HIPAA compliance (healthcare regulations)
   - GDPR compliance if applicable
   - Regular privacy impact assessments

7. **Transparency:**
   - Clear consent processes
   - Explainable AI for medical decisions
   - Patient rights to access/correction

---

### Question 9 (5 points)
What are the main security threats to AI systems? How can they be mitigated?

**Main Security Threats:**

1. **Adversarial Attacks:**
   - Malicious inputs designed to fool models
   - Example: Slightly modified images misclassified
   - Mitigation: Adversarial training, input validation, robust models

2. **Model Poisoning:**
   - Attackers inject malicious data during training
   - Corrupts model behavior
   - Mitigation: Data validation, secure training pipelines, anomaly detection

3. **Model Extraction:**
   - Attackers query model to reconstruct it
   - Steals intellectual property
   - Mitigation: Rate limiting, query monitoring, model watermarking

4. **Membership Inference:**
   - Determine if specific data was in training set
   - Privacy breach
   - Mitigation: Differential privacy, regularization, secure training

5. **Data Breaches:**
   - Unauthorized access to training data
   - Privacy violations
   - Mitigation: Encryption, access controls, secure storage

6. **Inference Attacks:**
   - Extract sensitive information from model outputs
   - Privacy leakage
   - Mitigation: Output filtering, differential privacy, secure inference

**General Mitigation Strategies:**
- Defense in depth (multiple security layers)
- Regular security audits
- Secure development lifecycle
- Employee training
- Incident response plans

---

## Grading Rubric

- **90-100% (27-30 points):** Excellent understanding
- **80-89% (24-26 points):** Good understanding
- **70-79% (21-23 points):** Satisfactory
- **60-69% (18-20 points):** Needs improvement
- **Below 60% (<18 points):** Requires additional study