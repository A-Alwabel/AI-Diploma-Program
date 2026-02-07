# What students see when they clone the repo (Course 08 and repo-wide)

**Short answer:** Students see **everything that is committed and pushed**. Instructor-only files are **hidden** only when they are **not** in the repo (e.g. listed in `.gitignore` so they are never pushed).

---

## Course 08: student-facing vs instructor-only

### What **is** in the repo (students **see** this)

- **README, START_HERE, STUDENT_PROGRESS_CHECKLIST** – course entry and progress.
- **All unit folders** – examples, exercises, unit READMEs (with long-run notes).
- **QUIZZES** – `quiz_01.md` … `quiz_05.md` (questions only; no answers on the page; "Answer Key: See DOCS/SOLUTIONS/...").
- **ASSESSMENTS** – `Final_Exam.md` only (exam questions; no solution or rubric).
- **CASE_STUDIES** – `case_study_01_deep_learning_deployment.md` (scenario only; no rubric file).
- **PROJECTS** – Image Classification and Optional Project 02: READMEs and RUBRICs (rubrics are often given to students so they know how they’re graded).
- **DOCS (student-useful)** – COLAB_SETUP.md, EXAMPLES_ORDER.md, REQUIREMENTS_COURSE_08.md, GITHUB_VISIBILITY_TEACHING_FILES.md, INSTITUTION_SLIDES_COMPATIBILITY.md, PRACTICAL_ENHANCEMENT_ASSESSMENT.md.
- **TEMPLATES, tools/** (under Course 08) – notebook run/verify scripts, TEMPLATES/README.

So for **Course 08**, students see what they **need**: units, quizzes (no answers), exam (no solution), case study (scenario), projects, and the DOCS above.

### What is **not** in the repo (students **do not** see this)

These are listed in **Course 08/.gitignore**, so they are **not** committed/pushed:

- **DOCS/SOLUTIONS/** – all quiz and exercise solutions, case study sample solution.
- **ASSESSMENTS/Final_Exam_Solution.md**, **Final_Exam_Rubric.md**.
- **CASE_STUDIES/case_study_01_rubric.md**.
- **DOCS** (instructor-only): INSTRUCTOR_RUNBOOK, TEACHING_GUIDE, TEACHING_TIMING, DEMO_RUNBOOK, COMMON_MISCONCEPTIONS_AND_FAQ, HOW_I_SCORE, RE_REVIEW_AND_SCORING, FINAL_10_10_CHECKLIST, NOTEBOOK_STANDARD, CLO_COVERAGE.
- **DOCS** (reports): notebook_run_report.*, output_pedagogy_verification_report.*.

So for **Course 08**, only **needed** (student-facing) files are in the repo; instructor-only and reports are hidden.

---

## Repo-wide: artifacts and root tools

These **are** in the repo (we pushed them), so **students see them**:

- **artifacts/** – execution logs, verification JSON, Course 05 executed outputs (e.g. PNG, HTML, pkl, CSV), executed_modified notebooks, etc.
- **tools/** (at repo root) – e.g. analyze_execution_failures.py, re_execute_all_failed.py, re_execute_failed_notebooks.py.

They are **not** required for students to do the courses; they are mainly for instructors/developers. If you want the repo to show **only** what students need, you can add `artifacts/` and `tools/` to the **root** `.gitignore` and stop tracking them (they would then exist only on your machine).

---

## Summary

| Location              | Students see                                      | Hidden (not in repo)                          |
|-----------------------|---------------------------------------------------|-----------------------------------------------|
| **Course 08**         | Units, quizzes (no answers), exam (no solution), case study (scenario), projects, student DOCS | Solutions, exam/case rubrics & solutions, teaching runbooks, scoring docs, run reports |
| **Other courses**     | Whatever is tracked (root .gitignore already excludes many **/solutions/, *INSTRUCTOR*.md, etc.) | Depends on each course’s and root .gitignore |
| **artifacts/, root tools/** | Yes (currently pushed)                            | —                                             |

**Bottom line:** For **Course 08**, only **needed** (student-facing) files appear; instructor-only content is hidden via Course 08/.gitignore. **Repo-wide**, students also see **artifacts/** and root **tools/**; to show only what students need, add those to the root `.gitignore` and remove them from tracking.
