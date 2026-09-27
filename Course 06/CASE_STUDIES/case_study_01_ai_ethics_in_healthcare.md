# Case Study 01: The risk model that brought down a government
## What an AI governance board does the day the audit comes back

**Course:** Course 06 — AIAT 116, Artificial Intelligence Ethics
**Type:** Case-study analysis (official assessment instrument) — **team analysis**, presented in the session-69 block
**Points:** 100, scaled to **20** of the course's 100
**Set:** session 65 · **Checkpoint:** session 67 · **Due:** session 68 · **Presented:** session 69
**Effort:** one hour per team member. 10 min reading · 15 min collecting numbers from your own notebook runs · 30 min writing your section · 5 min checking the whole
**Length:** 1,500–2,000 words. Teams of four; each member owns one section and signs it.

> *File name.* This file keeps its original name so that the links in `README.md` and
> `START_HERE.md` still work. The case is not a healthcare case; it is the Dutch childcare-benefits
> affair, the case this course returns to in three of its notebooks.

---

## 1. The situation

### What happened

Between roughly 2005 and 2019 the Netherlands' Tax and Customs Administration (*Belastingdienst*)
ran risk models to flag childcare-benefit claims for fraud investigation. Applicants' **(dual)
nationality** was one of the inputs. Families flagged by the model were ordered to repay their
allowances in full — typically **€20,000 to €60,000** each — often for administrative errors rather
than fraud. Families went into debt and bankruptcy; children were taken into care.

| Date | What the record shows |
|---|---|
| October 2018 | The administration stops using nationality in the risk model |
| 17 December 2020 | A parliamentary inquiry publishes its report, *Ongekend onrecht* ("Unprecedented injustice") |
| **15 January 2021** | The entire Rutte III cabinet resigns over the affair |
| **7 December 2021** | The Dutch Data Protection Authority fines the Minister of Finance **€2.75 million**: €750,000 for unlawfully storing second nationality (it should have been deleted by January 2014 and was still there in 2018), €1 million for using nationality as an indicator in the risk-classification model, and €1 million for using it to detect organised fraud |

The regulator described the breach as so severe that it set aside its usual fine-calculation
policy. The number of families wrongly accused is usually given as **roughly 26,000**.

### The part that is not in the headline

The administration had procedures, lawyers and a data-protection officer. It would have scored
respectably on a governance maturity checklist (`unit5-governance-regulations/examples/03_governance_frameworks.ipynb`
makes exactly that point). The harm was not a missing checkbox. It was in what the model was *for*,
what it fed on, and the fact that in fifteen years **no person had the job of answering for its
decisions** — and no family had a route to contest one that would have surfaced the pattern in
year one rather than year fifteen.

Nationality was removed from the model in 2018. Removing a column is the first thing every team
proposes, and `unit2-bias-fairness/examples/01_bias_detection.ipynb` shows what it buys: a model
that never saw the protected column and still reconstructed the group split from proxies.

You have met this case in `unit3-privacy-security/examples/04_gdpr_compliance.ipynb`,
`unit4-transparency-accountability/examples/04_accountability_frameworks.ipynb` and
`unit5-governance-regulations/examples/03_governance_frameworks.ipynb`. Every fact above is on
the record there.

**Sources:** Autoriteit Persoonsgegevens, *Tax Administration fined for discriminatory and unlawful
data processing*, press release, 7 December 2021 (the fine and its three components); Pinsent Masons
Out-Law, *Dutch tax authority handed record fine for discriminatory data processing*, December 2021
(the October 2018 and deletion-deadline details); Parliamentary Committee of Inquiry into Childcare
Allowances, *Ongekend onrecht*, 17 December 2020; the cabinet's resignation statement of
15 January 2021 as reported by CNBC, France 24 and Al Jazeera on that date.

---

## 2. The decision you must make

Your team is the four-person **AI governance board** that a Saudi social-benefits agency created
last month, after reading about the Dutch case. Its first item of business is an internal audit of
the agency's own **fraud-risk model**, which has been in production for six years and is retrained
every quarter on the previous quarter's investigation outcomes.

The audit found:

- the model does not use nationality — that column was removed in 2022 — but it uses **country of
  birth, residency-permit type and the applicant's district**;
- claimants flagged by the model are investigated at a rate that differs between groups by more
  than the agency's own fairness guideline allows; the audit did not say which fairness measure it
  used;
- **91% of flags are never seen by a human** before the repayment letter is generated;
- there is no appeal route other than writing to the same office that sent the letter;
- nobody in the organisation chart is named as accountable for the model's decisions.

The board must decide **this week** and put its decision in writing to the Director-General, who
will act on it. Every option must include a plan for the families already flagged.

