# SQL — the strand that is not in the official plan

Three lessons, about **6–9 contact hours**, on the one skill that Saudi employers ask junior data
people for more often than anything else this diploma already teaches.

```
SQL/examples/01_getting_the_data_out.ipynb    SELECT, WHERE, ORDER BY, GROUP BY, HAVING
SQL/examples/02_joins_and_windows.ipynb       INNER/LEFT JOIN, fan-out, CTEs, window functions
SQL/examples/03_the_row_count_is_wrong.ipynb  debugging a query somebody else wrote
```

---

## Why this is not inside one of the twelve courses

Because it does not belong to one. The official TVTC specification for this programme — Associate
Diploma in Artificial Intelligence, NQF Level 4, nine months, 420 contact hours — defines twelve
courses, and **not one of them contains SQL**. Filing these lessons under a course would mean
claiming they implement a learning outcome that the specification does not contain.

So they sit in a folder of their own, and this README says plainly what they are: **an addition to
the official plan, made deliberately, for a reason recorded below.** An instructor who must teach
only the official plan can skip this folder entirely and lose nothing that the specification asks
for. An instructor who wants graduates who can hold a job should not.

## The honest reason it exists

A market pass run for this programme collected **322 real job postings**, of which **183 were
located in Saudi Arabia** and **74 were junior-plausible**. Every requirement in them was counted
against a term-by-term scan of all 427 notebooks in the diploma. The top result:

| named in | Saudi postings (183) | junior-plausible (74) |
|---|---|---|
| **SQL** | **63 (34%)** | **21 (28%)** |
| "deep learning" / "neural network" | 15 (8%) | — |
| scikit-learn | 13 (7%) | — |

SQL was asked for roughly **four times** as often as deep learning and **five times** as often as
scikit-learn. And a scan of every notebook outside this folder — all **427** of them — finds **no
cell, code or markdown, containing an uppercase `SELECT … FROM`**. The diploma taught none of it.

The consequence, in the words of the researcher who ran the pass:

> "They will be asked for SQL on day one and will not be able to write it. A graduate who can build
> a CNN but cannot write a JOIN cannot get the data out of the warehouse, which means they cannot
> start the job at all."

A Riyadh fintech posting for a Data Analyst, recorded in that same pass, is more specific than
"know SQL", and it is the syllabus for lessons 01–03 in order:

> "Strong SQL. You can write and debug complex joins, window functions, and CTEs against a large
> transactional schema without hand-holding." … "Ability to scope a vague business question into
> something answerable, and to say clearly when the data can't answer it."

The first job most of these graduates get is **analyst-shaped far more often than model-shaped**.
This folder is the smallest honest response to that fact.

## Where the hours come from

`TEACHING_PLAN.md` in the instructor repository already identifies the cheapest hours in the
programme, in its own words: Course 05 Unit 4, where *"all six are C04 re-teaches"*. Six lessons
that re-teach material from Course 04 are worth less than six hours of SQL a student will use in
their first week of work. Take **6–9 hours** from there.

| lesson | teaches | time |
|---|---|---|
| **01 — Getting the data out** | the table somebody else designed; `SELECT`, `WHERE`, `ORDER BY`, `LIMIT`, `GROUP BY` with `COUNT`/`SUM`/`AVG`, `HAVING`; pandas and SQL side by side; a query that runs and lies | ≈2.5 h (stated in the notebook) |
| **02 — Joins and windows** | `INNER` vs `LEFT JOIN`, fan-out, anti-joins, CTEs, `ROW_NUMBER`/`RANK`/`LAG`/`SUM() OVER` | ≈2.5 h (stated in the notebook) |
| **03 — The row count is wrong** | six failures that give you a clean run and a wrong answer, and how to prove a number wrong before you know why | ≈2–3 h (the longest of the three) |

Lessons 02 and 03 assume lesson 01. Teach them in order.

## What you need to run them

**Nothing.** That is not a slogan, it is a design constraint that was checked:

- Every lesson uses Python's **built-in `sqlite3` module**. No install, no server, no database
  account, no password, no network after the data file is on disk.
- They behave identically on **Windows, macOS and Google Colab**. The setup cell finds the
  repository from any working directory, and downloads the data loader if there is no repository
  at all.
- The database is **built inside the notebook** from data already committed to this repository —
  the Montgomery County, Pennsylvania 911 call log under `Course 04/datasets/`, loaded through
  `tools/data.py`.
- Every lesson loads it with `prefer="sample"`, which pins all three notebooks to the **25,000-row
  sample committed to the repo**, so **every student in the room reconciles against the same
  numbers** and every printed total is reproducible on a fresh clone.

That sample is 1 call in 27 of the real 663,522-call log. The notebooks say so, repeatedly, and
they distinguish between the numbers that survive the thinning (shares, rankings) and the numbers
that do not (totals). Teaching that distinction is part of the point.

## What this strand does not cover

Say this to the students, so they do not overestimate what they now have:

- **Writing to a database.** `INSERT`, `UPDATE`, `DELETE`, transactions, and what happens when two
  people write at once. These lessons only read.
- **Designing a schema.** There is exactly one `CREATE TABLE` in the strand, and it is scaffolding.
  Normalisation, keys and constraints are not taught here.
- **Performance.** Indexes, query plans, `EXPLAIN`, partitioning. Every table here fits in RAM and
  every query returns instantly, which is precisely the situation in which performance cannot be
  taught. The posting's phrase *"a large transactional schema"* is asking for a skill this folder
  does not give.
- **Dialects.** The lessons are written on SQLite and flag the places where SQLite is unusually
  permissive — its flexible typing, its case-insensitive `LIKE`, its tolerance of bare columns in
  an aggregate query — but a student meeting PostgreSQL, SQL Server or BigQuery for the first time
  will still meet surprises.
- **Anything above one database.** No warehouses, no dbt, no orchestration, no BI tools.

## For the instructor

- **No answer keys on the student path.** Lessons 01 and 02 check student SQL with a
  **fingerprint**: they hash the rows of the expected result, so the notebook can say "correct",
  "right rows, wrong order" or "3 of your 5 rows match" **without containing the answer anywhere**.
  Lesson 03 checks a different way, against a stated control total the student must reconcile to.
  Reference solutions live in the instructor repository at `/Users/abdullah/AI-Diploma-Instructor`,
  never here.
- **Lessons 01 and 02 end with an exercise that has no checker, on purpose.** It asks the student
  to scope a vague question and to say what the data cannot answer — the second half of the
  sentence in that fintech posting, and the half no automatic checker can grade. It is meant to be
  argued about in pairs, out loud.
- **The cells that are supposed to fail are tagged `raises-exception`**, so
  `tools/verify/run_notebooks.py` enforces both directions: an untagged error fails the gate, and
  a tagged cell that stops failing fails it too.
- **Re-running any notebook top to bottom rebuilds its database from scratch** (`:memory:`), so a
  student who breaks something recovers by restarting the kernel and running all cells.
