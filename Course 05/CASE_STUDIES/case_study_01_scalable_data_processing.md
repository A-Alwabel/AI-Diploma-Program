# Case Study 01: Fifteen thousand rows that never arrived
## Designing an ingestion pipeline after Public Health England's spreadsheet failure

**Course:** Course 05 — AIAT 115, Scalable Data Science
**Type:** Case-study analysis (official assessment instrument)
**Points:** 100, scaled to 10 of the course's 100
**Set:** session 54 · **Due:** session 59
**Effort:** one hour. 10 min reading · 15 min collecting numbers from your own notebook runs · 30 min writing · 5 min checking
**Length:** 1,200–1,500 words. Individual work.

---

## 1. The situation

### What happened

In autumn 2020 Public Health England (PHE) collected COVID-19 test results from commercial
laboratories. The laboratories sent CSV files. PHE's process loaded those results into Excel
templates saved in the legacy **`.xls`** format, and passed the templates on to the national
reporting dashboards and to contact tracing.

`.xls` stops at **65,536 rows**. When a template filled up, the rows past the limit were not
rejected and were not flagged. They were dropped. Nothing errored. The process reported success.

| Fact | Figure |
|---|---|
| Positive cases that never reached the daily count or contact tracing | **15,841** |
| Period over which they were lost | **25 September – 2 October 2020** |
| File format at the point of failure | legacy `.xls`, **65,536-row** ceiling |
| Why the ceiling was reached faster than it sounds | each test result occupied several rows, so a template held on the order of **1,400 cases**, not 65,536 |
| The fix that was applied | split the data across more, smaller spreadsheets |

The government described the incident as a "file size" problem: some files "exceeded the maximum
file size that takes these data files and loads then into central systems". Every one of the 15,841
people had tested positive. Their contacts were not told for up to a week.

### The part that is not in the headline

Nothing about this failure required a hard algorithm. It required a row-count check, a file format
chosen for the volume, and an alert on a number that stopped growing. It happened in a national
health agency with a professional data team in the middle of a pandemic, and it happened silently
for eight days, which is the part to hold onto: **the pipeline did not fail; it succeeded at the
wrong thing, and reported success.**

You met the same shape twice in this course. `unit1-introduction/examples/02_pandas_numpy_basics.ipynb`
uses PHE as the reason pandas exists; `unit5-scaling/examples/07_large_datasets.ipynb` uses it as the
reason chunked processing exists. Both notebooks make the same point: the 708 MB, 2,300,825-flow
capture they stream in seconds is many times larger than anything PHE was handling, and it needed
no cluster, only the right container and the right loop.

**Sources:** The Register, 5 October 2020, theregister.com/2020/10/05/excel_england_coronavirus_contact_error
(the 15,841 figure, the date range, the `.xls` limit and the "file size"
statement); Public Health England / Department of Health and Social Care statements of
4–5 October 2020 as reported there. The same facts appear in the two notebooks named above.

---

## 2. The decision you must make

You are the data lead at a **regional health cluster in Saudi Arabia**. Forty laboratories, public
and private, send you result files every night. Each laboratory has its own template. The Ministry
dashboard must be updated by 08:00 and the contact-tracing team works from the same feed. Volume
is a few thousand rows per laboratory per night today, and the cluster has been told to plan for
ten times that.

Your director has read about PHE and wants a written recommendation. You have thirty days and one
engineer besides yourself.

**Choose exactly one and defend it:**

- **A — Keep the laboratories' spreadsheet templates**, because forty laboratories already know
  them, and build validation, a row-count assertion and monitoring on top of the existing loader.
  You must state exactly which checks, where they run, and what they cannot catch.
- **B — Replace the templates with a data contract** (a fixed CSV or Parquet schema with declared
  types), a chunked ingestion job under a scheduler with retries, idempotent loads, and alerting.
  You must state what the migration costs the laboratories and what happens to a laboratory that
  cannot comply by day thirty.
- **C — Buy a distributed platform** (a Dask or Spark cluster, or a managed lakehouse) because the
  cluster has been told the data will grow tenfold. You must state the volume at which this
  choice stops being overhead, with numbers from this course.

