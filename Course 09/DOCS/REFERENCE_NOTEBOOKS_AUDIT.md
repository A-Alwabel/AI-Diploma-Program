# Reference Notebooks Audit

## Purpose

This document explains how to treat the long descriptive notebook filenames that
appear beside the numbered notebooks in some unit `examples/` folders.

## Decision

- The **numbered notebooks** are the official student-facing learning path.
- The **long descriptive notebooks** are preserved as **reference/source
  notebooks only**.
- They are kept because the course was built from more than one source set and
  those sources still matter for coverage review.
- They should **not** be used as the student's default study sequence.
- They are now archived under `DOCS/REFERENCE_NOTEBOOKS/` so the student path
  stays clean inside each unit `examples/` folder.

## Why They Are Reference Only

During review, the numbered notebooks were found to be the curated path for
student understanding. They consistently include:

- lesson briefs
- step guides before code
- beginner-friendly comments
- student support packs
- closing takeaways
- saved visuals and outputs

By contrast, many long descriptive notebooks are weaker for student use because
they often contain one or more of these issues:

- overlapping topics already covered better in the numbered path
- inconsistent worked examples
- generic template sections
- topic drift between filename and actual content
- missing student support sections
- missing saved visual outputs

## Student Rule

If you are a student, follow only:

1. the unit `README.md`
2. the numbered example notebooks in order
3. the unit exercise
4. the unit solution after your own attempt

Do not switch to the long descriptive notebooks unless your instructor assigns a
specific one for a specific reason.

## Instructor / Reviewer Rule

Use the long descriptive notebooks only as:

- source comparison material
- reference archives from the earlier course inputs
- backup coverage checks when auditing whether a topic was preserved in the
  numbered path

## Unit-Level Audit Summary

### Unit 1

- The numbered notebooks form a coherent foundational path.
- The long descriptive notebooks are overlapping reference copies and are not
  needed for the main student sequence.

### Unit 2

- The numbered notebooks are the student-ready path.
- The long descriptive notebooks are not reliable as primary lessons because
  some contain generic or mismatched worked examples.

### Unit 3

- The numbered notebooks are the curated teaching path for deep RL.
- The long descriptive notebooks should be treated as archived source material,
  especially where scope drift or incomplete polish exists.

### Unit 4

- The numbered notebooks already cover the intended student path clearly.
- The long descriptive notebooks are overlapping references rather than better
  teaching alternatives.

### Unit 5

- The numbered notebooks are the appropriate student-facing sequence.
- Several long descriptive notebooks are particularly risky for students because
  their internal examples or objectives do not consistently match their titles.

## Bottom Line

Keep the long descriptive notebooks for source preservation.

Do **not** treat them as equal alternatives to the numbered notebooks for
students.
