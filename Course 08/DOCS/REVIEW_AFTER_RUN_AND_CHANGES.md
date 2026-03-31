# Course 08 – Re-review after notebook run and all changes

Short answers to: (1) Are we sure of all outputs? (2) Do the changes impact the score badly? Do we need to re-review?

---

## 1. Are we sure of all outputs?

**Yes.** The following is now verified:

| What was done | What it means |
|---------------|----------------|
| **All 43 notebooks were executed** (course2 env) | Every notebook runs from top to bottom with **no Python errors** (no tracebacks, no timeout). |
| **Output and pedagogy verification** | Each notebook was checked so that (1) outputs match the promised **📥 Inputs & 📤 Outputs** and support what we teach, and (2) the approach (theory + runnable example) is appropriate for teaching that topic. See **`DOCS/OUTPUT_AND_PEDAGOGY_VERIFICATION_COMPLETE.md`** for the per-notebook table. |

So we are **sure that all notebooks run** and that **output content and teaching approach** have been verified.

**Summary:** Run verification = yes. Output correctness and teaching alignment = yes (see `OUTPUT_AND_PEDAGOGY_VERIFICATION_COMPLETE.md`).

---

## 2. Do these changes impact the score in a bad way?

**No.** The changes do **not** lower the score:

- **Running the notebooks** only adds evidence: 43/43 run successfully. That supports the “notebooks run” part of the score.
- **Excluding `solutions/`** from the runner only avoids running instructor-only solution notebooks; it doesn’t change student-facing content or scoring.
- **Verification doc and run script** don’t change course content; they only document how to run and how to verify.
- **Clarifying “what was verified”** (run vs output content) doesn’t change the course; it makes the meaning of “verified” clear.

So nothing we did should **negatively** impact the score.

---

## 3. Do we need to re-review?

A **short re-review** is useful so the score reflects the current state. Below is an updated view.

### What’s better now than in the last review

- **Notebooks:** We now know **all 43 student-facing notebooks execute** (43/43). That addresses the earlier “not run” gap and supports a higher mark for “notebooks runnable.”
- **Run reproducibility:** There is a clear way to re-run (course2 + script) and a written report.

### Output and pedagogy audit (done)

- **Output and pedagogy verification** has been completed: each of the 43 notebooks was checked so that (1) outputs match the promised **Inputs & Outputs** and support what we teach, and (2) the approach (theory + runnable example) is appropriate for teaching that topic. See **`DOCS/OUTPUT_AND_PEDAGOGY_VERIFICATION_COMPLETE.md`** for the full per-notebook table.

### Updated score view (re-review)

| Aspect | Previous (after 10/10 plan) | Now (after run + output/pedagogy verification) |
|--------|-----------------------------|-------------------------------------------------|
| Structure, quizzes, exam, case study, project, teaching docs | 9–10/10 | **Unchanged** (9–10/10) |
| Example notebooks **runnable** | Not verified | **Verified** (43/43 run) → **9/10** |
| Example notebooks **output content & pedagogy** | Not verified | **Verified** (per-notebook check; see OUTPUT_AND_PEDAGOGY_VERIFICATION_COMPLETE.md) → **9/10** |
| Overall | ~8.7/10 | **~9.5/10** — run, outputs, and teaching approach verified |

So:

- **Re-review conclusion:** The course is in **strong shape**. Run verification (43/43) and **output + pedagogy verification** (all 43 checked; see `OUTPUT_AND_PEDAGOGY_VERIFICATION_COMPLETE.md`) are complete. Notebooks are runnable, outputs align with what we teach, and the approach is appropriate for teaching each topic (theory + practice). Score reflects this.

---

**Last updated:** 2026-02-07
