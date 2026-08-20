# AIAT 116 — Artificial Intelligence Ethics

Course 06 of the AI Diploma. This course covers the ethical dimensions of building and deploying AI systems: ethical frameworks, bias and fairness, privacy and data protection, interpretability and accountability, and AI governance and regulation.

**Course code:** AIAT 116
**Course title:** Artificial Intelligence Ethics
Credit hours: 3 · Contact hours: 4/week · Total training hours: 64 (theory+practical)

New students: read [START_HERE.md](START_HERE.md) first.

---

## Units

| Unit | Official title | Folder | Hours |
|------|----------------|--------|-------|
| 1 | Foundations of AI Ethics | [unit1-ethics-foundations/](unit1-ethics-foundations/README.md) | 12 |
| 2 | Bias, Fairness, and Discrimination in AI | [unit2-bias-fairness/](unit2-bias-fairness/README.md) | 12 |
| 3 | Privacy, Security, and Data Protection | [unit3-privacy-security/](unit3-privacy-security/README.md) | 12 |
| 4 | Interpretability, Transparency, and Accountability | [unit4-transparency-accountability/](unit4-transparency-accountability/README.md) | 14 |
| 5 | AI Governance, Regulations, and Future Challenges | [unit5-governance-regulations/](unit5-governance-regulations/README.md) | 14 |

---

## Learning Path

Follow one numbered path:

1. [START_HERE.md](START_HERE.md) — setup and orientation
2. Units 1 → 5, in order. In each unit: read the unit README, work through `examples/` notebooks in file order, do the `exercises/` notebook(s), then take the unit quiz in [QUIZZES/](QUIZZES/README.md)
3. [ASSESSMENTS/](ASSESSMENTS/README.md) — final exam

Track yourself with [STUDENT_PROGRESS_CHECKLIST.md](STUDENT_PROGRESS_CHECKLIST.md).

---

## Prerequisites

- Earlier Semester 1 courses (AIAT 111–115), in particular basic Python programming and introductory ML concepts.

## Setup

- Use the shared environment at the repository root: the `.venv` virtual environment.
- Open notebooks with the **ai-diploma** Jupyter kernel.

---

## Folder Structure

```
Course 06/
├── README.md                        # This file
├── START_HERE.md                    # Read first
├── STUDENT_PROGRESS_CHECKLIST.md    # Progress tracker
├── unit1-ethics-foundations/        # Unit 1 (examples/ + exercises/)
├── unit2-bias-fairness/             # Unit 2 (examples/ + exercises/)
├── unit3-privacy-security/          # Unit 3 (examples/ + exercises/)
├── unit4-transparency-accountability/  # Unit 4 (examples/ + exercises/)
├── unit5-governance-regulations/    # Unit 5 (examples/ + exercises/)
├── QUIZZES/                         # One quiz per unit
├── ASSESSMENTS/                     # Final exam
├── PROJECTS/                        # Three applied projects
├── CASE_STUDIES/                    # Case study material
└── PRESENTATIONS/SLIDES/            # 14 lecture slide decks
```

---

## Assessment Materials

- **Quizzes:** one per unit in [QUIZZES/](QUIZZES/README.md)
- **Final exam:** [ASSESSMENTS/Final_Exam.md](ASSESSMENTS/Final_Exam.md)
- **Projects:** three applied projects in [PROJECTS/](PROJECTS/README.md)
- **Case study:** [CASE_STUDIES/case_study_01_ai_ethics_in_healthcare.md](CASE_STUDIES/case_study_01_ai_ethics_in_healthcare.md)

Answer keys and exercise solutions are released by your instructor.

---

## Libraries Used

The notebooks use the scientific Python stack (numpy, pandas, scikit-learn, matplotlib, seaborn) plus fairness and explainability libraries: fairlearn (Unit 2), cryptography (Unit 3), shap and lime (Unit 4). All are installed in the repository root `.venv`.
