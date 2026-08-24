# Quiz 05 – Unit 5: NLP Applications and Ethics Standards
## AIAT 121 - Natural Language Processing

**Time Limit:** 45 minutes  
**Total Points:** 110 points (100 required; Q8 application may count as bonus or toward total)  
**Covers:** Unit 5 (types of bias in NLP, the logic of a bias audit, association gaps, mitigation strategies, the responsible-NLP checklist).  
**Concepts from:** Unit 5 example 01 (bias detection) and exercise 01 (NLP applications and ethics audit).  
**Answer key:** released by your instructor.

---

## Part 1: Multiple Choice (40 points)

### Question 1 (10 points)
Which of the following is an example of **gender bias** in an NLP model?

a) The model runs slower on longer documents  
b) The model strongly associates professions with genders (e.g. "nurse" with female, "engineer" with male)  
c) The model has a large vocabulary  
d) The model was trained on English text  

---

### Question 2 (10 points)
The Unit 5 notebook explicitly disclosed that its association scores were **simulated**. In a *real* bias audit, where would those scores come from?

a) They would be invented by the auditor to make the report interesting  
b) They would be copied from another company's audit  
c) They would be measured from the system itself — e.g. cosine similarities in trained embeddings, or model outputs on controlled test inputs  
d) Real audits do not use numbers  

---

### Question 3 (10 points)
Which of these is a **valid bias-mitigation strategy** taught in Unit 5?

a) Ensure diverse, balanced representation in the training data  
b) Delete the test set so bias cannot be measured  
c) Keep known biases undocumented so users do not worry  
d) Audit the model once at launch and never again  

---

### Question 4 (10 points)
You build pairs of test sentences that are **identical except for one demographic word** (e.g. "he"/"she", or a male/female name) and compare the model's outputs on each pair. What does this test measure?

a) The model's vocabulary size  
b) The model's training speed  
c) The model's accuracy on the original training data  
d) Whether the model's output changes when only the demographic attribute changes — a direct probe of bias  

---

## Part 2: Code Writing (30 points)

### Question 5 (30 points)
Write code that reproduces the bias-audit table logic from Unit 5. Starting from:

```python
associations = {
    "doctor":   (0.70, 0.30),
    "nurse":    (0.20, 0.80),
    "engineer": (0.80, 0.20),
    "teacher":  (0.40, 0.60),
    "pilot":    (0.90, 0.10),
}   # (male_score, female_score)
```

1. For each profession, compute the association gap `abs(male_score - female_score)`.
2. Classify the bias level using the unit's thresholds: `"High"` if the gap is greater than 0.5, `"Moderate"` if greater than 0.3, otherwise `"Low"`.
3. Print one table row per profession: profession, male score, female score, bias level.

**Answer key:** released by your instructor.

---

## Part 3: Short Answer (30 points)

### Question 6 (15 points)
Describe **two different routes** by which bias can enter an NLP system, and give a concrete example of each (e.g. what could go wrong in the data, the embeddings, or the evaluation).

**Answer key:** released by your instructor.

---

### Question 7 (15 points)
Name **three items** from the responsible-NLP checklist taught in Unit 5, and explain in one sentence each why the item matters in a deployed system.

**Answer key:** released by your instructor.

---

## Part 4: Application (10 points)

### Question 8 (10 points)
Your deployed sentiment model scores otherwise-identical reviews **lower when they contain female names**. Design a response plan: (1) how you would measure the problem precisely, (2) one mitigation you would apply, and (3) how you would verify the mitigation worked. Ground each step in the Unit 5 material.

**Answer key:** released by your instructor.

---

**Mapping:** CLO7, CLO10; notebooks: `unit5-applications-ethics/examples/01_bias_detection`, `unit5-applications-ethics/exercises/01_nlp_applications_ethics_exercise`.

**For:** AIAT 121 - Natural Language Processing
