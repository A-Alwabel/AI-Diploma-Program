# Course 09 Full Parity Alignment Checklist

## Goal

Fill the meaningful gaps between the instructor-provided Course 09 materials and the
existing repo course while preserving the repo's stronger student-learning workflow.

## Rules

- [ ] Keep student-facing materials separate from instructor-only solutions.
- [ ] Do not weaken or replace stronger existing repo content.
- [ ] Prefer practical, student-friendly, theory-to-practice examples.
- [ ] Update docs and assessments only where they materially improve learning.

## Phase 1: Final Gap Baseline

- [ ] Reconfirm the final gap list for Unit 3, Unit 4, and Unit 5 against the current repo.
- [ ] Identify the exact files to create for each missing topic.
- [ ] Decide naming conventions that match existing `examples/`, `exercises/`, and `solutions/` patterns.
- [ ] Confirm where instructor-only answer keys should live.

## Phase 2: Unit 3 Deep RL Gap

- [ ] Add a student-facing `DDPG` example notebook in `unit3-deep-rl/examples/`.
- [ ] Make the notebook beginner-friendly with theory, architecture, code, plots, and summary.
- [ ] Add a matching Unit 3 exercise notebook for DDPG.
- [ ] Add an instructor-only DDPG solution notebook.
- [ ] Update `unit3-deep-rl/README.md` if needed so DDPG is clearly represented in the learning flow.
- [ ] Update `QUIZZES/quiz_03.md` to cover DDPG at the correct depth.
- [ ] Update `ASSESSMENTS/Final_Exam.md` only if DDPG needs explicit course-level assessment coverage.

## Phase 3: Unit 4 Exploration Gap

- [ ] Add a student-facing notebook for intrinsic motivation / curiosity-driven exploration.
- [ ] Add a student-facing notebook for Random Network Distillation (`RND`) or a course-appropriate simplified version.
- [ ] Add a student-facing notebook for Bayesian optimization or a clearly scoped approximation suitable for this course.
- [ ] Keep the examples aligned with existing Unit 4 exploration notebooks and avoid unnecessary research-level complexity.
- [ ] Add one exercise notebook that compares multiple exploration methods, including at least one newly added method.
- [ ] Add instructor-only solutions for the new Unit 4 exercise(s).
- [ ] Update `unit4-exploration-exploitation/README.md` only if sequencing or topic wording needs clearer student guidance.
- [ ] Update `QUIZZES/quiz_04.md` to reflect the expanded topic coverage.
- [ ] Update `ASSESSMENTS/Final_Exam.md` only if the new Unit 4 material should appear at exam level.

## Phase 4: Unit 5 Advanced Topics Gap

- [ ] Add a student-facing notebook for meta-learning or few-shot RL at a student-appropriate level.
- [ ] Add a student-facing notebook or written assessment artifact for ethics, fairness, safety, and responsible RL deployment.
- [ ] Ensure the Unit 5 additions fit the existing applications-first structure instead of feeling like unrelated theory inserts.
- [ ] Add one Unit 5 exercise covering the new advanced topic(s).
- [ ] Add instructor-only solution material for the new Unit 5 exercise(s).
- [ ] Update `unit5-applications/README.md` only if sequencing, framing, or topic mapping needs refinement.
- [ ] Update `QUIZZES/quiz_05.md` so ethics and meta-learning coverage are represented appropriately.
- [ ] Update `ASSESSMENTS/Final_Exam.md` if stronger Unit 5 assessment alignment is needed.

## Phase 5: Course-Level Alignment

- [ ] Update `START_HERE.md` only if students need clearer guidance about the new materials.
- [ ] Update `STUDENT_PROGRESS_CHECKLIST.md` only if the added materials should appear in the student workflow.
- [ ] Review `README.md` to ensure the top-level course promise still matches the real structure.
- [ ] Verify that any new files follow the repo's bilingual or student-friendly tone where appropriate.

## Phase 6: Verification

- [ ] Open each new notebook and verify structure consistency with existing course notebooks.
- [ ] Run or sanity-check the code paths in each newly added notebook.
- [ ] Verify exercises are solvable from preceding examples.
- [ ] Verify instructor-only solutions are separated from student-facing flow.
- [ ] Recheck quizzes and exam changes for scope, clarity, and non-duplication.
- [ ] Do one final pass to confirm the course is stronger for students, not just longer.

## Phase 7: Cleanup

- [ ] Remove placeholder text, weak prompts, and duplicated explanations.
- [ ] Normalize filenames, section ordering, and notebook naming.
- [ ] Confirm no instructor-only material is exposed in student-facing locations.
- [ ] Prepare a concise summary of what was added and why.
