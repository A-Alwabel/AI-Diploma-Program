# AI System Design Case Study
## Designing, and deciding on, a risk-scoring system

**Course:** Course 01 – AIAT 111 (Introduction to Artificial Intelligence and Applications)
**Type:** Case Study Analysis
**Points:** 100 (scaled to 10 of the course's 100 marks)
**Set:** session 4 · **Due:** session 8
**Length:** 1,200–1,500 words. No code required.
**Time budget:** about one hour — 15 minutes reading and re-opening the two notebooks you will cite, 45 minutes writing.

---

## 1. The situation

This is a documented case. Every fact in this section is on the record, and the same facts appear in
`unit1-ai-foundations/examples/01_ai_introduction.ipynb`, which is where the course opens.

In May 2016 the newsroom ProPublica published *Machine Bias*, an audit of **COMPAS** — a commercial
risk-scoring tool used by courts in Broward County, Florida to advise on bail and sentencing decisions.
The journalists collected the scores of more than **7,000 people** arrested in that county and checked,
two years later, who had actually been rearrested.

Their finding: among the defendants who did **not** go on to reoffend, Black defendants had been labelled
high-risk about **45%** of the time, against about **24%** of white defendants — roughly double the rate.

Northpointe, the company that built the tool, rejected the analysis. It pointed to a different fairness
measure — whether a given score means the same rearrest probability in every group — and on that measure
the scores did behave equally across groups.

**Both sides were arithmetically right.** They were measuring different things and calling both of them
fairness. The argument about which measure a court should use has not been settled, and it is now a
standard result that the two measures cannot both hold when the underlying rates differ between groups.

Three more facts from this course that belong next to it:

- **A vendor's accuracy claim is not a system.** Epic's Sepsis Model, built into one of the most widely
  deployed hospital record systems in the United States, was documented by its maker at AUC 0.76–0.83.
  An external validation published in *JAMA Internal Medicine* in June 2021 (Wong et al.) measured
  **AUC 0.63** and sensitivity around **33%** on hospitalised patients, while alerting on **18% of
  hospitalisations** (6,971 of 38,455). See `unit5-generative-ai-intro/examples/03_diabetes_classification_ffnn.ipynb`.
- **A score can be right and still never be used.** MYCIN, built at Stanford in the 1970s, was put through
  a blinded evaluation published in *JAMA* in 1979: eight independent infectious-disease experts rated the
  therapy chosen for ten real meningitis cases without knowing which came from the machine. MYCIN's
  recommendations were rated acceptable **65%** of the time; the five faculty specialists it was compared
  with scored between **42.5% and 62.5%**. It beat every human in the comparison and was never deployed to a
  single patient — the obstacles were hardware, workflow and liability, not accuracy.
  See `unit2-ai-concepts/examples/02_expert_systems.ipynb`.
- **A wrongly-chosen feature is not a technical detail.** Between 2005 and 2019 the Dutch tax administration
  ran a risk-classification system over families claiming childcare benefits; nationality was among the
  attributes it used. Roughly **26,000 families** were wrongly accused of fraud and ordered to repay
  allowances in full. A parliamentary inquiry called it an "unprecedented injustice", and in January 2021
  the Dutch government resigned over it. See `unit2-ai-concepts/examples/07_encoding_categorical_features.ipynb`.

**Sources.** ProPublica, *Machine Bias*, May 2016 · Northpointe's published response to that analysis,
2016 · Wong et al., external validation of the Epic Sepsis Model, *JAMA Internal Medicine*, 2021 · Yu et al.,
*Antimicrobial Selection by a Computer*, *JAMA*, 1979 (the MYCIN blinded evaluation) · the Dutch
parliamentary inquiry into the childcare-benefits affair, 2020. Each of these is used and referenced in the
notebook named beside it; go there first.

---

## 2. The decision you have to make

You are the technical adviser to a **public agency that pays a monthly family allowance**. Every month it
receives more claims than its staff can review by hand, so today a clerk picks which claims to check using
experience and a two-page checklist. Nobody has ever measured how good that checklist is.

A vendor is offering a **claim-risk score**: claim data in, a 1–10 risk number out, ranked worklist for the
review team. The vendor's written claims are:

- 94% accuracy on its own held-out data;
- "proven in three other countries";
- nationality is not an input;
- the model is proprietary and cannot be inspected, but the vendor will supply a monthly accuracy report.

Your director has to answer one question at the board meeting: **adopt, adopt with conditions, or reject.**
You write the recommendation, and if it is anything other than "reject" you also have to design the system
that goes around the score.

There is no correct answer to this. All three answers can score full marks. What is being marked is whether
your reasoning would survive the meeting.

---

## 3. The evidence you must bring

Your analysis must **cite at least three of this course's own notebooks by filename**, and quote a number or
a specific claim from each. A general answer that cites none of them cannot pass the middle of the mark
range, because it could have been written about any system at all.

| Question you have to answer | Where the course already answered it |
|---|---|
| What exactly does the output claim? | `unit1/01_ai_introduction.ipynb` — describe a system by inputs, output, training data and error rate |
| What does the agent actually have to do? | `unit1/12_case_studies_intelligent_agents.ipynb` — the PEAS specification, and why PEAS starts with P |
| Is 94% a good number? | `unit2/06_supervised_unsupervised_models.ipynb` — 0.9825 accuracy against a 0.6316 always-guess baseline |
| What does one flagged claim mean? | `unit2/04_bayes_theorem.ipynb` — 95 physicians in 100 read a positive mammogram as 75% when the answer was 7.7%; base-rate neglect |
| Where does bias enter, if nationality is excluded? | `unit2/07_encoding_categorical_features.ipynb` — what an encoded category actually tells the model |
| Will the model still work next year? | `unit2/08_data_generation_process.ipynb` — Google Flu Trends estimated more than double the CDC's measured rate for the 2012–13 season |
| Can you see why it decided? | `unit3/05_model_interpretability_shap_lime.ipynb` — the model that gave asthmatic pneumonia patients a *lower* predicted risk of death |
| What is a fair error to make? | `unit3/01_regression_classification.ipynb` — Zillow Offers, a model wrong by dollars in one direction |

> Paths in the table are abbreviated. `unit2/04_bayes_theorem.ipynb` means
> `unit2-ai-concepts/examples/04_bayes_theorem.ipynb`; the unit folder names are in the course README.

---

## 4. What you submit

Five sections, in this order. The marks are on the reasoning inside them, not on their length.

**1. Problem analysis.** What is the core problem, in one sentence a board member would understand? Who is
affected — including people who never touch the system? What are the constraints, including any the brief
above does not state outright? What would count as success, as a number you could measure?

**2. Solution design.** What system do you propose — including "no system"? If a score is used, write the
PEAS specification. Say where the data enters, what the score is allowed to be used for, and what a human
does with it. Name one alternative you considered and rejected, and why.

**3. Implementation plan.** Five to eight ordered steps someone could start on Monday. Include the step
almost everyone omits: how you measure the *current* clerk-and-checklist process before anything replaces it.

**4. Evaluation.** Which numbers you would require, before signing and after going live. Say which fairness
measure you are requiring and what it costs you, given that you cannot have both. Say what you would monitor
monthly and what result would make you switch the system off.

**5. Recommendation, limits and ethics.** Your decision, in one sentence. Then at least two limitations that
would genuinely make your own proposal fail, and what you would do about each. Then: what happens to a
family whose claim is wrongly flagged, and how do they contest it?

---

## 5. Analysis questions

Answer these inside your five sections — do not answer them as a separate list. None has a single right
answer, and two students who disagree can both be right.

1. **ProPublica and Northpointe were both arithmetically correct.** Which fairness measure would you write
   into the contract for *this* agency, and what does choosing it cost the group it disadvantages? Say the
   cost out loud; a recommendation that claims to satisfy both measures is wrong.

2. **The vendor says 94%.** What else do you need to know before that number means anything? Work out what
   the agency's own base rate of wrongful claims would have to be for a flagged claim to be more likely
   right than wrong.

3. **Nationality is not an input — and the Dutch system's failure is still available to this model.** Name
   two or three fields in ordinary claim data that could carry the same information, and describe how you
   would test whether they do, given that you cannot inspect the model.

4. **MYCIN beat five specialists and was never used.** Name two things in your implementation plan that
   decide whether the review team actually uses this score — and neither of them is accuracy.

5. **What would make you recommend rejecting the tool and changing nothing?** Answer this even if your
   recommendation is to adopt: state the measurement that would have changed your mind.

---

## 6. What a strong answer contains

This is not a list of the right answers. It is what the marker is looking for.

- **A constraint the brief did not state.** It is in there. Finding it is worth more than any technique you
  can name.
- **Success defined as a measurable target**, not "high accuracy". "Accuracy" on this problem is close to
  meaningless and a strong answer says why in one sentence.
- **A baseline.** The clerk and the two-page checklist have an error rate that nobody has measured. An
  analysis that compares the vendor's score to nothing has repeated the mistake this course opens with.
- **An alternative that was considered and rejected**, with the reason — including the alternative of
  measuring the current process and buying nothing.
- **Named course evidence.** Three notebooks, three specific numbers or claims, used to support an argument
  rather than decorate one.
- **A limitation of your own proposal that would genuinely sink it.** "More data would help" is true of
  every project ever written and earns nothing.
- **A named consequence for a real person** when the system is wrong, in the direction it is most often
  wrong — and a route by which that person can contest it.

"There are no ethical concerns" is not an available answer on this brief.

---

## Submission

- Markdown or PDF, 1,200–1,500 words.
- If you used an AI assistant, declare it in one line at the end: which tool, for what. Declared use is
  permitted; you will be asked to talk through your section 3 aloud.
- Submit by session 8.

---

**For:** Course 01 – AIAT 111 · Introduction to Artificial Intelligence and Applications
