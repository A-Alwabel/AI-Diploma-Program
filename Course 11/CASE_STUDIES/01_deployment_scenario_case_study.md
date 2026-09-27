# Case Study 01: The healthy service that served wrong answers
## Writing the monitoring and retraining policy after Instacart, March 2020

**Course:** Course 11 — AIAT 125, Deploying AI Models
**Type:** Case-study analysis (official assessment instrument)
**Points:** 100, scaled to 10 of the course's 100
**Set:** session 120 · **Due:** session 125
**Effort:** one hour. 10 min reading · 15 min collecting numbers from your own notebook runs · 30 min writing · 5 min checking
**Length:** 1,200–1,500 words. Individual work.

---

## 1. The situation

### What happened

Instacart's item-availability model predicts whether a product a customer orders will be on the
shelf when a shopper arrives. In March 2020 shoppers emptied the shelves of toilet paper, flour,
eggs and sanitiser in a week, and the model kept predicting the world of February.

| Fact | Figure |
|---|---|
| What the company saw | *"At the beginning of March, we saw nearly a 30% drop in ordered items being found"* |
| The metric's fall, as reported by Fortune | the found-rate metric's accuracy dropped **to 61% from 93%** |
| First fix | the model was run **every 60 minutes** — double the previous rate |
| Second fix | the look-back window was cut **from 30 days to one week, and in places three days** — a month of history had become a description of a world that no longer existed |
| After the fixes, as reported by Fortune | the metric was correct **about 85%** of the time |

Nothing about the model had changed. The shelves had.

### The part that is not in the headline

Every infrastructure dashboard was green. CPU normal, memory normal, error rate zero, latency
unchanged. The service was healthy and its answers were wrong, and the only reason anyone knew was
that this particular model is lucky: its label arrives within the hour, when the shopper reaches
the shelf. For a fraud, churn or credit model the label arrives in weeks or never, and the same
failure is invisible for as long as that takes.

Instacart's answer was not a cleverer drift detector. It was the boring baseline: retrain often,
on a short window. `unit5-pipelines-monitoring/enrichment/E11_drift_detection_is_harder_than_it_looks.ipynb`
measures why that is not a lazy answer.

You met the case in `unit3-cloud-deployment/examples/06_monitoring_logging_cloud.ipynb`, which runs
"the Instacart test" on the course's own deployed model, and again in
`unit5-pipelines-monitoring/examples/01_model_monitoring.ipynb` and
`03_alerting_incident_management.ipynb`.

