# Graduation Project Guidelines
## AIAT 126

---

## 📋 Project Requirements

### 1. Project Selection

**Choose ONE of the following categories:**

#### Category A: Computer Vision
- Medical image analysis
- Object detection system
- Image classification application
- Quality control automation

#### Category B: Natural Language Processing
- Multi-language translation system
- Intelligent document processing
- Conversational AI assistant
- Text summarization system

#### Category C: Predictive Analytics
- Demand forecasting system
- Fraud detection system
- Predictive maintenance
- Recommendation system

#### Category D: Generative AI
- Content generation system
- Image synthesis application
- Creative AI tool
- Data augmentation system

#### Category E: Reinforcement Learning
- Game-playing agent
- Robotics control system
- Resource optimization
- Autonomous decision system

---

## 📝 Project Deliverables

### 1. Project Proposal (end of Unit 1)
**Due:** End of Unit 1

**Must include:**
- Problem statement
- Objectives and goals
- Dataset description (including its licence and any personal data it contains)
- Methodology
- Expected outcomes
- Ethical, legal and social risks you anticipate, and how you plan to handle them
- Timeline
- **Prior Work Inventory** (template section 6) - for each of the five components (dataset,
  model, pipeline, deployment target, ethics review), the AIAT 111-125 artifact you reuse or
  extend, with the course, the unit and a path your instructor can open. At least three
  components must name a real artifact, from at least three different courses.

**Template:** See `TEMPLATES/project_proposal_template.md` (sections 1-9)
**Graded as:** Gate 1 (10 points), of which 1.5 are the Prior Work Inventory

> **Why the inventory is graded.** The official AIAT 126 description requires the project to
> integrate knowledge from multiple AI domains, and CLO2 is "integrate knowledge from the
> different AI subfields into a coherent, practical system". A capstone that starts from a blank
> file has integrated nothing. Naming what you build **on** is the evidence - and it is also a
> plan: a component with a named prior artifact starts from code that already runs.

---

### 2. Design Document (after Unit 2)
**Due:** Before implementation starts

**Must include:**
- Prior Work Inventory, carried forward from proposal section 6 and updated if the design changed
- System architecture diagram
- Data flow between components
- Model, algorithm, dataset and platform choices, each with a justification citing your own data
  type, data size and constraints, plus at least one alternative and why you rejected it
- Data collection and preprocessing plan
- Evaluation metrics and the baselines you must beat
- Input/output formats and where artifacts are stored
- Feasibility check against your timeline and available data

**Taught in:** `unit2-system-design-architecture/examples/01_system_design_architecture.ipynb`.
Part 8 of that lesson generates the twelve-section document for you from your own answers, and
its `check_design()` validator refuses to write a document that still contains `TODO`, names a
model with no justification, states no baseline, or maps fewer than three components to earlier
courses. Run it before you submit: it is the same list your instructor grades from.

**Graded as:** Gate 2 (10 points). **Do not start implementation until this passes** - building
on a design that will fail is the most expensive mistake in this course.

---

### 3. Progress Reports (Bi-weekly)
**Due:** Every 2 weeks

**Must include:**
- Completed tasks
- Current challenges
- Next steps
- Updated timeline

**Graded as:** formative - no points of their own, but they are evidence at Gate 3.

---

### 4. Final Project (implementation and evaluation)
**Due:** End of Unit 4

**Must include:**
- Complete working system
- Source code (well-documented, with `requirements.txt` and setup instructions)
- Trained models (if applicable)
- Deployment (local or cloud)
- User documentation
- Evaluation: metric choice, baseline comparison, failure analysis, limitations

**Graded as:** Gate 3 (30 points, implementation) and Gate 4 (20 points, evaluation)

---

### 5. Project Report (end of Unit 5)
**Due:** End of Unit 5

**Length:** 20-40 pages, using the nine sections taught in Unit 5:

1. Executive summary (1-2 pages)
2. Introduction and problem statement (2-3 pages)
3. Literature review (3-5 pages)
4. Methodology (4-6 pages)
5. Results and analysis (5-8 pages)
6. Discussion - interpretation, limitations, **ethical considerations**, future work (2-3 pages)
7. Conclusion (1-2 pages)
8. References - minimum 15-25 sources (2-3 pages)
9. Appendices (variable)

