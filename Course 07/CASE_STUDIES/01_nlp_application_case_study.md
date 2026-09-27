# Case Study 01: The chatbot that invented a refund policy
## Building a customer-service assistant after *Moffatt v. Air Canada*

**Course:** Course 07 — AIAT 121, Natural Language Processing
**Type:** Case-study analysis (official assessment instrument)
**Points:** 100, scaled to 10 of the course's 100
**Set:** session 74 · **Due:** session 78
**Effort:** one hour. 10 min reading · 15 min collecting numbers from your own notebook runs · 30 min writing · 5 min checking
**Length:** 1,200–1,500 words. Individual work.

---

## 1. The situation

### What happened

On 11 November 2022 Jake Moffatt's grandmother died, and he went to Air Canada's website to book a
flight to Toronto. The website's chatbot told him he could buy the ticket now and apply for the
airline's **bereavement fare within 90 days** of travel. Air Canada's actual policy, on another page
of the same website, said the opposite: bereavement fares cannot be claimed after travel. He booked,
applied, and was refused.

He took the airline to British Columbia's Civil Resolution Tribunal. Air Canada argued that the
chatbot was **"a separate legal entity that is responsible for its own actions."** The tribunal
called that "a remarkable submission" and rejected it.

| Fact | Figure |
|---|---|
| Decision | *Moffatt v. Air Canada*, 2024 BCCRT 149, **14 February 2024** |
| Finding | negligent misrepresentation; Air Canada "did not take reasonable care to ensure its chatbot was accurate" |
| Damages | **CA$650.88** — the difference between the fare he paid and the bereavement fare |
| Total with interest and tribunal fees | **CA$812.02** |
| The airline's position | the chatbot was a separate legal entity; the customer should have checked the policy page |

### The part that is not in the headline

The money is trivial. The holding is not: **the words a generative model produces on your website
are your words**, and a disclaimer that the customer should have read a different page was not a
defence. Nothing about the failure was exotic. A language model produced a fluent, specific,
confident sentence about a policy it had no way to check, and nobody had built the step that
checks it.

You met the case in `unit4-deep-learning-nlp/examples/05_gpt_openai_text_generation.ipynb`, which
uses it to ask where the safeguard belongs. The rest of this course supplies the numbers: what
decoding does to truth, what a checkpoint does off-domain, what Arabic costs, and how many test
questions it takes to believe an accuracy figure.

**Sources:** Civil Resolution Tribunal of British Columbia, *Moffatt v. Air Canada*, 2024 BCCRT 149,
14 February 2024 (the facts, the "separate legal entity" submission, the finding and the amounts);
American Bar Association, Business Law Today, *BC Tribunal Confirms Companies Remain Liable for
Information Provided by AI Chatbot*, February 2024; McCarthy Tétrault, *Moffatt v. Air Canada: A
Misrepresentation by an AI Chatbot*, 2024. The same facts appear in the notebook named above.

---

## 2. The decision you must make

You are the NLP lead at a **Saudi airline**. The board wants a bilingual — Arabic and English —
customer-service assistant on the website within ninety days, answering questions about fare rules,
refunds, baggage and rebooking. The airline's policies exist as 140 pages of PDF in both languages,
updated monthly. Most customers write in Saudi dialect, not Modern Standard Arabic. The board has
read about Air Canada and asked you, in writing, how you will make sure it does not happen here.

**Choose exactly one and defend it:**

- **A — A generative assistant.** A large language model answers in free text, with the policy
  documents in its prompt and a disclaimer under the chat window. You must state the pre-launch
  test that would have caught the Air Canada sentence, and what the disclaimer is worth after the
  tribunal's holding.
- **B — A retrieval-grounded assistant.** The model may only answer from policy passages a
  retrieval step returns; every answer quotes its source passage; when retrieval confidence is low
  the conversation goes to a human. You must state how retrieval is evaluated, who writes the gold
  answers, and what happens when the policy changes.
- **C — A classifier and approved answers.** An intent classifier routes each question to one of
  N answers written and signed off by the policy team; anything it cannot classify goes to a human.
  No text is generated. You must state how many intents, how you get labelled data in dialect, and
  what the customer loses.

There is no correct option. There are defensible arguments and indefensible ones, and the
difference is whether you brought numbers.

---

## 3. Evidence you must bring from this course

