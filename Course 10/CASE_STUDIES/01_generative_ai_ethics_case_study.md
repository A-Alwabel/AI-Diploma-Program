# Case Study 01: The watermark in the generated image
## Choosing an image-generation stack after *Getty Images v Stability AI*

**Course:** Course 10 — AIAT 124, Generative Artificial Intelligence
**Type:** Case-study analysis (official assessment instrument)
**Points:** 100, scaled to 10 of the course's 100
**Set:** session 108 · **Due:** session 112
**Effort:** one hour. 10 min reading · 15 min collecting numbers from your own notebook runs · 30 min writing · 5 min checking
**Length:** 1,200–1,500 words. Individual work.

---

## 1. The situation

### What happened

In February 2023 Getty Images sued Stability AI — in the United States and, separately, in the
High Court in London — alleging that Stability had copied millions of Getty photographs to train
Stable Diffusion. Part of Getty's evidence needed no expert: the **Getty watermark** appearing,
distorted, in images the model generated.

Judgment in the English case came on **4 November 2025**.

| Fact | Figure |
|---|---|
| Judgment | *Getty Images (US) Inc & Ors v Stability AI Ltd* [2025] EWHC 2863 (Ch), Mrs Justice Joanna Smith, 4 November 2025 |
| The primary copyright claim (copying during training) | **abandoned by Getty during the trial**, after it accepted there was no evidence the training had taken place in the United Kingdom |
| The secondary copyright claim (the model itself is an "infringing copy") | **dismissed**: "the model weights are not themselves an infringing copy" — the model does not store the works |
| The trade-mark claim (the watermarks in outputs) | **"limited infringements"** for "a small number of examples for certain iterations"; the wider claim under section 10(3) failed |
| Passing off | not established |

### The part that is not in the headline

Read the two findings together. A court held that the weights contain no copies of Getty's
photographs, **and** that some outputs reproduced Getty's mark closely enough to infringe it. Both
are true of the same model. "The model only learns statistics, it does not store images" survived
as law and failed as a description of what came out of the sampler. The case also turned on
something no engineer controls: where the training happened. The same model, trained on the same
data, would have faced a different claim in a different jurisdiction, and the United States action
was brought separately.

You met the case in `unit3-image-generation/examples/05_generating_ai_images_stylegan_dalle.ipynb`,
which asks what the watermark does to the "only statistics" argument, and in
`unit4-ethics-regulations/examples/01_generative_ai_ethics.ipynb`, which lists it among the open
questions. The rest of this course supplies the tools: what FID can and cannot see, what "we
removed your data" does to a trained model, how well a detector generalises, and what a chain of
generators does to reliability.

**Sources:** Courts and Tribunals Judiciary, *Getty Images v Stability AI*, judgment page
(the date, citation and judge); Latham & Watkins, *Getty Images v. Stability AI: English High Court
Rejects Secondary Copyright Claim*, November 2025 (the holdings quoted above); Squire Patton Boggs
and DLA Piper client notes of November 2025. The February 2023 filings and the watermark evidence are as described in
the notebook named above.

---

## 2. The decision you must make

You lead the creative-technology team at a **Saudi marketing agency**. Clients want campaign
imagery faster and cheaper; two have asked for "AI-generated" work by name; one — a bank — has
asked, in writing, whether the images you deliver could expose it to a claim. The agency owns a
library of 40,000 licensed stock photographs and every client's brand assets. You have one
workstation with a consumer GPU and a modest cloud budget.

The managing director wants a stack decision in writing within thirty days.

**Choose exactly one and defend it:**

- **A — Self-host an open-weights model** (the Stable Diffusion family) and fine-tune it on each
  client's brand assets. You must say what you know, and cannot know, about what the base model
  was trained on, and what test you run before the first delivery.
- **B — A closed API with a contractual indemnity.** You must read the indemnity as an engineer:
  what it covers, what it excludes, and what the bank's lawyer will ask that it does not answer.
- **C — Generate only from what you own or license:** a model trained or fine-tuned exclusively on
  the agency's licensed library and the client's assets, or a vendor that warrants the same. You
  must say what the library cannot produce and what that costs the creative team.
- **D — No generative imagery.** Stock, photographers, designers. You must say who pays for that,
  and what measurement would change your mind.

