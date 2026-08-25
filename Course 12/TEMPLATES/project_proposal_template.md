# Project Proposal Template
## AIAT 126 - Graduation Project

---

## 1. Project Information

**Project Title:** [Your project title here]  
**Student Name(s):** [Your name(s)]  
**Date:** [Date]  
**Course:** AIAT 126 - Graduation Project

---

## 2. Problem Statement

[Describe the problem you want to solve. Why is it important?]

---

## 3. Objectives

### Primary Objectives:
1. [Objective 1]
2. [Objective 2]
3. [Objective 3]

### Secondary Objectives:
1. [Objective 1]
2. [Objective 2]

---

## 4. Dataset

**Dataset Name:** [Name]  
**Source:** [Where you'll get the data]  
**Size:** [Number of samples, features]  
**Description:** [Brief description]

---

## 5. Methodology

### Approach:
[Describe your approach to solving the problem]

### Technologies:
- [Technology 1]
- [Technology 2]
- [Technology 3]

### Algorithms/Models:
- [Algorithm/Model 1]
- [Algorithm/Model 2]

---

## 6. Prior Work Inventory (AIAT 111-125)

> **Why this section exists.** AIAT 126 is a *graduation* project: the official course
> description requires it to "demonstrate the ability to integrate knowledge from multiple
> domains - machine learning, deep learning, natural language processing, computer vision, data
> science", and **CLO2** is "integrate knowledge from the different AI subfields into a coherent,
> practical system". A capstone that starts from a blank file has integrated nothing. This
> section is where you show what you are building **on**, and it is scored at Gate 1 and
> re-checked at the Gate 2 design review.

For **each component below**, name the AIAT 111-125 artifact you reuse or extend. Give the
course, the unit, and the actual notebook path - not just a course name.

| Component | Course + unit | Artifact (notebook / script / document path) | Reuse or Extend? | What you change or add for this project |
|-----------|---------------|-----------------------------------------------|------------------|------------------------------------------|
| **Dataset** - where the data comes from and how it is loaded | [e.g. AIAT 115 U2] | [e.g. `Course 05/unit2-cleaning/examples/01_data_loading.ipynb`] | [Reuse / Extend / None] | [e.g. same loading and profiling routine, new file] |
| **Model** - the algorithm you train | [e.g. AIAT 114 U3] | [e.g. `Course 04/unit3-classification/examples/01_logistic_regression.ipynb`] | [Reuse / Extend / None] | [what is different here] |
| **Pipeline** - preprocessing, training and tuning code | [e.g. AIAT 114 U1 + AIAT 115 U2] | [e.g. `Course 04/unit1-regression-algorithms/examples/03_data_preprocessing.ipynb`] | [Reuse / Extend / None] | [what is different here] |
| **Deployment target** - how the model is packaged and served | [e.g. AIAT 125 U2] | [e.g. `Course 11/unit2-versioning-serving/examples/02_fastapi_deployment.ipynb`] | [Reuse / Extend / None] | [what is different here] |
| **Ethics review** - your bias, privacy or accountability check | [e.g. AIAT 116 U2] | [e.g. `Course 06/unit2-bias-fairness/examples/01_bias_detection.ipynb`] | [Reuse / Extend / None] | [what is different here] |

**Rules (these are what the rubric scores):**

1. **At least three** of the five components must name a real artifact, drawn from **at least
   three different courses**.
2. "None" is allowed for a component, but only with a written reason on the next line - for
   example, a project with no user-facing service may legitimately have no deployment target.
   "I did not look" is not a reason.
3. Every path must be a file that actually exists in your copy of the diploma repository. Your
   instructor will open them.
4. **Reuse** = you run the earlier code largely as-is on new data. **Extend** = you keep the
   pattern and change something substantive. Say which; they are graded the same, but claiming
   "Extend" and delivering "Reuse" is not.

**Components marked "None", with the reason:**

- [Component]: [why nothing from AIAT 111-125 applies]

### 6.1 AI subfields integrated (CLO2)

Tick every subfield your system actually uses, and name the component that uses it. One tick is
not integration; the official description names several domains for a reason.

- [ ] Machine learning (AIAT 114) - component: [ ]
- [ ] Data science / scalable data handling (AIAT 115) - component: [ ]
- [ ] Deep learning (AIAT 122) - component: [ ]
- [ ] Natural language processing (AIAT 121) - component: [ ]
- [ ] Computer vision (AIAT 122 U2) - component: [ ]
- [ ] Reinforcement learning (AIAT 123) - component: [ ]
- [ ] Generative AI (AIAT 124) - component: [ ]
- [ ] Deployment and monitoring (AIAT 125) - component: [ ]
- [ ] AI ethics (AIAT 116) - component: [ ]

> **Carried forward.** This inventory becomes section 1 of your Unit 2 **design document**, where
> the `check_design()` validator refuses to emit a document that maps fewer than three components
> to AIAT 111-125 artifacts. Fill it in properly once and you have done it for both gates.

---

## 7. Expected Outcomes

[What do you expect to achieve?]

---

## 8. Timeline

| Week | Tasks |
|------|-------|
| 1-2 | [Tasks] |
| 3-4 | [Tasks] |
| 5-6 | [Tasks] |
| 7-8 | [Tasks] |
| 9-10 | [Tasks] |
| 11-12 | [Tasks] |

---

## 9. Resources Needed

- [Resource 1]
- [Resource 2]
- [Resource 3]

---

**For:** AIAT 126 - Graduation Project