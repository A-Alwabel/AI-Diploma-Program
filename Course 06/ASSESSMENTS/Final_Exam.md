# Final Exam: Ethics of Artificial Intelligence
## AIAT 116

**Time Limit:** 2 hours  
**Total Points:** 100 points  
**Instructions:** Answer all questions. Show your work for partial credit.

**Marking scheme:** Part 1 (Q1–Q6): 5 pts each = 30. Part 2 (Q7–Q9): 10 pts each = 30. Part 3 (Q10: 15 pts, Q11: 10 pts) = 25. Part 4 (Q12): 15 pts. **Total: 100.**

---

## Part 1: Multiple Choice (30 points)

Each question has exactly one best answer. Every option describes a position someone has actually held — read all four before choosing.

### Question 1 (5 points)
**CLO2:** A team removes the `Sex` column from a screening model's training data and reports that the system is now fair. On the held-out set the model's positive-prediction rate is **44.3% for women and 31.6% for men** — a demographic parity difference of **0.128**. What does this result show?

A) Removing `Sex` made the model blind to gender, so the remaining gap is not something the model itself produced  
B) Demographic parity is the wrong test here: on the same held-out set the equalized-odds gaps are small (TPR gap 0.047)  
C) The model rebuilt the group split from correlated features like fare and class, so deleting the column changed nothing  
D) The model satisfies demographic parity, since two applicants with identical inputs receive an identical decision from it  

---

### Question 2 (5 points)
**CLO1, CLO2:** Northpointe showed that COMPAS was **calibrated** — a given risk score meant the same re-offence probability for Black and for white defendants. ProPublica showed that the **false-positive rates differed**: 44.9% for Black defendants against 23.5% for white defendants. Which statement best describes this situation?

A) Both are correct: with different base rates, no classifier can be calibrated and have equal error rates at once  
B) Northpointe is right and ProPublica is not: a score that means the same thing for both groups is the fairness that counts  
C) ProPublica measured demographic parity, which is the fairness definition a court would apply to a sentencing tool  
D) Calibrating the scores separately within each group would let both fairness criteria hold at the same time  

---

### Question 3 (5 points)
**CLO3:** In the differential privacy lesson, the Laplace mechanism at **ε = 0.1** produced a mean absolute error of about **10** on a count of **212** patients (4.7% of the answer) and about **10** again on a count of **29** patients (34.2% of the answer). What does this tell you about deploying differential privacy?

A) The Laplace mechanism is unsuitable for small groups, which should be protected using k-anonymity instead of added noise  
B) Lowering ε further would shrink the error on the small subgroup, because ε is the mechanism's accuracy setting  
C) The small subgroup has fewer records to average over, so collecting more data there would close the gap  
D) Laplace noise scales with sensitivity and ε, not with the size of the true answer, so one ε costs small groups more  

---

### Question 4 (5 points)
**CLO4:** A global SHAP chart reports a mean |SHAP| of **0.204** for the feature `is_female`. Computed *within* ticket class, the same quantity is **0.300** in second class and **0.163** in third class. A regulator asks how much the model relies on sex when it decides about **third-class** passengers. What is the correct response?

A) Report 0.204, since it is computed on far more data and is therefore the more reliable estimate  
B) Report 0.163, and state that the global average of 0.204 in fact describes none of the three classes  
C) Report 0.300 from second class, since a regulator should be shown the largest reliance on sex the model has  
D) Report that SHAP explains single predictions, so a per-class average of SHAP values is not a usable figure  

---

### Question 5 (5 points)
**CLO5:** Your company is placing a CV-screening model that ranks job applicants on the EU market. Under the EU AI Act risk tiers taught in Unit 5, what follows?

A) Limited risk: the duty is a transparency notice telling applicants that an AI system is involved in the screening  
B) Prohibited: the Act lists automated decision-making about employment among its Article 5 banned practices  
C) Minimal risk: the system produces a ranking and a human recruiter still takes the final hiring decision  
D) High risk: data governance, logging, human oversight and a conformity assessment apply before deployment  

---

### Question 6 (5 points)
**CLO4:** An audit trail shows **29 decisions** that were automated although written policy required human review below a confidence of 0.70 (the deployed router was configured at 0.60). On those 29 decisions the model was right **62.1%** of the time — its worst band, against **78.9%** overall. Under the accountability framework taught in Unit 4, what does this finding require?

A) A named human role is accountable for the gap, and the audit trail is what made it measurable months later  
B) Accountability rests with the routing algorithm, since it issued all those decisions with no human involved  
C) The band's 62.1% is normal variation around the 78.9% overall accuracy, so the trail shows no problem to fix  
D) Retraining the model on those 29 cases resolves it, because the problem is model accuracy, not process  

---

## Part 2: Short Answer Questions (30 points)

### Question 7 (10 points)
**CLO1:** A hospital wants to deploy a triage model that raises average survival across all patients but systematically deprioritises one demographic group.

Explain the main ethical frameworks used in AI ethics (utilitarianism, deontology, virtue ethics), **apply each one to this decision**, and state where they disagree and why.

---

### Question 8 (10 points)
**CLO2:** Describe bias detection and mitigation techniques in AI systems. Provide examples.

Your answer must also state, with a reason, **why a single fairness metric is not enough** to clear a system.

---

### Question 9 (10 points)
**CLO4:** Explain the importance of transparency and explainability in AI. What methods can be used?

---

## Part 3: Practical/Coding Questions (25 points)

### Question 10 (15 points)
**CLO2:** Implement bias detection for a classification model. Use a **real dataset with a genuine group attribute** (for example the Titanic manifest through the course data loader) — not invented data.

1. Load the data, train a classifier, and obtain predictions alongside ground truth and the group attribute
2. Calculate fairness metrics (demographic parity, equalized odds)
3. Identify bias across different groups
4. Visualize results

---

### Question 11 (10 points)
**CLO4:** Use SHAP or LIME to explain a model's predictions. Show how to interpret the results, and state clearly which parts of your output are **global** and which are **local**.

---

## Part 4: Case Study / Real-World Application (15 points)

### Question 12 (15 points)
**CLO2, CLO3, CLO5:** Analyze an AI hiring system that shows bias against certain demographic groups:
1. Identify the ethical issues
2. Propose bias detection methods
3. Suggest mitigation strategies
4. Design a fairness evaluation framework
5. Consider legal and regulatory compliance

---

**End of Exam**

**Good Luck!**
