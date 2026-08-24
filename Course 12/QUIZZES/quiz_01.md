# Quiz 01 – Unit 1: Project Proposal and Plan
## AIAT 126 - Graduation Project

**Time Limit:** 45 minutes  
**Total Points:** 110 points (100 required; Q8 application may count as bonus or toward total)  
**Covers:** Unit 1 (defining project scope, measurable objectives and success criteria, the literature-review framework and gap analysis, the 14-week timeline and its milestones).  
**Concepts from:** Unit 1 example 01 (project proposal and literature review: the `project_scope` template, the `literature_review_structure` template, the 14-week `timeline` template) and exercise 01 (writing your own proposal).  
**Answer key:** released by your instructor.

---

## Part 1: Multiple Choice (40 points)

### Question 1 (10 points)
Which of these is a properly stated **success criterion** in the form taught in Unit 1?

a) "The model will use a deep neural network."  
b) "The model will be state of the art in its field."  
c) "Recall > 85% on the validation set, because false negatives are the costly error in this diagnostic setting."  
d) "The model will perform well on medical images."  

---

### Question 2 (10 points)
How many research papers does the Unit 1 **literature-review framework** say you should review?

a) 3–5  
b) 15–25  
c) 40–60  
d) As many as you can find in a single day  

---

### Question 3 (10 points)
In the taught `literature_review_structure`, which field records **what is missing in existing work and how your project will contribute**?

a) `research_papers[].key_findings`  
b) `tools_and_libraries`  
c) `state_of_the_art.performance_baselines`  
d) `state_of_the_art.gap_analysis`  

---

### Question 4 (10 points)
Why does the taught `scope` block require an **`out_of_scope`** list as well as an `in_scope` list?

a) Because naming what you will deliberately *not* build is what keeps the project finishable inside the 14-week plan  
b) Because reviewers require a longer proposal document  
c) Because the out-of-scope items become the literature review  
d) Because that is where the success criteria are recorded  

---

## Part 2: Code Writing (30 points)

### Question 5 (30 points)
Write a `project_scope` dictionary for a project of your choice, using the **seven keys** taught in Unit 1: `project_title`, `problem_statement`, `objectives`, `research_questions`, `scope`, `target_users`, `success_criteria`.

Then write a function `validate_scope(scope)` that returns a list of problems it finds:

- any of the seven keys missing,
- any empty value (empty string, empty list, empty dict),
- any leftover placeholder text (for example `TODO`, `Example:`, `Brief description`),
- a `scope` block that does not contain **both** `in_scope` and `out_of_scope`.

Call the function on your dictionary and print the result.

**Answer key:** released by your instructor.

---

## Part 3: Short Answer (30 points)

### Question 6 (15 points)
Explain why project **objectives must be measurable**. Then rewrite the vague objective *"improve the model's performance"* as a measurable objective in the Unit 1 style, and name the data split your target is set on.

**Answer key:** released by your instructor.

---

### Question 7 (15 points)
Name the **five milestones** of the 14-week timeline taught in Unit 1, in order, with each one's week range and at least one of its deliverables. Then explain why the template attaches a deliverable to every milestone.

**Answer key:** released by your instructor.

---

## Part 4: Application (10 points)

### Question 8 (10 points)
A classmate's proposal states one success criterion: **"accuracy > 90%"**. Their dataset is 95% negative and 5% positive, for a rare medical condition. Explain how a useless system could satisfy that criterion, and rewrite the `success_criteria` block so it cannot be satisfied that way.

**Answer key:** released by your instructor.

---

**Mapping:** CLO1, CLO4; notebooks: `unit1-project-planning/examples/01_project_proposal_literature_review`, `unit1-project-planning/exercises/exercise_01_project_proposal`.

**For:** AIAT 126 - Graduation Project
