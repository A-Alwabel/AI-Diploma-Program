# Unit 2: Solution System Design and Architecture

Unit hours: 15 total (3 theory + 12 practical)

You design the system that will implement your proposal: overall architecture, data flow, module interconnections, model and algorithm selection with justification, and dataset/preprocessing design.

## Builds on (AIAT 111-125)

**Builds on:** AIAT 114 U1/U3 (preprocessing pipelines, classifiers) · AIAT 115 U5 (production pipelines, big files) · AIAT 125 U2/U5 (serving, monitoring) · AIAT 116 U2 (bias detection, for the risks section) · AIAT 122 U2 / AIAT 121 U3 if your system takes images or text.

Every artifact you reuse goes in **section 6, the Prior Work Inventory**, of [`TEMPLATES/project_proposal_template.md`](../TEMPLATES/project_proposal_template.md) — scored at gate 1 and re-checked at the design review. It is this course's **CLO2** evidence: AIAT 126 integrates the diploma, it does not re-teach it.

## Prerequisites

- Unit 1: Project Proposal and Plan (an approved proposal)

## Examples (work through in order)

> **Tiers:** **CORE** = taught live in class (max 2 per 3-hour session) · **HOMEWORK** = self-study, assigned around the live sessions · **ENRICHMENT** = optional extra, only if time allows.

1. **[CORE]** [examples/01_system_design_architecture.ipynb](examples/01_system_design_architecture.ipynb) - Full lesson: components and lanes, an architecture/data-flow diagram generated from your component list, model/algorithm/dataset/platform selection with justification, a data plan built from a real column profile, evaluation metrics and baselines, I/O formats and storage, scalability and modularity measured rather than asserted, and the design-document deliverable. Worked end to end on the real 1912 Titanic manifest; it writes `design_document_example.md` next to the notebook so you can see the deliverable before you write yours.

## Exercise

- [exercises/exercise_01_system_design.ipynb](exercises/exercise_01_system_design.ipynb) - Produce the system design and architecture for your own project. It carries a compact five-question primer and a worked mini-example; the lesson notebook above is the full treatment, and Part 8 of the lesson has the twelve-section design document with the `check_design()` validator. Solutions are released by your instructor.

## Quiz

- [../QUIZZES/quiz_02.md](../QUIZZES/quiz_02.md)

## Next

[Unit 3: Implementation and Development of the Project Idea](../unit3-model-development/README.md)