There is no correct option. There are defensible arguments and indefensible ones, and the
difference is whether you brought numbers.

---

## 3. Evidence you must bring from this course

Your analysis must cite **at least three** of the following by notebook filename, with the number
from **your own run** (timings will differ from machine to machine; where they do, report yours).
An analysis that argues from principle alone cannot pass Section 1 or Section 5.

| Notebook | What it gives you |
|---|---|
| `unit1-introduction/examples/02_pandas_numpy_basics.ipynb` | The 708 MB CIC-IDS2017 capture (2,300,825 flows) cannot simply be `read_csv` whole; the notebook reads the bundled 14,015-row sample and keeps 4 of 79 columns with `usecols`. Rule of thumb: pandas wants several times the file size in RAM. |
| `unit2-cleaning/examples/01_data_loading.ipynb` | `read_csv` sniffed the `Date` column as `object` (text) until `parse_dates=` was passed. An Excel round-trip dropped the `category` dtype and the `int8` — "Excel stores values, not pandas types". Streaming 16,000 rows in 8 chunks of 2,000 held at most **0.03 MB** in memory, against a 4.7 MB file and a 151 MB original. |
| `unit2-cleaning/examples/02_missing_values_duplicates.ipynb` | 866 missing values, none planted. `dropna()` keeps **183 of 891** rows (79% thrown away). Mean-filling `Age` shrinks its standard deviation from **14.53 to 13.00**. **210** repeated ticket numbers are not duplicates — families travelled on one ticket. A dedup rule can delete real records silently. |
| `unit5-scaling/examples/02_dask_distributed.ipynb` | On data already in memory, pandas was **25×** faster than Dask on a groupby in this session's run (0.0008 s against 0.0196 s); end to end, including the load, 0.01 s against 0.02 s. The multiple moves between runs; the direction does not. Dask wins when the data does not fit, not before. |
| `unit5-scaling/examples/07_large_datasets.ipynb` | 14,015 flows streamed in 10 chunks of 1,500 (the last holds 515): peak memory **1.3 MB** all at once against **0.1 MB** per chunk, about **9×** — with only 6 of the 79 columns. Carry SUM and COUNT per chunk; averaging chunk means is wrong when the last chunk is smaller. |
| `unit5-scaling/examples/09_model_monitoring.ipynb` | March–May 2020: accuracy **rose** 0.663 → 0.764 while the traffic-class F1 **fell** 0.337 → 0.223 and the traffic share fell 35.0% → 22.4%. An accuracy-only dashboard stays green through the largest shift in the data. The metric you monitor is the only failure you can see. |
| `unit5-scaling/examples/10_data_pipeline_automation.ipynb` | 51 replayed nightly runs, **51 reported `success`**. A volume assertion (8–24 rows, the median ±50%) would have failed **1** of them (2019-07-11, 29 rows). The null rate per run ranged **0.0%–26.7%**, pooled 12.3%. The pipeline has no scheduler, retries, dependency graph, backfill or alerting; a well-organised script is not a production pipeline. |

---

## 4. Analysis questions

These have no single right answer. Answer all five inside the five sections in §5 — the mapping is
in the table there.

**Q1 — Where the silence lives.** PHE's process reported success for eight days while dropping
rows. Walk through your proposed pipeline from the laboratory's file to the 08:00 dashboard and
list **every** point where a row can disappear without an error: a format ceiling, a type guess
(`01_data_loading`), a `dropna` or a dedup rule (`02_missing_values_duplicates`), a chunk
aggregation done wrong (`07_large_datasets`). For each one, name the check that turns silence
into a failure, and say where it runs. Use the volume assertion in `10_data_pipeline_automation`
as your model: it is one line, and it would have caught PHE.

**Q2 — Size it honestly.** Estimate tonight's volume (rows × bytes) for forty laboratories, then
the tenfold case. Put both next to the course's own measurements: a 708 MB file processed in
chunks in seconds on one laptop; pandas 25× faster than Dask on data that fits. Does option C buy
anything at either volume? Name the number — rows per night, or gigabytes — at which it would.