Your analysis must cite **at least three** of the following by notebook filename, with the number
from **your own run** (they will differ slightly from the figures quoted here, and where they do,
report yours). An analysis that argues from principle alone cannot pass Section 1 or Section 5.

| Notebook | What it gives you |
|---|---|
| `unit3-ml-for-nlp/examples/01_text_classification.ipynb` | Two classifiers score **100%** on 32 reviews. With 8 documents and 2 in the test set, the *same* pipeline scores **0% to 100%** across five splits, mean 60%. Spread by dataset size: 8 documents, sd 18.6 points; 32 documents, sd 2.2. A single accuracy number on a handful of test questions is noise. |
| `unit3-ml-for-nlp/examples/02_named_entity_recognition.ipynb` | spaCy finds 12 entities in a friendly paragraph. Lowercase the same text and it loses 2 (`apple`, `redmond`); ALL CAPS loses 3 and *invents* 2. You do not control how customers type. |
| `unit2-tokenization-morphology/examples/01_advanced_tokenization.ipynb` | An Arabic sentence of 71 characters — shorter than the 85-character English one — costs GPT-2 **67 tokens against 13**: 6.09 against 1.18 tokens per word, **×5.2**; BERT-base-uncased ×4.7. |
| `unit2-tokenization-morphology/enrichment/E4_retrieval_in_sixty_seconds.ipynb` | 72 README files → 370 chunks; TF-IDF retrieval scores hit@1 **71%**, hit@3 **100%** on seven queries — written by the person who built the index. Lexical retrieval cannot match "self-driving car" to "autonomous vehicle". Seven author-written queries are a smoke test, not an evaluation. |
| `unit4-deep-learning-nlp/examples/03_bert_advanced_usage.ipynb` | A sentiment checkpoint fine-tuned on movie reviews calls "The meeting is scheduled for Tuesday at 3pm." **POSITIVE (0.93)** and "Water boils at 100 degrees Celsius" NEGATIVE. The two Arabic sentences land in the 0.10–0.90 uncertain band (0.42, 0.37), tokenized **one letter per token**. A checkpoint carries its training data with it, and keeps answering off-domain without any error. |
| `unit4-deep-learning-nlp/examples/05_gpt_openai_text_generation.ipynb` | GPT-2 with greedy decoding spends **24 of 35** steps inside a repeated four-token phrase. At temperature 0.5 the top token has probability 0.601 and 8 tokens cover 90% of the mass; at 1.3 it has 0.042 and **3,055** tokens do. No setting of that knob makes a sentence true. |
| `unit5-applications-ethics/enrichment/E17_the_arabic_evaluation_gap.ipynb` | An English-trained BPE tokenizer spends **5.58** tokens per Arabic word against 1.13 per English word (×4.92); per meaning, ×3.31 — a 4,000-token window holds 178 of the sample sentences in Arabic against 590 in English. The English side is trained on this repository's own Markdown, so those English figures move as the repository changes; the Arabic side does not. MSA and dialect differ by **0.018** tokens per word: the tokenizer does not know what a dialect is. 117 Arabic words in the training corpus cut fertility on unseen MSA by 34%. |

---

## 4. Analysis questions

These have no single right answer. Answer all five inside the five sections in §5 — the mapping is
in the table there.

**Q1 — Where the wrong sentence came from.** Air Canada's answer was fluent, specific and false.
Using `05_gpt_openai_text_generation` (what decoding optimises) and `03_bert_advanced_usage` (what a
checkpoint does off its training domain), explain to the board why "the model made a mistake" is
not a bug report but the default behaviour of the component. Then say which of A, B and C changes
that *structurally* — makes the wrong sentence impossible to emit — and which only changes it
*statistically*.

**Q2 — The Arabic bill and the Arabic gap.** Using `E17` and `01_advanced_tokenization`, estimate
the token-cost multiplier and the context-window loss for Arabic against English for your chosen
model family. Then say what evaluation set you need for **Saudi dialect** specifically — `E17`
shows the tokenizer cannot tell dialect from MSA, and `unit5-applications-ethics/examples/01_bias_detection.ipynb`
names a benchmark built for exactly this gap — and who must write the gold answers (`E4`: not the
person who built the index).

