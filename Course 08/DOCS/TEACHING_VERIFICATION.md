# Course 08 – Teaching Verification
## Everything we teach matters (conversation summary + checklist)

This document summarizes **what we decided to teach** and confirms that **every part of it matters** and is aligned with the 20-minute plan. Use it so you don’t have to re-ask: “Is this right? Is this enough?”

---

## 1. What the full conversation decided

| Topic | Decision |
|-------|----------|
| **Institution slides** | 23 slides match Units 1–4; Unit 5 has no slides. Slides = theory/objectives; **practicals** live in course notebooks. |
| **Course 08 gap** | Notebooks were thin (objectives + 1 code cell or no code). Other courses (05, 07) give real data, full pipeline, real outputs. |
| **Goal** | In **~20 min per notebook**, students get **theory + practical in real life** for each topic. |
| **Plan** | `20_MIN_NOTEBOOK_PLAN.md`: short theory (3–5 bullets), real-life (2–3 sentences), **multiple code cells** (imports → load → build → train → plot → evaluate), clear inputs/outputs, “we use X to do Y; instead of Z because …”, key takeaway, link to next. Run time &lt;15 min. |
| **Plots** | Every plot has **axis labels** (xlabel, ylabel), title, legend when relevant. If we print “before vs after” numbers, add a simple plot (e.g. bar chart). See **Plots and visualizations** in the plan. |
| **Already done** | `01_simple_neural_network`, `02_backpropagation_detailed`, `03_optimization_techniques` rewritten to the 20-min standard; plan updated with plot rules. |

---

## 2. What we’re teaching in each rewritten notebook (and why it matters)

### 01 – Simple Neural Network

| What we teach | Why it matters |
|---------------|----------------|
| **Objectives** | Build a feedforward NN with Keras, train on real data (MNIST), understand why we use a NN instead of hand-coded rules. | Core skill: first “real” training loop students run. |
| **Real life** | Digit recognition in postal sorting, forms, checks, captchas. | Students see where this is used in the world. |
| **“We use X instead of Z because”** | We use a **feedforward NN** to classify digits **instead of** hand-coded rules **because** the network learns features from data; we don’t hand-design them. | Explains the **design choice**; not just “run this code.” |
| **Theory (short)** | NN = layers → activation → loss → backprop → optimizer. Data flow: input → flatten → Dense → ReLU → Dense → Softmax. | Minimal theory needed to read the code. |
| **Code** | Real MNIST, normalize, build Sequential model, compile, fit (3 epochs), plot loss/accuracy (with axis labels), evaluate, 5 sample predictions. | Full pipeline; every step has a clear purpose. |
| **Summary** | “What you did” + “In real life you’d also…” + **“The main idea: …”** + **“Next: 02_backpropagation_detailed”**. | One clear takeaway and a clear next step. |

**Verdict:** Everything in this notebook supports one goal: *run a real training pipeline and understand why we use a NN for this task.* No filler.

---

### 02 – Backpropagation Detailed

| What we teach | Why it matters |
|---------------|----------------|
| **Objectives** | See how gradients flow backward, use GradientTape to compute gradients, understand why we use backprop instead of guessing weights. | Backprop is how every modern NN is trained; students see the mechanism. |
| **Real life** | Every time you train a NN (digits, images, NLP), the optimizer uses gradients from backprop to update weights. | Connects the notebook to all real training. |
| **“We use X instead of Z because”** | We use **backpropagation** (via GradientTape) to compute gradients **instead of** guessing/randomly changing weights **because** gradients tell us **in which direction** to change each weight to reduce the loss. | Explains why we don’t “guess” weights. |
| **Theory (short)** | Forward pass → loss; backprop = chain rule, gradients backward; optimizer: `new_weight = old_weight - lr * gradient`. | Just enough to follow the code. |
| **Code** | Small MNIST batch, one-layer model, GradientTape forward + loss, `tape.gradient`, inspect gradient shapes, one manual optimizer step, loss before/after, **bar chart** (loss before vs after). | Shows the math in code; plot makes “loss goes down” visible. |
| **Summary** | “What you did” + “In real life you’d also…” + **“The main idea: …”** + **“Next: 03_optimization_techniques”**. | One idea + link to how optimizers use these gradients. |

**Verdict:** Everything supports one goal: *see how gradients are computed and used for one update.* No filler.

---

### 03 – Optimization Techniques

