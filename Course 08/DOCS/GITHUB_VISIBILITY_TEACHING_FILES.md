# Course 08 – Teaching files and GitHub visibility

**Short answer:** Teaching files are **not** all hidden by default. It depends on (1) whether the repo is **private** and (2) what `.gitignore` does.

---

## If the repo is "just for you" (private, no students)

- **Private repo:** Only you (and anyone you add as collaborator) can see it. So even if teaching files are committed, they are "hidden" from everyone else. You can keep everything in the repo.
- **No need to change anything** for visibility—just keep the repo private.

---

## If you share the repo with students (public or students as collaborators)

Then you **do** want instructor-only files hidden (not pushed to GitHub). Two options:

### Option A: One repo, instructor-only files ignored (recommended)

- **Course 08** now has a **`Course 08/.gitignore`** that lists instructor-only paths. Those files stay **only on your machine** and are **not** pushed to GitHub. Students who clone the repo will not get:
  - Quiz and exam solutions
  - Exam and case study rubrics
  - Teaching runbooks, scoring docs, and internal checklists

- **You** keep the full set locally (including solutions); **students** get the rest (notebooks, quizzes without answers, exam without solution, project instructions, etc.).

### Option B: Two repos

- **Private repo (you):** Full course including all teaching files.
- **Public or shared repo (students):** Copy of the course **without** the instructor-only paths (e.g. exclude `DOCS/SOLUTIONS/`, solution and rubric files, teaching guides). You can script this or maintain two clones.

---

## What is already ignored by the root `.gitignore` (repo-wide)

- `**/solutions/` and `**/SOLUTION/` → **Course 08/DOCS/SOLUTIONS/** is ignored (quiz and exercise solutions, case study sample solution).
- `*INSTRUCTOR*.md` → **DOCS/INSTRUCTOR_RUNBOOK.md** is ignored.
- `*REVIEW*.md` → e.g. **DOCS/RE_REVIEW_AND_SCORING.md** is ignored.

So **solutions** and **INSTRUCTOR_RUNBOOK** (and some review docs) are already not pushed if the root `.gitignore` is used.

---

## What was still visible before Course 08 `.gitignore`

These were **not** ignored by the root `.gitignore` and would have been pushed:

- **DOCS:** TEACHING_GUIDE.md, TEACHING_TIMING.md, DEMO_RUNBOOK.md, COMMON_MISCONCEPTIONS_AND_FAQ.md, HOW_I_SCORE_COURSE_08.md, FINAL_10_10_CHECKLIST.md, NOTEBOOK_STANDARD.md, CLO_COVERAGE.md
- **ASSESSMENTS:** Final_Exam_Solution.md, Final_Exam_Rubric.md
- **CASE_STUDIES:** case_study_01_rubric.md
- **Reports:** notebook_run_report.*, output_pedagogy_verification_report.*

The **Course 08/.gitignore** added for this course ignores the instructor-only ones listed above (see that file for the exact list). Student-useful docs (e.g. REQUIREMENTS_COURSE_08.md, COLAB_SETUP.md, EXAMPLES_ORDER.md) stay tracked so they are on GitHub for students.

---

## Summary

| Situation | What to do |
|-----------|------------|
| Repo is **private** and only for you | Nothing. Teaching files can stay in the repo; no one else sees it. |
| Repo is **shared with students** (public or collaborators) | Use **Course 08/.gitignore** so instructor-only files are not pushed. You keep them only locally. |

**Bottom line:** Teaching files are hidden on GitHub **only if** (a) the repo is private and only you have access, or (b) you use `.gitignore` (and don’t commit those files) so they never get pushed. The **Course 08/.gitignore** makes (b) easy when you share the repo with students.

**If the repo is only for you (private):** You can **remove or not use** `Course 08/.gitignore` so that all teaching files are committed and backed up on GitHub; no one else can see them if the repo is private.