There is no correct option. There are defensible arguments and indefensible ones, and the
difference is whether you brought numbers.

---

## 3. Evidence you must bring from this course

Your analysis must cite **at least three** of the following by notebook filename, with the number
from **your own run** (they will differ slightly from the figures quoted here, and where they do,
report yours). An analysis that argues from principle alone cannot pass Section 1 or Section 5.

| Notebook | What it gives you |
|---|---|
| `unit3-image-generation/examples/05_generating_ai_images_stylegan_dalle.ipynb` | The comparison table: StyleGAN, open weights; DALL·E, closed, API only; Stable Diffusion, open weights on a consumer GPU (about 8 GB). "Open weights" is not "open data" and not "unrestricted use" — three separate things that fail separately. The 8-epoch anchor GAN (discriminator loss between 0.436 and 0.538, generator loss between 1.747 and 2.715 at the printed epochs) teaches the mechanism and nothing about data curation, which is where the lawsuit lived. |
| `unit1-generative-fundamentals/examples/10_evaluating_generative_models_fid_bleu.ipynb` | Fréchet distance: a held-out real set scores **0.06**, noisy 0.26, blurred 2.29, pure noise 3.82. The ordering FID is built to give — and a generator that **memorises its training set scores excellently**. FID is blind to the exact failure Getty put in evidence. |
| `unit4-ethics-regulations/examples/04_applying_ai_regulatory_guidelines_gdpr.ipynb` | Erasing one real person from the training data changed **0 of 193** predictions and moved the largest coefficient by **0.00235**. "The metrics did not move" is not evidence that erasure worked. Minimisation cost accuracy 77.6% → 74.1%; a consent register drawn independently of every column still produced visible attrition differences. |
| `unit4-ethics-regulations/examples/02_deepfake_detection.ipynb` | A detector trained against the course's own generator scores **98.4%** on held-out images from that generator — and **33.6%** of its calls land in the 0.2–0.8 undecided band. The notebook's calibration point: the Deepfake Detection Challenge winner scored 82.56% on the public set and **65.18%** on the unseen black-box set. A detector overfits its generator. |
| `unit4-ethics-regulations/examples/01_generative_ai_ethics.ipynb` | Dropping the protected column cut the predicted-rate gap from 81.9% to **13.4%**, cost 9.7 points of accuracy, and the attribute was still predictable at 66.0% against a 63.8% baseline. Removing a column removes your ability to audit, not the model's ability to discriminate. The copyright section names Getty v Stability and *The New York Times v OpenAI* as open questions. |
| `unit5-future-trends/examples/01_generative_ai_applications.ipynb` | Six stages at 90% each finish correctly **53.1%** of the time; two at 90% give 81.0%. The word-list quality gate scored an invented policy **2** and the accurate one **0**. A pipeline gets less reliable as it gets more ambitious, and a gate that counts vocabulary cannot check a fact — or a watermark. |

---

## 4. Analysis questions

These have no single right answer. Answer all five inside the five sections in §5 — the mapping is
in the table there.

**Q1 — What the model stores.** The court held the weights are not a copy; the outputs carried
Getty's mark. Reconcile the two for a non-lawyer using `10_evaluating_generative_models_fid_bleu`
(why a quality score cannot see memorisation) and the extraction result the notebook in
`unit3-image-generation` cites (Carlini et al., 2023). Then design the **regurgitation test** you
would run before the first delivery: how many prompts, matched against what, with what similarity
threshold, and the number at which the model fails.

**Q2 — Provenance is not a licence.** For each option A–D, write three sentences: what you *know*
about the training data, what you *can find out*, and what you *cannot*. Then read an indemnity
clause as an engineer: what does it transfer, what does it exclude (your fine-tuning data? your
prompts? trade-mark claims?), and what happens to it if the vendor loses its own case.

**Q3 — The client who leaves.** A client withdraws its brand assets from your fine-tuned model and
asks for written confirmation that its data is gone. Using `04_applying_ai_regulatory_guidelines_gdpr`
(0 of 193 predictions changed), say what "we removed your data" can honestly mean for a fine-tuned
generator, what you would have to do to mean it — retrain from the base, unlearn, purge backups and
logs — and what each costs.