| What we teach | Why it matters |
|---------------|----------------|
| **Objectives** | Compare SGD and Adam on the same task, see how optimizer choice affects loss curves, understand why we often use Adam instead of plain SGD. | Optimizer choice is one of the first hyperparameters students change in practice. |
| **Real life** | Every `model.compile(optimizer='adam', ...)` or training run uses an optimizer that uses backprop gradients to update weights. | Connects to real Keras/PyTorch usage. |
| **“We use X instead of Z because”** | We use **optimizers** (SGD and Adam) to update weights. We use **Adam** instead of plain **SGD** in many projects **because** Adam adapts the learning rate per parameter and usually converges faster and more reliably. | Explains a standard default (Adam). |
| **Theory (short)** | Optimizer = uses gradients to update weights; SGD = direct gradient; Adam = per-parameter adaptive rate (momentum + scaling). | Enough to interpret the comparison plot. |
| **Code** | MNIST subset (10k), two identical models, one trained with SGD and one with Adam (2 epochs each), **one plot**: SGD vs Adam train loss (with xlabel, ylabel, title, legend). | Direct comparison; plot is the main output. |
| **Summary** | “What you did” + “In real life you’d also…” + **“The main idea: …”** + **“Next: 04_perceptron_mlp_…”**. | One idea + link to next notebook. |

**Verdict:** Everything supports one goal: *compare two optimizers and see why Adam is often preferred.* No filler.

---

## 3. Checklist: “Does everything we teach matter?”

Use this when adding or reviewing a Course 08 notebook.

| Check | Required? | Where |
|-------|-----------|--------|
| **3 learning objectives** (what the student will do/understand) | Yes | Header |
| **“Where is this used in real life?”** (2–3 sentences) | Yes | Real life block |
| **“We use [X] to [do Y]. We use it instead of [Z] because [reason].”** | Yes | Markdown + at least one code comment |
| **Theory: 3–5 bullets** (no long paragraphs) | Yes | Theory block |
| **Inputs & Outputs** (what goes in, what comes out) | Yes | Dedicated section |
| **Multiple code cells** (not one giant cell) | Yes | 5–8 cells: imports → load → … → plot → evaluate |
| **Real or realistic data** (e.g. MNIST, subset) | Yes | So output is interpretable |
| **At least one plot** with **axis labels**, title, legend if needed | Yes | Plot cell(s) |
| **“After this cell you should see: …”** (expected output) | Recommended | After train/plot cell |
| **“We use N epochs here so it runs in ~X min; in real projects …”** | Recommended | Near training |
| **Summary: “What you did” (3 bullets)** | Yes | End |
| **“In real life you’d also: …”** (one line) | Yes | Summary |
| **“The main idea: …”** (one line) | Yes | Summary |
| **“Next: [notebook] shows …”** | Yes | Summary |
| **Prerequisites / environment** (e.g. run imports; see COLAB_SETUP) | Yes | Top (after objectives) |

If every row is “yes” (or “recommended” where we chose to add it), the notebook is aligned with what we agreed **matters**.

---

## 4. Flow: why this order matters

- **01** – Run a full pipeline (load → train → plot → evaluate). Students see **what** we do.
- **02** – Open the “black box”: **how** gradients are computed and used for one step (backprop).
- **03** – **How** we update weights: compare SGD vs Adam (optimizers use the gradients from 02).
- **04** – Setup and perceptron vs MLP (next in plan).

So we teach: **what** (pipeline) → **how** (backprop) → **how** (optimizer) → then setup/perceptron/MLP. Each step uses the previous one; nothing is isolated.

---

## 5. What’s in the plan (so you don’t have to re-ask)

- **20_MIN_NOTEBOOK_PLAN.md** – Structure (time blocks), “we use X instead of Z because,” multiple cells, rules, “what else helps,” order of work.
- **Plots and visualizations** – Axis labels, title, legend; visualize “before vs after” when we print those numbers; one main figure per idea.
- **PRACTICAL_ENHANCEMENT_ASSESSMENT.md** – Why Course 08 was thin vs 05/07 and what “real life” should mean (real data, full pipeline, visible outputs, context).
- **TEACHING_VERIFICATION.md** (this file) – What we teach in each rewritten notebook and that **everything we teach matters**.

---

## 6. Summary

- **Conversation:** We fixed “notebooks too thin” and “students don’t see what happens in real life” by: 20 min per notebook, real data, full pipeline, multiple cells, real-life context, “we use X instead of Z because,” clear inputs/outputs, plots with labels, key takeaway, link to next.
- **Rewritten so far:** 01 (simple NN), 02 (backprop), 03 (optimizers). Each has objectives, real life, theory, inputs/outputs, multiple code cells, real MNIST (or subset), plots with axis labels, summary with main idea and next.
- **Verification:** Every element in these notebooks supports the stated learning goal; there is no filler. The same checklist and plan apply to 04 and the rest of Course 08 so that **everything we teach keeps mattering**.
