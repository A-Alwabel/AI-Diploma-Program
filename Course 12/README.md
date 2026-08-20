# AIAT 126 - Graduation Project

The final course of the AI Diploma. You plan, design, build, evaluate, document, and present one complete AI project of your own, applying what you learned across the program.

**New here? Read [START_HERE.md](START_HERE.md) first.**

---

## Course Facts

- **Course code:** AIAT 126
- **Course name:** Graduation Project
- Credit hours: 3 · Contact hours: 5/week · Total training hours: 80 (theory+practical)

## Prerequisites

- Semester 1 (AIAT 111-116)
- Semester 2 (AIAT 121-125)

---

## Units

| Unit | Official title | Folder | Hours (theory + practical) |
|------|----------------|--------|----------------------------|
| 1 | Project Proposal and Plan | [unit1-project-planning/](unit1-project-planning/README.md) | 14 (4 + 10) |
| 2 | Solution System Design and Architecture | [unit2-system-design-architecture/](unit2-system-design-architecture/README.md) | 15 (3 + 12) |
| 3 | Implementation and Development of the Project Idea | [unit3-model-development/](unit3-model-development/README.md) | 17 (3 + 14) |
| 4 | Evaluation and Refinement | [unit4-evaluation-optimization/](unit4-evaluation-optimization/README.md) | 17 (3 + 14) |
| 5 | Project Documentation and Final Presentation | [unit5-documentation-presentation/](unit5-documentation-presentation/README.md) | 17 (3 + 14) |

Note: the Unit 2 lesson notebook is currently a placeholder that outlines the planned content; see the Unit 2 README.

---

## Learning Path

Follow one numbered path. In each unit: read the unit README, work through the example notebooks in file order, do the exercise (Units 1-3), then take the unit quiz.

1. [START_HERE.md](START_HERE.md)
2. [Unit 1: Project Proposal and Plan](unit1-project-planning/README.md) → [Quiz 1](QUIZZES/quiz_01.md)
3. [Unit 2: Solution System Design and Architecture](unit2-system-design-architecture/README.md) → [Quiz 2](QUIZZES/quiz_02.md)
4. [Unit 3: Implementation and Development of the Project Idea](unit3-model-development/README.md) → [Quiz 3](QUIZZES/quiz_03.md)
5. [Unit 4: Evaluation and Refinement](unit4-evaluation-optimization/README.md) → [Quiz 4](QUIZZES/quiz_04.md)
6. [Unit 5: Project Documentation and Final Presentation](unit5-documentation-presentation/README.md) → [Quiz 5](QUIZZES/quiz_05.md)
7. [ASSESSMENTS](ASSESSMENTS/README.md) - final project evaluation

Track your progress in [STUDENT_PROGRESS_CHECKLIST.md](STUDENT_PROGRESS_CHECKLIST.md).

---

## Setup

Use the shared environment at the repository root:

```bash
cd ..            # repo root
source .venv/bin/activate
jupyter lab
```

Open notebooks with the **ai-diploma** Jupyter kernel.

---

## Your Project

- **Requirements and deliverables:** [PROJECT_GUIDELINES.md](PROJECT_GUIDELINES.md)
- **Templates (for students):** [TEMPLATES/](TEMPLATES/) - proposal, report, and presentation templates
- **Workspace:** [PROJECTS/](PROJECTS/README.md)

**Deliverables:** project proposal, progress reports, working system with source code, final project report, and a presentation with demo.

**Success criteria:** the project solves a real problem, applies multiple AI techniques from the program, includes complete documentation, and is presented clearly with a working demo.

---

## Course Structure

```
Course 12/
├── README.md
├── START_HERE.md
├── STUDENT_PROGRESS_CHECKLIST.md
├── PROJECT_GUIDELINES.md
├── TEMPLATES/                          # 3 project templates (for students)
│   ├── project_proposal_template.md
│   ├── project_report_template.md
│   └── presentation_template.md
├── unit1-project-planning/             # Unit 1: Project Proposal and Plan
│   ├── README.md
│   ├── examples/
│   └── exercises/
├── unit2-system-design-architecture/   # Unit 2: Solution System Design and Architecture
│   ├── README.md
│   ├── examples/
│   └── exercises/
├── unit3-model-development/            # Unit 3: Implementation and Development
│   ├── README.md
│   ├── examples/
│   └── exercises/
├── unit4-evaluation-optimization/      # Unit 4: Evaluation and Refinement
│   ├── README.md
│   └── examples/
├── unit5-documentation-presentation/   # Unit 5: Documentation and Final Presentation
│   ├── README.md
│   └── examples/
├── QUIZZES/                            # quiz_01.md ... quiz_05.md
├── ASSESSMENTS/                        # Final_Exam.md (project evaluation)
├── PROJECTS/                           # project workspace
└── CASE_STUDIES/                       # worked case study
```
