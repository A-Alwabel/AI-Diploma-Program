# Quiz 4: Transparency and Accountability
## اختبار 4: الشفافية والمساءلة

**Time Limit:** 30 minutes | **Marks:** 30 points

---

## Part 1: Multiple Choice (10 points)

### Question 1 (2 points)
What is Explainable AI (XAI)?
- A) AI that is faster
- B) AI systems that can explain their decisions in understandable terms
- C) AI that uses less data
- D) AI that is cheaper

---

### Question 2 (2 points)
What does SHAP stand for?
- A) Simple Human-AI Protocol
- B) SHapley Additive exPlanations
- C) Secure Human-AI Process
- D) Standard Human-AI Practice

---

### Question 3 (2 points)
What is LIME used for?
- A) Data cleaning
- B) Explaining individual predictions locally
- C) Model training
- D) Data visualization

---

### Question 4 (2 points)
What is algorithmic transparency?
- A) Making algorithms public
- B) Making algorithms understandable and explainable
- C) Making algorithms faster
- D) Making algorithms cheaper

---

### Question 5 (2 points)
What is accountability in AI?
- A) Making models faster
- B) Clear responsibility for AI decisions and outcomes
- C) Using more data
- D) Improving accuracy

---

## Part 2: Short Answer (10 points)

### Question 6 (5 points)
Explain the difference between global and local interpretability. Give examples of techniques for each.

**Global Interpretability:**
- Understanding how the model works overall
- Explains general behavior and patterns
- Shows which features are important globally
- Use: Understanding model behavior, feature importance

**Techniques:**
- Feature importance scores
- Permutation importance
- Partial dependence plots
- Global SHAP values

**Example:** "Age is the most important feature for loan approval decisions across all applicants."

**Local Interpretability:**
- Understanding individual predictions
- Explains why a specific prediction was made
- Shows feature contributions for one instance
- Use: Explaining specific decisions, debugging

**Techniques:**
- LIME (Local Interpretable Model-agnostic Explanations)
- SHAP values for individual predictions
- Counterfactual explanations
- Attention mechanisms (for neural networks)

**Example:** "This loan was rejected because: credit score (40% impact), debt-to-income ratio (35% impact), employment history (25% impact)."

**Trade-off:** Often easier to achieve local than global interpretability, especially for complex models.

---

### Question 7 (5 points)
What are the key components of an accountability framework for AI systems?

**Key Components:**

1. **Clear Responsibility:**
   - Define who is responsible for AI decisions
   - Assign roles (developers, operators, managers)
   - Establish chain of responsibility
   - Example: AI ethics board, responsible AI officer

2. **Documentation:**
   - Document model development process
   - Record data sources and preprocessing
   - Track model versions and changes
   - Maintain decision logs
   - Example: Model cards, data sheets

3. **Audit Trails:**
   - Log all AI decisions and inputs
   - Track model performance over time
   - Record when and why models were updated
   - Enable retrospective analysis
   - Example: Decision logs, performance monitoring

4. **Human Oversight:**
   - Human review for critical decisions
   - Escalation procedures
   - Human-in-the-loop systems
   - Override mechanisms
   - Example: Medical diagnosis review, loan approval oversight

5. **Redress Mechanisms:**
   - Process for challenging AI decisions
   - Appeal procedures
   - Correction mechanisms
   - Compensation for harm
   - Example: Customer service, ombudsman

6. **Transparency:**
   - Explainable AI systems
   - Clear communication about AI use
   - Public disclosure where appropriate
   - Example: Algorithmic impact assessments

7. **Compliance:**
   - Adherence to regulations
   - Regular compliance audits
   - Legal review of AI systems
   - Example: GDPR compliance, industry standards

8. **Continuous Monitoring:**
   - Track model performance
   - Monitor for bias and drift
   - Regular assessments
   - Example: Automated monitoring dashboards

---

## Part 3: Case Analysis (10 points)

### Question 8 (5 points)
A bank uses an AI system for loan approvals. A customer's loan is rejected and they want to know why. How would you design a system to provide transparency and accountability?

**Design Elements:**

1. **Explainability:**
   - Use interpretable models or XAI techniques (SHAP, LIME)
   - Generate explanations for each decision
   - Show feature contributions in plain language
   - Example: "Rejected due to: credit score (650, below threshold), high debt-to-income ratio (45%), short employment history (6 months)"

2. **Transparency:**
   - Clear communication about AI use in loan process
   - Public information about model criteria
   - Algorithmic impact assessment available
   - Example: Website explaining loan criteria

3. **Accountability:**
   - Human loan officer review available
   - Appeal process for rejected applications
   - Clear responsibility (loan officer + AI system)
   - Audit trail of all decisions
   - Example: Customer can request human review

4. **Documentation:**
   - Model card explaining model behavior
   - Data documentation (training data sources)
   - Decision logs for each application
   - Example: Detailed records of all loan decisions

5. **Redress:**
   - Process to challenge decision
   - Ability to provide additional information
   - Correction mechanism if error found
   - Example: Appeal form, additional documentation submission

6. **Monitoring:**
   - Track approval rates by demographics
   - Monitor for bias
   - Regular model audits
   - Example: Monthly fairness reports

---

### Question 9 (5 points)
What are the challenges in achieving transparency and accountability in AI systems? How can they be addressed?

**Challenges:**

1. **Complexity:**
   - Deep learning models are "black boxes"
   - Difficult to understand internal workings
   - **Solution:** Use interpretable models, XAI techniques, model simplification

2. **Trade-offs:**
   - Interpretability vs. accuracy
   - Transparency vs. proprietary information
   - **Solution:** Hybrid approaches, selective transparency, explainability by design

3. **Scalability:**
   - Explaining millions of decisions is expensive
   - Real-time explanations may slow systems
   - **Solution:** Efficient XAI methods, cached explanations, on-demand explanations

4. **Technical Barriers:**
   - Lack of XAI tools and expertise
   - Integration challenges
   - **Solution:** Better tools, training, standardized frameworks

5. **Legal/Regulatory:**
   - Unclear regulations
   - Liability questions
   - **Solution:** Clear regulations, legal frameworks, industry standards

6. **User Understanding:**
   - Technical explanations may confuse users
   - Different users need different explanations
   - **Solution:** Layered explanations, user-friendly formats, education

**Addressing Strategies:**
- **Explainability by Design:** Build interpretability into models from start
- **Regulatory Compliance:** Follow GDPR, AI Act, etc.
- **Industry Standards:** Adopt XAI best practices
- **Education:** Train developers and users
- **Tools:** Develop better XAI tools
- **Hybrid Approaches:** Combine interpretable and complex models

---

## Grading Rubric

- **90-100% (27-30 points):** Excellent understanding
- **80-89% (24-26 points):** Good understanding
- **70-79% (21-23 points):** Satisfactory
- **60-69% (18-20 points):** Needs improvement
- **Below 60% (<18 points):** Requires additional study
