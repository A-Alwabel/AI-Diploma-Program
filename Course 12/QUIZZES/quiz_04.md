# Quiz 04 – Unit 4: Evaluation and Refinement
## AIAT 126 - Graduation Project

**Time Limit:** 45 minutes  
**Total Points:** 110 points (100 required; Q8 application may count as bonus or toward total)  
**Covers:** Unit 4 (comparing candidate algorithms on the validation set, confusion matrices and ROC curves, failure-case analysis, one refinement iteration by decision-threshold tuning, and the single final evaluation on the test set).  
**Concepts from:** Unit 4 example 01 (model evaluation and optimization).  
**Note:** Questions 1–4 and 7 refer to the numbers printed by the Unit 4 notebook when you ran it.  
**Answer key:** released by your instructor.

---

## Part 1: Multiple Choice (40 points)

### Question 1 (10 points)
Three algorithms were compared in the Unit 4 notebook. Which one was selected, on which data split, and by which metric?

a) Logistic Regression, on the test set, by accuracy  
b) Random Forest, on the validation set, by F1 (0.9175)  
c) SVM, on the training set, by precision  
d) Random Forest, on the test set, by ROC-AUC  

---

### Question 2 (10 points)
The failure analysis found 16 misclassified validation samples: 5 false positives and 11 false negatives. Which error type dominated, and what does that suggest as a first refinement?

a) False positives dominated, so the decision threshold should be raised  
b) The two counts were effectively equal, so nothing follows from the split  
c) False negatives dominated, so the decision threshold should be raised  
d) False negatives dominated — the model is under-calling the positive class, so lowering the decision threshold is the natural first refinement to test  

---

### Question 3 (10 points)
Threshold tuning found 0.410, raising validation F1 from 0.9175 to 0.9246. The **decision threshold** is best described as:

a) A parameter of the **decision**, tuned on the validation set after the model is trained  
b) A hyperparameter of the random forest, learned during training  
c) A property of the test set  
d) A fixed constant that must always be 0.5  

---

### Question 4 (10 points)
The final test evaluation gave F1 0.9020 against validation F1 0.9246 at the same threshold — a gap of −0.0227. What is the correct action?

a) Re-tune the threshold on the test set until the gap closes  
b) Report the validation number, since it is the higher of the two  
c) Report the test number, note that the gap is small, and stop — the test set is now spent  
d) Re-split the data and repeat until the gap comes out positive  

---

## Part 2: Code Writing (30 points)

### Question 5 (30 points)
Write code that:

1. gets predicted probabilities for the **validation** set from a trained model;
2. sweeps the decision threshold using `precision_recall_curve` and selects the threshold that maximises F1;
3. prints F1 at the default 0.5 threshold, F1 at the tuned threshold, and the change between them;
4. **keeps the tuned threshold only if it improved F1**, and otherwise falls back to 0.5;
5. applies the chosen threshold **once** to the test set and prints the test metrics together with the validation-to-test gap measured at that same threshold.

**Answer key:** released by your instructor.

---

## Part 3: Short Answer (30 points)

### Question 6 (15 points)
Explain the three-way **train / validation / test** split: what each set is for, and why candidate models are compared on the validation set rather than the test set. State precisely what would be wrong with the reported final number if the comparison had been run on the test set instead.

**Answer key:** released by your instructor.

---

### Question 7 (15 points)
Describe what **failure-case analysis** adds beyond an overall error rate. Then interpret the two confidence figures from the Unit 4 run — false positives at an average predicted probability of 0.6960 and false negatives at 0.2464 — and explain what they suggested about how much the threshold refinement could gain.

**Answer key:** released by your instructor.

---

## Part 4: Application (10 points)

### Question 8 (10 points)
In your own capstone the positive class is a rare equipment failure, and missing one costs far more than raising a false alarm. Using the Unit 4 workflow, state which metric you would select the model on, which direction you would move the decision threshold away from 0.5 and why, which split you would tune it on, and what number you would report at the end.

**Answer key:** released by your instructor.

---

**Mapping:** CLO3; notebooks: `unit4-evaluation-optimization/examples/01_model_evaluation_optimization`.

**For:** AIAT 126 - Graduation Project