**Choose exactly one and defend it:**

- **A — Switch the model off today** and return to manual review. You must say what happens to
  the investigation queue, who bears that cost, and what evidence would let you switch it back on.
- **B — Keep it running under remediation:** remove the proxy features, add a human-review
  threshold, an audit trail and a redress path. You must say what evidence, by what date, would
  show the remediation is working — and what you do if it is not.
- **C — Keep it running unchanged** while a ninety-day investigation runs. You must name the role
  that signs that decision and state, in one sentence, what that person is accepting.

There is no correct option. There are defensible arguments and indefensible ones, and the
difference is whether you brought numbers.

---

## 3. Evidence you must bring from this course

Your analysis must cite **at least four** of the following by notebook filename, with the number
from **your own run**. The course's screening model (`screening-rf-v1.0`, trained on the real
Titanic manifest) is your stand-in for the agency's model: the same audit questions apply, and you
have the numbers.

| Notebook | What it gives you |
|---|---|
| `unit2-bias-fairness/examples/01_bias_detection.ipynb` | The model **never saw `Sex`** and still produced a demographic-parity gap of **0.128** from proxies (fare, class, family size). The same model is *fair* by equalized odds (TPR gap 0.047, FPR gap 0.031). Per-group accuracy 0.713 against 0.598. Different metrics, different verdicts, one model. |
| `unit2-bias-fairness/examples/02_bias_mitigation.ipynb` | The historical outcome gap is **55.3 points**. Post-processing for demographic parity took the DP gap from 0.5958 to **0.0322** and accuracy from 0.8172 to **0.6754**; post-processing for equalized odds reached an EO gap of 0.0040 at accuracy 0.7313. Reweighing moved DP by −0.0072; correlation removal made it *worse* (+0.0178), and a non-linear attacker still recovered the group at **1.000** afterwards. |
| `unit3-privacy-security/examples/04_gdpr_compliance.ipynb` | 12 columns held, **6** used, **5** personal fields carried for no modelling benefit. Compliance score 5/8 = **62%**, not ready. The DATA-441 annex: as deployed, **11** personal columns leave the Kingdom; only the combination of minimisation *and* an in-Kingdom endpoint passes 4/4. |
| `unit4-transparency-accountability/examples/04_accountability_frameworks.ipynb` | **204 of 223** decisions (91.5%) made without human review. Policy said review below 0.70; the router was set to **0.60**; the trail turned that two-line configuration gap into **29** countable decisions (13.0%) at **62.1%** accuracy against 78.9% overall — 7 female, 22 male. The RACI row for individual decisions names a Case Officer, never "the algorithm". |
| `unit4-transparency-accountability/examples/05_hitl_approaches.ipynb` | Threshold 0.7 sends a **0.228** share of cases (22.8%) to humans and lifts automated accuracy to 0.850; threshold 0.9 sends **52.6%** and reaches 0.913. The routing rule itself defers the two groups at rates **0.066** apart. A HITL policy is not automatically the fair option. |
| `unit4-transparency-accountability/examples/06_transparency_tools.ipynb` | Per-group accuracy gap **0.022**; per-group predicted-outcome gap **0.470** — 21× larger. A model card that disaggregates only accuracy passes review. |
| `unit5-governance-regulations/examples/05_ai_governance_frameworks.ipynb` | Compliance check 6/8 = **75%**, verdict *not ready* (no DPIA, no incident process). Risk tier: **high risk, EU AI Act Annex III**. Obligations phase in on 2 February 2025, 2 August 2025, 2 August 2026 and 2 August 2027; the notebook counts how many are in force on the day you run it. |

---

## 4. Analysis questions

These have no single right answer. Answer all five inside the five sections in §5 — the mapping is
in the table there.

**Q1 — Which fairness measure, and who chooses it.** The course's own model was flagged by
demographic parity and cleared by equalized odds (`01_bias_detection`). For a fraud-risk queue,
choose the measure the agency must enforce. State what it costs the group it disadvantages
(`02_bias_mitigation`: every fix spent accuracy, and no fix satisfied both). Then say **who** should
make that choice — the engineer, your board, the Director-General, a court — and why it is not the
engineer.

**Q2 — The column that was deleted and the group that was not.** The Dutch administration dropped
nationality in 2018; your agency dropped it in 2022 and kept country of birth, permit type and
district. Using the result in `01_bias_detection` (a gap of 0.128 with the column gone) and the
attacker table in `02_bias_mitigation` (linear attacker 0.653, non-linear 1.000 after correlation
removal), design the test that shows whether the group is still recoverable from what remains, and
say what you do if it is.

