# Quiz 02 – Unit 2: Solution System Design and Architecture
## AIAT 126 - Graduation Project

**Time Limit:** 45 minutes  
**Total Points:** 110 points (100 required; Q8 application may count as bonus or toward total)  
**Covers:** Unit 2 (the five questions a system design document answers: components, data flow, model selection with justification and alternatives, data formats and storage, risks and dependencies).  
**Concepts from:** Unit 2 exercise 01 (system design) — its design primer and the worked example design document for a customer-review sentiment web app. The Unit 2 lesson notebook is still a placeholder, so this quiz examines only the primer and worked example.  
**Answer key:** released by your instructor.

---

## Part 1: Multiple Choice (40 points)

### Question 1 (10 points)
The Unit 2 design primer says a capstone system design document answers **five questions**. Which of the following is **not** one of them?

a) What are the components of your system, and what does each one do?  
b) In what order does data move between the components?  
c) What could block you — licences, APIs, compute, imbalanced data — and what do you depend on?  
d) What is the projected annual cloud hosting cost of the system?  

---

### Question 2 (10 points)
In the worked example (a customer-review sentiment web app), what **justification** is recorded for choosing logistic regression on TF-IDF features?

a) "50k short texts; a linear model is strong, fast and interpretable at this scale"  
b) "Logistic regression is the most accurate text classifier available"  
c) "A transformer was unavailable in the environment"  
d) "It is the only classifier scikit-learn provides"  

---

### Question 3 (10 points)
The worked example lists a **75% positive class imbalance** as a risk. What planned response does it record?

a) Report accuracy only, since accuracy is the standard headline metric  
b) Stratified split plus F1 reporting  
c) Delete majority-class rows until the data is 50/50, before splitting  
d) Postpone the project until a balanced dataset can be collected  

---

### Question 4 (10 points)
What does the design document's **`data_flow`** field specify?

a) The folder structure of the project repository  
b) The network bandwidth the deployed system will require  
c) The order in which data moves between the listed components  
d) The hyperparameters used to train the chosen model  

---

## Part 2: Code Writing (30 points)

### Question 5 (30 points)
Write a `my_system_design` dictionary for a project of your choice, filling in all **six keys** used by the worked example: `project_name`, `components`, `data_flow`, `model_selection`, `data_formats_storage`, `risks_dependencies`.

Write each component in the taught `name — what it does` form, and give `model_selection` a `chosen_model`, a `justification`, and at least one entry in `alternatives_considered` stating the reason it was rejected.

Then write `check_design(design)` that returns a list of problems:

- any of the six keys missing or empty,
- any leftover `TODO` text anywhere in the document,
- a `chosen_model` with no justification,
- an empty `alternatives_considered` list.

Call it on your design and print the result.

**Answer key:** released by your instructor.

---

## Part 3: Short Answer (30 points)

### Question 6 (15 points)
Why must the model-selection section name **at least one alternative** and the reason you rejected it? Give at least three distinct reasons, and state what a reviewer can do with that information that a bare model name would not let them do.

**Answer key:** released by your instructor.

---

### Question 7 (15 points)
Describe the purpose of the **risks and dependencies** section of a design document. List the three risks recorded in the worked example, classify each one as legal/ethical, data, or technical, and give the planned response recorded for each.

**Answer key:** released by your instructor.

---

## Part 4: Application (10 points)

### Question 8 (10 points)
A classmate's design document names **"a deep neural network"** as the chosen model, gives the data flow as **"data goes into the model and predictions come out"**, and leaves the risks list empty. State which of the primer's five questions this document fails to answer, then give the single most valuable correction you would ask for at design review, with your reason for ranking it first.

**Answer key:** released by your instructor.

---

**Mapping:** CLO1, CLO2; notebooks: `unit2-system-design-architecture/exercises/exercise_01_system_design`.

**For:** AIAT 126 - Graduation Project
