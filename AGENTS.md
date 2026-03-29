## Learned User Preferences

- When they ask for environment or tooling setup (e.g. venv, Jupyter kernel), they expect the agent to perform it, not only list instructions.
- Student-facing repo changes must not ship solutions; new exercises, stubs, and guides should stay aligned with existing unit examples and materials.
- For course and notebook quality, they want systematic, topic-by-topic checks—including running notebooks or cells when feasible—not vague claims of completeness.
- They care how the curriculum feels to learners: explicit theory→practice links, unambiguous ordering, and support when specific notebooks are hard to follow.
- When fixes or improvements are identified, the user expects them to be applied directly to the files—not just documented in markdown reports.
- After completing a set of changes, the user expects a git commit and push to GitHub without needing to ask separately; "push changes" is a routine final step.

## Learned Workspace Facts

- The AI Diploma materials are organized as `Course NN/` trees with units, examples, exercises, quizzes, and projects.
- Course 08 documents tell students to follow notebook file order (01 → 02 → 03 …); slide numbers are treated as topic labels, not the sequence to follow.
- Filenames matching `*INSTRUCTOR*` are gitignored and are not assumed to exist on the student-facing remote.
- Student-oriented clarity and gap notes live under `DOCS/` (e.g. ordering, when a notebook is unclear, theory→practice gaps).
- The workspace uses a `.venv` at the repo root (Python 3.13, Homebrew); the registered Jupyter kernel is named "ai-diploma" / "Python 3.13 (AI Diploma)".
- Course 08 contains two student projects under `unit4-advanced-dl/projects/`: Image Classification and Sequence/Text Generation; PROJECT_GUIDE.md files follow the pattern used in courses 01–06.
- `DOCS/WHEN_A_NOTEBOOK_IS_NOT_CLEAR.md` and `DOCS/GAPS_FOR_STUDENTS.md` are the canonical student-facing support docs for notebook clarity and theory→practice gaps.