**Q4 — Labelling and detection.** Campaign imagery generated by AI will have to be labelled;
`01_generative_ai_ethics` records the EU AI Act's transparency duty for deployers of synthetic
content, and a Saudi client may have its own policy. Using `02_deepfake_detection` (98.4% in
distribution, 33.6% undecided, 65.18% off-distribution), argue whether *detection* or *provenance
metadata attached at generation* is the reliable path, and write the sentence you say to a client
who asks for "undetectable".

**Q5 — Your recommendation and its price.** Commit to A, B, C or D from §2. Argue the strongest
case *against* your own choice. Say what it costs the agency if you are wrong — a claim, a lost
client, a campaign pulled — and name who is affected who never uses the system: the photographer
whose work is in the training set, the stock agency, the audience that cannot tell.

---

## 5. What you submit

One document, five sections, marked out of 100.

| Section | Points | Feeds from |
|---|---:|---|
| 1. Problem analysis | 20 | Q1, Q2 |
| 2. Solution design | 25 | Q2, Q4 |
| 3. Implementation plan | 25 | Q1, Q3 |
| 4. Evaluation | 15 | Q1, Q4 |
| 5. Recommendations, limits and ethics | 15 | Q5 |

### What a strong answer contains

This is a description of **properties**, not of content. Two students can recommend opposite things
and both score full marks.

- **A constraint the brief did not state.** The brief gives you a bank's written question, a
  40,000-image library, a consumer GPU and thirty days. A strong Section 1 names something else
  that binds — the library's licence may not permit training; the client's assets include people
  who never consented to be synthesised; a judgment in London binds nobody in Riyadh — and says
  how it was inferred.
- **Success defined as a number with a target**, never as "safe" or "high quality". A regurgitation
  rate on a named prompt set, a threshold, and what happens when it is exceeded.
- **An alternative considered and rejected, with the reason.** A design that names only what it
  chose has not been designed.
- **A baseline that appears before the generator in the plan.** For this problem it is the
  agency's current cost and turnaround per image with stock and designers. If the generator cannot
  beat that on cost *after* the review step you add, there is no product in it.
- **Something that happens after the first delivery.** A regurgitation test on every model
  update, a provenance record per image, a takedown route, and the named person who receives a
  claim.
- **Two limitations that would genuinely make your proposal fail**, and what you would do about
  each. "The law is unclear" is true of every project in this field and earns nothing on its own.
- **Who is affected who never uses the system** — named, not gestured at.
- **At least three references to this course's own material**, by filename, with your own numbers.

### Rules

- Submit markdown or PDF. Code is optional; if you include a snippet it must match your written
  design.
- Over the word count by more than 25% loses marks. Length is not the deliverable.
- This brief is teaching analysis, not legal advice; say so in your document if a client would
  read it.
- If you used an AI assistant, declare it in one line at the end: which tool, for what. Declared
  assistance is permitted. You will be asked to walk through your Section 3 plan aloud.

---

## 6. Sources

- *Getty Images (US) Inc & Ors v Stability AI Ltd* [2025] EWHC 2863 (Ch), 4 November 2025 — the
  judgment page at judiciary.uk carries the date, citation and judge.
- Latham & Watkins, *Getty Images v. Stability AI: English High Court Rejects Secondary Copyright
  Claim*, November 2025 — the holdings on secondary infringement, trade marks and the abandoned
  primary claim.
- Squire Patton Boggs, *Getty Images (US) Inc (and others) v Stability AI Limited*, November 2025;
  DLA Piper, *Getty Images v Stability AI: the UK High Court decision offers guidance...*,
  November 2025.
- Carlini, N. et al., *Extracting Training Data from Diffusion Models*, 2023 (arXiv:2301.13188) — the
  extraction result cited in `unit3-image-generation/examples/05_generating_ai_images_stylegan_dalle.ipynb`.
- Parmar, G., Zhang, R. & Zhu, J.-Y., *On Aliased Resizing and Surprising Subtleties in GAN
  Evaluation*, CVPR 2022 — the FID-pipeline dependence cited in
  `unit1-generative-fundamentals/examples/10_evaluating_generative_models_fid_bleu.ipynb`.

**For:** Course 10 — AIAT 124