**Sources:** Instacart, *Building an Essential Service During a Pandemic* — a Q&A with CTO Mark
Schaaf, tech.instacart.com, 21 May 2020, republished at company.instacart.com (the 30% figure, the
60-minute cadence and the window change, all quoted above); Fortune, Jonathan Vanian, 9 June 2020,
fortune.com/2020/06/09/instacart-coronavirus-artificial-intelligence (the 93%, 61% and 85%
figures, and the quotation from Instacart's machine-learning director that the shift was "a shock
to the system").

---

## 2. The decision you must make

You are the ML platform engineer at a **Saudi grocery-delivery platform**. Your item-availability
model serves every order. Demand changes shape every Ramadan, every Eid, every summer, and every
time a school year starts — and it changed shape in a week in March 2020 too. The head of
engineering wants a written **operating policy** for the model: what is monitored, what triggers a
retrain, how a new model reaches production, and who is paged when.

You have the request logs, the shopper's found/not-found label within the hour, one engineer
besides yourself, and a cloud budget that the finance team reads.

**Choose exactly one and defend it:**

- **A — Scheduled retraining on a short window** — Instacart's fix. You must state the cadence,
  the window, what a short window costs you in the week after Eid, and what the schedule cannot
  catch.
- **B — Drift-triggered retraining.** A detector on inputs or predictions decides when to
  retrain. You must state the detector, its window, its threshold, the baseline it compares
  against, and — from `E11` — the alarm rate you expect in an ordinary month.
- **C — Scheduled retraining plus a canary gate plus a human loop.** Every candidate model
  serves a slice before it serves everyone; shoppers' corrections feed the next retrain. You must
  size the slice, in observations, and say what happens while you wait for them.
- **D — No automation.** Monitor, and retrain by hand when a human decides. You must say who
  that human is, what they look at, and what it cost Instacart to find out from customers.

There is no correct option. There are defensible arguments and indefensible ones, and the
difference is whether you brought numbers.

---

## 3. Evidence you must bring from this course

Your analysis must cite **at least three** of the following by notebook filename, with the number
from **your own run** (they will differ slightly from the figures quoted here, and where they do,
report yours). An analysis that argues from principle alone cannot pass Section 1 or Section 5.

| Notebook | What it gives you |
|---|---|
| `unit3-cloud-deployment/examples/06_monitoring_logging_cloud.ipynb` | The Instacart test on the course's own model, across a shift: p50 latency 4.94 → 3.78 ms, p95 5.04 → 3.84 ms (timing values move run to run; the direction is the point), errors 0 → 0, mean confidence 0.974 → 0.946, share predicted `virginica` **36.7% → 0.0%**, accuracy **1.000 → 0.567**. The accuracy row is only visible because the classroom kept the labels. |
| `unit5-pipelines-monitoring/examples/01_model_monitoring.ipynb` | After the shift, `versicolor` predictions fell from 27.4% to **0.0%**; p95 latency rose 46 → 163 ms against a 100 ms SLO; the first alert fired **25 requests** after the incident began. Thresholds set without a healthy baseline are guesses. |
| `unit5-pipelines-monitoring/examples/02_retraining_pipeline.ipynb` | Over 24 simulated weeks: never retrain, mean accuracy **0.481** (worst week 0.183); scheduled every four weeks, **0.883** with 6 retrains; drift-triggered, **0.821** with 4 retrains. Champion 0.644 against challenger 0.978; promote only if the challenger strictly wins on the same held-out set. |
| `unit5-pipelines-monitoring/enrichment/E11_drift_detection_is_harder_than_it_looks.ipynb` | 663,522 real dispatches. The traffic share fell from 35.5% to **20.8%** in April 2020 — the one event verifiable from outside the data. A KS test on hour-of-day alarms in **26 of 43** months; PSI above 0.10 alarms in **0**; they agree on 40% of months. Alarm rates of 37%, 58% and 50% for 7-, 30- and 90-day windows. On an ordinary month the p-value fell **4,727×** as the window grew while the effect size stayed about 0.021. Correlation with monthly F1: KS −0.322, PSI −0.612, shift in the *label* rate **−0.718**. |
| `unit5-pipelines-monitoring/examples/07_ab_testing_canary_deployment.ipynb` | The 5% canary stage decided on **17 requests**; a perfect 17-for-17 slice only bounds accuracy above **0.816**. The bad canary was rolled back with 5% of users exposed. A slice that small detects crashes, not quality. |
| `unit1-deployment-basics/examples/05_model_validation_testing.ipynb` | A deployment gate returned APPROVED on **30 of 30** validation rows — with a 95% interval of **[88.4%, 100%]** that crosses the 90% threshold it was gating on. |

---

## 4. Analysis questions

These have no single right answer. Answer all five inside the five sections in §5 — the mapping is
in the table there.

**Q1 — Which signal moves first.** In `06_monitoring_logging_cloud` the infrastructure row did not
move and the prediction-distribution row did. For an availability model, list the signals in the
order they would move — input distribution, prediction distribution, confidence, found-rate label —
and for each say whether it needs labels, what lead time it buys, and what false alarms it produces
in an ordinary week. Then say which one Instacart could have seen a week earlier.

**Q2 — Scheduled or triggered.** `02_retraining_pipeline` scored the schedule above the trigger;
`E11` shows the trigger's verdict depends on the window, the bins and the reference more than on
the world. Argue for A or B. Say what the "boring baseline" is that any detector you build must beat,
and what a three-day window costs you in the week after Eid, when the world snaps back.

**Q3 — The size of the gate.** `07_ab_testing_canary_deployment` decided on 17 requests;
`05_model_validation_testing` approved on 30 rows. Your model's healthy found-rate is around 93%
and the failure you must catch is a fall to 85%. Compute — with a binomial interval, or the
notebook's own table — how many observations the canary slice needs before it can tell those two
apart, and say what serves the customers while you collect them.

**Q4 — The label that arrives late.** Your availability label arrives within the hour. Name a
second model at the same company whose label arrives in weeks — a fraud, a churn, a credit
decision — and rewrite your policy for it. Which of the signals in Q1 survive, and what does the
`E11` correlation table (label shift −0.718, covariate KS −0.322) say about how much you have lost?

**Q5 — Your recommendation and its price.** Commit to A, B, C or D from §2. Argue the strongest
case *against* your own choice. Say what it costs the platform if you are wrong — orders refunded,
shoppers sent to empty shelves, a retrain that ships a worse model at 03:00 — and write the runbook
line: who is paged, what they look at first, and how they roll back.

---

## 5. What you submit

One document, five sections, marked out of 100.

| Section | Points | Feeds from |
|---|---:|---|
| 1. Problem analysis | 20 | Q1, Q4 |
| 2. Solution design | 25 | Q2 |
| 3. Implementation plan | 25 | Q3, Q5 |
| 4. Evaluation | 15 | Q3, Q1 |
| 5. Recommendations, limits and ethics | 15 | Q5, Q4 |

### What a strong answer contains

This is a description of **properties**, not of content. Two students can recommend opposite things
and both score full marks.

- **A constraint the brief did not state.** The brief gives you hourly labels, one engineer, a
  finance team and a calendar of predictable shocks. A strong Section 1 names something else that
  binds — a retrain that runs hourly on all stores costs money every hour; the label is biased
  because shoppers substitute rather than report; a Ramadan night looks like no training window —
  and says how it was inferred.
- **Success defined as a number with a target**, never as "the model stays accurate". A found-rate
  floor, a detection latency in hours, an alarm precision, and what happens when each is missed.
- **An alternative considered and rejected, with the reason.** A design that names only what it
  chose has not been designed.
- **A baseline that appears before the detector in the plan.** For this problem the baseline is
  Instacart's: retrain on a schedule with a short window, and measure it for a month before you
  claim a detector beats it (`E11`: periodic retraining frequently does).
- **Something that happens after deployment.** A monitor with a threshold set from a measured
  healthy week, a champion/challenger gate, a rollback that has been rehearsed, and the named
  person who is paged.
- **Two limitations that would genuinely make your proposal fail**, and what you would do about
  each. "Drift is hard" earns nothing without the number from `E11` that shows how hard.
- **Who is affected who never uses the system** — the shopper sent to an empty shelf, the
  customer whose order is silently substituted, the small store whose stock the model never
  learned.
- **At least three references to this course's own material**, by filename, with your own numbers.

### Rules

- Submit markdown or PDF. Code is optional; if you include a snippet it must match your written
  design.
- Over the word count by more than 25% loses marks. Length is not the deliverable.
- If you used an AI assistant, declare it in one line at the end: which tool, for what. Declared
  assistance is permitted. You will be asked to walk through your Section 3 plan aloud.

---

## 6. Sources

- Instacart, *Building an Essential Service During a Pandemic* (Q&A with CTO Mark Schaaf),
  tech.instacart.com, 21 May 2020; republished at company.instacart.com.
- Vanian, J., Fortune, 9 June 2020, fortune.com/2020/06/09/instacart-coronavirus-artificial-intelligence.
- Gower-Winter et al. (2026), on concept-drift detection being ill-posed as usually framed, IDA 2026 —
  as cited in `unit3-cloud-deployment/examples/06_monitoring_logging_cloud.ipynb` for the claim that
  periodic retraining frequently outperforms drift-aware methods.
- Wong, A. et al., *External Validation of a Widely Implemented Proprietary Sepsis Prediction Model
  in Hospitalized Patients*, JAMA Internal Medicine, 2021 — the reference case for "a healthy service
  serving wrong answers" in `unit1-deployment-basics/examples/05_model_validation_testing.ipynb`,
  if you use it for Q3.

**For:** Course 11 — AIAT 125