Submit the separate **ethical considerations document** from the Unit 5 submission checklist
alongside the report.

**Template:** See `TEMPLATES/project_report_template.md`
**Graded as:** Gate 5 (15 points)

---

### 6. Presentation and Defense (defense session)
**Due:** Defense session

**Must include:**
- 15-20 minute presentation
- Live demo of the system (bring a backup recording)
- Q&A session

**Template:** See `TEMPLATES/presentation_template.md`
**Graded as:** Gate 6 (15 points)

---

## ✅ Evaluation Criteria: the six milestone gates

Your course grade is produced by **six milestone gates**, each graded when the corresponding
unit ends. There is no timed written exam in AIAT 126.

| # | Gate | Points | Graded after | What is assessed |
|---|------|-------:|--------------|------------------|
| 1 | Project proposal | 10 | Unit 1 | Problem, scope, dataset, methodology, timeline, and the ethical/legal/social risks you expect |
| 2 | Design review | 10 | Unit 2 | System architecture, data flow, technology choices, feasibility |
| 3 | Implementation | 30 | Unit 3 | Working code, technique selection and justification, code quality, reproducibility |
| 4 | Evaluation | 20 | Unit 4 | Metric choice, baseline comparison, failure analysis, test-set discipline, limitations |
| 5 | Final report | 15 | Unit 5 | The 20-40 page report, including its ethical considerations section |
| 6 | Defense | 15 | Defense session | 15-20 minute presentation, live demo, Q&A |
| | **Total** | **100** | | |

**Pass thresholds:** you must reach 60/100 overall **and** meet the individual threshold on
gates 3 (18/30), 4 (12/20) and 6 (9/15). Gates 1, 2 and 5 pass at 6/10, 6/10 and 9/15. A gate
below its threshold is resubmitted once within the window your instructor sets.

**Gates are gates, not just scores.** Implementation does not start until the design review
passes - this is the rule that saves the most wasted work.

**Ethics is assessed (CLO5).** Ethical, legal and social considerations are graded at gate 1
(the risks you identify in the proposal), gate 5 (the report's Discussion section plus the
ethical considerations document from the Unit 5 submission checklist) and gate 6 (defense
Q&A). They are also the whole of Part 4 of
[ASSESSMENTS/Final_Exam.md](ASSESSMENTS/Final_Exam.md). Treat them as a deliverable, not a
paragraph added at the end.

**Relationship to the final evaluation.** `ASSESSMENTS/Final_Exam.md` scores the *same*
artifacts a second time as a summative review of the finished project, using its own 100-point
breakdown (30/30/20/20). It does not ask for extra work, and it does not replace the gate
totals above.

**Progress reports are formative:** they carry no points of their own, but a missing progress
report costs you under the project-management criterion of gate 3.

---

## 📅 Timeline

Deliverables are tied to **units**, not to fixed calendar weeks: cohorts run this course at
different paces, so your instructor announces the binding dates in session 1. The table below
is the indicative full-length schedule; map it onto your cohort's calendar.

| Unit | Phase | Deliverable | Gate |
|------|-------|-------------|------|
| Unit 1 | Project planning | Proposal | Gate 1 (10) |
| Unit 2 | System design and architecture | Design document | Gate 2 (10) |
| Unit 3 | Data preparation and model development | Working implementation + progress reports | Gate 3 (30) |
| Unit 4 | Evaluation, optimization, deployment | Evaluation results + progress reports | Gate 4 (20) |
| Unit 5 | Documentation and presentation | Final report + submission package | Gate 5 (15) |
| Defense session | Defense | Presentation, live demo, Q&A | Gate 6 (15) |

---

## 🎯 Success Criteria

Your project must demonstrate:
- Application of multiple AI/ML techniques
- Real-world problem solving
- Complete end-to-end system
- Professional code quality
- Clear documentation
- Explicit ethical, legal and social analysis of the system you built (CLO5)

---

**For:** AIAT 126 - Graduation Project