**Q3 — The human who was not in the loop.** For fifteen years nobody was accountable for the
Dutch model's decisions. Write the two RACI rows the agency is missing — *individual decision* and
*appeal* — with job titles. Set the human-review threshold from the table in `05_hitl_approaches`
and defend the staffing cost it implies. Then use the 0.60-versus-0.70 finding in
`04_accountability_frameworks` to describe the monthly audit query that would catch your own router
drifting.

**Q4 — Redress that would have surfaced 26,000 families in year one.** Write the appeal path: who
receives an appeal, what they are empowered to change, what deadline binds them, and what happens
if they do nothing. Then name **one statistic the agency publishes every quarter** — computable
from the audit trail you designed in Q3 — that would have exposed the Dutch pattern in its first
year rather than its fifteenth.

**Q5 — Your decision, signed.** Commit to A, B or C from §2. Argue the strongest case *against*
your own choice. Say what it costs the agency, and the families, if you are wrong. Name the role
that signs. State what evidence, within ninety days, would make the board reverse it. Each team
member signs one section of the document; the board signs Section 5 together.

---

## 5. What you submit

One document, five sections, marked out of 100. The four roles from the group-work guide map onto
the sections; the whole team is accountable for Section 5.

| Section | Points | Feeds from | Owner (role) |
|---|---:|---|---|
| 1. Problem analysis | 20 | Q1 | fairness-metric implementation |
| 2. Intervention design | 25 | Q2, Q3 | subgroup performance analysis |
| 3. Intervention and mitigation plan | 25 | Q3, Q4 | mitigation (pre-/in-/post-processing) |
| 4. Evaluation | 15 | Q2, Q4 | audit report and recommendation |
| 5. Recommendation, limits and ethics | 15 | Q5 | the whole board |

### What a strong answer contains

This is a description of **properties**, not of content. Two teams can recommend opposite things
and both score full marks — and in the session-69 block they will argue it in front of each other.

- **A constraint the brief did not state.** The brief gives you six years of production, a
  quarterly retrain, 91% automation and no appeal route. A strong Section 1 names something else
  that binds — the retrain learns from the outcomes of its own flags; the agency cannot lawfully
  collect the attribute it would need to audit; the queue does not stop while you deliberate — and
  says how it was inferred.
- **A fairness measure chosen, named, and priced**, never "we will make it fair". The measure, the
  group that pays for it, and the person who decided.
- **An alternative considered and rejected, with the reason.** "Switch it off" is a full-credit
  design if it is specified as concretely as any other: what the manual queue looks like, who
  works it, and what gets measured before the model may return.
- **A baseline that exists before the remediation.** Measure the current model's per-group flag
  rates and the current appeal volume *before* anything changes. Without that number, "the
  remediation worked" is an opinion.
- **Something that happens after the decision.** A monthly audit query, a published quarterly
  statistic, a redress path with a deadline, and the named role that receives the escalation.
- **Two limitations that would genuinely make your proposal fail**, and what you would do about
  each. "Bias is complex" earns nothing.
- **Who is affected who never uses the system** — the family that repaid €40,000 for a paperwork
  error, the child taken into care, the caseworker who deferred to a score because it was usually
  right.
- **At least four references to this course's own material**, by filename, with your own numbers.

### Rules

- Submit markdown or PDF. Code is optional; if you include a snippet it must match your written
  design.
- Over the word count by more than 25% loses marks. Length is not the deliverable.
- Every member signs the section they own. In the session-69 block each member answers questions
  on the whole document, not only their section.
- If you used an AI assistant, declare it in one line at the end: which tool, for what. Declared
  assistance is permitted.

---

## 6. Sources

- Autoriteit Persoonsgegevens (Dutch Data Protection Authority), *Tax Administration fined for
  discriminatory and unlawful data processing*, 7 December 2021 — the €2.75 million fine and its
  three components.
- Pinsent Masons Out-Law, *Dutch tax authority handed record fine for discriminatory data
  processing*, December 2021 — the October 2018 end of nationality use and the retention detail.
- Parlementaire ondervragingscommissie Kinderopvangtoeslag, *Ongekend onrecht*, 17 December 2020.
- CNBC, *Dutch government resigns after childcare benefits scandal*, 15 January 2021; France 24
  and Al Jazeera reports of the same day.
- Chouldechova, A., *Fair prediction with disparate impact*, Big Data 5(2), 2017 — the
  impossibility result behind Q1, as used in `unit2-bias-fairness/examples/01_bias_detection.ipynb`.
- Mitchell, M. et al., *Model Cards for Model Reporting*, FAT* 2019 — the card format in
  `unit4-transparency-accountability/examples/06_transparency_tools.ipynb`.

**For:** Course 06 — AIAT 116