**Q3 — The test that would have caught it.** Design the pre-launch evaluation: how many questions,
who writes them, what "correct" means for a fare rule (exact policy? any paraphrase? the right
passage?), and what the test size does to the number you report. `01_text_classification` gives you
the spread at 8, 16, 24 and 32 documents; say at what number of test questions you would believe
a 95% figure, and what you tell the board if the airline can only afford 100.

**Q4 — The safeguard and its price.** `05_gpt_openai_text_generation` lists four safeguards:
filter the output, restrict the model to retrieved documents, keep a human approval step, publish a
disclaimer. Rank them by cost, then by how much each would actually have prevented Moffatt. Say
whether the two rankings agree, and where a disclaimer stands after a tribunal has held that the
customer was not obliged to check a second page.

**Q5 — Your recommendation and its price.** Commit to A, B or C from §2. Argue the strongest case
*against* your own choice. Say what it costs the airline if you are wrong — in refunds, in a
tribunal, in customers who stop trusting the answer. Name the **role** that is accountable when the
assistant is wrong about a refund; "the model" is not a role. State what you measure in the first
thirty days after launch.

---

## 5. What you submit

One document, five sections, marked out of 100.

| Section | Points | Feeds from |
|---|---:|---|
| 1. Problem analysis | 20 | Q1, Q2 |
| 2. Solution design | 25 | Q1, Q4 |
| 3. Implementation plan | 25 | Q3, Q4 |
| 4. Evaluation | 15 | Q2, Q3 |
| 5. Recommendations, limits and ethics | 15 | Q5 |

### What a strong answer contains

This is a description of **properties**, not of content. Two students can recommend opposite things
and both score full marks.

- **A constraint the brief did not state.** The brief gives you ninety days, 140 pages of policy
  updated monthly, dialect-speaking customers and a bilingual requirement. A strong Section 1
  names something else that binds — the policy PDFs disagree between languages; the airline's
  legal team must sign every answer the assistant may give; the refund desk that receives
  escalations is open eight hours a day — and says how it was inferred.
- **Success defined as a number with a target**, never as "accurate" or "helpful". A metric on a
  named test set of a stated size, a threshold, and what happens when it is missed.
- **An alternative considered and rejected, with the reason.** A design that names only what it
  chose has not been designed.
- **A baseline that appears before the real model in the plan.** For this problem it is cheap and
  it is not zero: the existing FAQ page, or a keyword search over the policy PDFs (`E4` builds one
  in sixty seconds). If your assistant cannot beat the search box on your test set, there is no
  product in it.
- **Something that happens after launch.** A sample of conversations read by a human every week,
  a metric that moves when the policy changes, a kill switch, and the named role that receives the
  alert.
- **Two limitations that would genuinely make your proposal fail**, and what you would do about
  each. "LLMs hallucinate" stated without a number and a mitigation earns nothing.
- **Who is affected who never uses the system** — the customer who trusted the answer and cannot
  afford the tribunal, the agent whose job the assistant replaces, the Arabic speaker who gets a
  worse answer than the English speaker and never knows.
- **At least three references to this course's own material**, by filename, with your own numbers.

### Rules

- Submit markdown or PDF. Code is optional; if you include a snippet it must match your written
  design.
- Over the word count by more than 25% loses marks. Length is not the deliverable.
- If you used an AI assistant, declare it in one line at the end: which tool, for what. Declared
  assistance is permitted. You will be asked to walk through your Section 3 plan aloud.

---

## 6. Sources

- Civil Resolution Tribunal of British Columbia, *Moffatt v. Air Canada*, 2024 BCCRT 149,
  14 February 2024.
- American Bar Association, Business Law Today, *BC Tribunal Confirms Companies Remain Liable for
  Information Provided by AI Chatbot*, February 2024.
- McCarthy Tétrault, *Moffatt v. Air Canada: A Misrepresentation by an AI Chatbot*, 2024.
- Lewis, P. et al., *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*, NeurIPS 2020
  (arXiv:2005.11401) — the retrieval design behind option B, as cited in
  `unit4-deep-learning-nlp/examples/05_gpt_openai_text_generation.ipynb`.
- Kalai, A. T., Nachum, O., Vempala, S. S. & Zhang, E., *Why Language Models Hallucinate*, 2025
  (arXiv:2509.04664) — the argument that confident falsehood is structural, as cited in
  Course 10's `unit2-text-generation/examples/01_text_generation_gpt_models.ipynb`, if you use it
  for Q1.

**For:** Course 07 — AIAT 121