**Q3 — The format is the contract.** `.xls` stops at 65,536 rows; `.xlsx` at 1,048,576; CSV has
no ceiling and no types; Parquet has types and a schema, and is immutable and columnar
(`unit2-cleaning/examples/07_cudf_import_export_gpu.ipynb` measured Parquet *losing* on a small
warm table). Choose the contract you will give the laboratories. For each format you rejected, say
which failure it makes impossible and which new failure it introduces.

**Q4 — What you would alert on.** In `09_model_monitoring` accuracy went *up* during the lockdown
while the model got worse. For an ingestion pipeline, name the three signals you would page on at
03:00, the threshold for each, the baseline period the threshold comes from (`10_data_pipeline_automation`:
pick the threshold from the picture, *before* the night it fires), and who receives the page.
Say what a false alarm costs your one engineer and what a missed alarm cost PHE.

**Q5 — Your recommendation and its price.** Commit to A, B or C from §2. Then argue the strongest
case *against* your own choice, say what it costs the cluster if you are wrong, and name the one
measurement in the first thirty days that would tell you.

---

## 5. What you submit

One document, five sections, marked out of 100.

| Section | Points | Feeds from |
|---|---:|---|
| 1. Problem analysis | 20 | Q1, Q2 |
| 2. Solution design | 25 | Q3, Q2 |
| 3. Implementation plan | 25 | Q1, Q4 |
| 4. Evaluation | 15 | Q4 |
| 5. Recommendations, limits and ethics | 15 | Q5 |

### What a strong answer contains

This is a description of **properties**, not of content. Two students can recommend opposite things
and both score full marks.

- **A constraint the brief did not state.** The brief gives you forty laboratories, thirty days,
  one engineer and an 08:00 deadline. A strong Section 1 names something else that binds —
  a laboratory that will not change its template, a public holiday, a result that arrives after
  08:00, a column that means different things in two laboratories — and says how it was inferred.
- **Success defined as a number with a target**, never as "reliable" or "scalable". A rows-in
  versus rows-out reconciliation, a latency, a null-rate ceiling, and what happens when it is
  missed.
- **An alternative considered and rejected, with the reason.** A design that names only what it
  chose has not been designed.
- **A baseline that exists before the new pipeline.** Count what the current loader delivers
  tonight — rows in, rows out, minutes — before you replace it. If your plan cannot show that the
  new pipeline delivers more rows than the old one, you cannot show it fixed anything.
- **Something that happens after go-live.** A reconciliation that runs every night, an alert with
  an owner, a rollback to the old loader, and the named person who is paged.
- **Two limitations that would genuinely make your proposal fail**, and what you would do about
  each. "More data would help" and "we need more engineers" earn nothing.
- **Who is affected who never uses the system** — the person whose positive result is in row
  65,537, and the contacts who are never called.
- **At least three references to this course's own material**, by filename, with your own numbers.

### Rules

- Submit markdown or PDF. Code is optional; if you include a snippet it must match your written
  design.
- Over the word count by more than 25% loses marks. Length is not the deliverable.
- If you used an AI assistant, declare it in one line at the end: which tool, for what. Declared
  assistance is permitted. You will be asked to walk through your Section 3 plan aloud.

---

## 6. Sources

- The Register, 5 October 2020, theregister.com/2020/10/05/excel_england_coronavirus_contact_error
  — the 15,841 cases, the 25 September – 2 October window, the `.xls` row ceiling,
  the multi-row-per-result detail and the government's "file size" statement.
- Public Health England / Department of Health and Social Care, statements of 4–5 October 2020,
  as reported above.
- Pimentel, J. F., Murta, L., Braganholo, V. & Freire, J., *A Large-Scale Study About Quality and
  Reproducibility of Jupyter Notebooks*, MSR 2019 — the "about 24% ran, about 4% reproduced"
  figures in `unit1-introduction/examples/05_jupyter_notebooks_best_practices.ipynb`, if you use
  them for Q1.
- Sculley, D. et al., *Hidden Technical Debt in Machine Learning Systems*, NeurIPS 2015 — cited in
  `unit5-scaling/examples/08_deployment.ipynb` for the claim that pipelines fail in the glue, not
  the model.

**For:** Course 05 — AIAT 115
