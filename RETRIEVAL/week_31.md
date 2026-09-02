# Cumulative Retrieval Quiz — Week 31

**Programme week 31 of 35 · Course 11 — AIAT 125 (AI Model Deployment), Units 3–4.**
**Taken in session 123, in the final 15 minutes.**

---

**How this works**

- **15 minutes, in class, at the END of the session.** 7 minutes to answer, then 8 minutes in which
  your instructor works the correct answers aloud.
- **Not graded.** No mark from this paper reaches your course grade.
- **Ten items.** Three on this week and last week, three from about a month ago, four from earlier in
  the programme.
- Write the **letter only**. Closed book. One best answer per item.

---

## Part A — This week and last week (Course 11, AI Model Deployment)

### Item 1
Unit 4 opened on the "works on my machine" problem. What does **Docker** provide for ML deployment?

A) Rescheduling a failed container onto a healthy node
B) Identical images from two builds of the same Dockerfile
C) Portability of the platform, not just the runtime
D) Containerization for a consistent runtime environment

---

### Item 2
Unit 4's analogy ran: Dockerfile = recipe, image = the baked cake, container = serving a slice. What
is the difference between a Docker **image** and a Docker **container**?

A) The image is a fixed template; a container is one running instance of it
B) The container is the stored artifact; the image is the copy loaded into memory
C) They are two names for the same artifact at two points in the build
D) An image runs on the build host; a container is what runs on a remote host

---

### Item 3
Unit 3 attached a target-tracking policy to a hosted endpoint: minimum 1 instance, maximum 10, scale
when invocations per instance pass 1000 per minute. What does **auto-scaling** do?

A) It retrains the served model when monitored accuracy drops
B) It adjusts the batch size the endpoint uses, to keep each response inside the budget
C) It adds or removes compute instances as the incoming traffic rises and falls
D) It rescales gradients during training so that large updates do not destabilise it

---

## Part B — About a month ago (Courses 10 and 09)

### Item 4 — Course 10, Generative AI
Two image generators are scored with **FID** inside one fixed, documented pipeline. Model A scores
8.0 and Model B scores 12.0. Which reading of that result is correct?

A) Model A is both better and more diverse than B, since FID's covariance term is what penalises a generator that has lost diversity.
B) Model A fits this pipeline's feature distribution better — but FID also scores well a model that memorised the training set.
C) The 4-point gap can be compared directly against FID values published in papers, since FID is a standardised metric.
D) Model A's images are sharper, since FID computes a per-image sharpness score and averages it over the generated set.

---

### Item 5 — Course 10, Generative AI
Unit 2 contrasted a decoder-only model with an encoder-only one. What is the key architectural
difference between **GPT** and **BERT**?

A) GPT is built from convolutions, while BERT is built entirely from attention layers
B) BERT generates text one token at a time; GPT scores a finished sentence
C) They share one architecture and differ in the corpus each was trained on
D) GPT attends left-to-right for generation; BERT reads context in both directions

---

### Item 6 — Course 09, Reinforcement Learning
Unit 5 compared a model-free agent with one that learns a model of the environment. What is the key
advantage of **model-based RL**?

A) A learned model lets the agent plan or replay simulated steps, so fewer real ones are needed
B) It removes the need to interact with the real environment, since the model supplies all of the data
C) It reaches a higher final reward than a model-free agent given the same training budget
D) It works without function approximation, so a table suffices for large state spaces

---

## Part C — Earlier in the programme

### Item 7 — Course 03, Mathematics and Probability for ML
Unit 1 computed the same two-layer transformation of the same data two ways: Route A as
`(X @ W1) @ W2`, using 8,510,592 scalar multiplications, and Route B as `X @ (W1 @ W2)`, using
1,191,040. The largest disagreement between the two outputs is **1.33e-14**. What does this establish
about a two-layer network with **no activation function** between the layers?

A) Route B is cheaper because it drops the hidden layer, so it returns an approximation.
B) The 1.33e-14 disagreement shows the two routes compute different functions, so the order the products are taken in matters.
C) The two layers can be replaced by one layer with weight matrix `W1 @ W2` without changing the function computed.
D) The second layer re-weights the first layer's outputs, so stacking the two adds expressive power a single layer lacks.

---

### Item 8 — Course 02, Python for Artificial Intelligence
Unit 3's diagnosis system is given a patient with fever, cough and fatigue, and prints:

```
disease         prevalence  prior (norm.)  P(symptoms|d)   posterior
Common Cold         15.0%          68.2%           5.6%       19.6%
Flu                  5.0%          22.7%          50.4%       58.9%
COVID-19             2.0%           9.1%          45.9%       21.5%
```

Common Cold is by far the most prevalent of the three, yet it finishes last. Why?

A) Renormalising the three prevalences over one another pushes the largest of them below the others.
B) Common Cold has no listed probability for fatigue, so the system skips it in the product.
C) The posterior follows the highest single symptom probability, and Flu's fever figure is 90%.
D) Bayes multiplies prior by likelihood, and P(symptoms | Cold) = 5.6% is nine times below Flu's.

---

### Item 9 — Course 08, Deep Learning
On IMDB reviews padded to 100 tokens, a `SimpleRNN` reaches **0.544** best validation accuracy and an
**LSTM** of the same width reaches **0.776**. Where does the LSTM's advantage come from?

A) It has fewer parameters than a `SimpleRNN` of the same width, so it needs less data to train.
B) Its gates and cell state add a path along which the gradient can be carried back many steps.
C) It reads all 100 tokens in parallel instead of one at a time, so early words are not forgotten.
D) It reads each review backwards as well as forwards, so early words are seen last.

---

### Item 10 — Course 05, Scalable Data Science
Unit 2 profiled two columns of the same 891-row Titanic manifest. `Age` printed a skew of **0.53** and
a median near **26**; `Fare` printed a skew of **4.79**, with most passengers in the first histogram
bin and a few tickets reaching **512** pounds. A colleague's report quotes one "average" per column.
What does the profiling step tell you to do, and why?

A) Report `Fare` by its median and quartiles and say the column is skewed, because a single mean describes almost nobody in that shape.
B) Report the mean for both columns, because the mean uses all the rows while the median keeps just the middle one.
C) Drop the tickets near 512 pounds as outliers first, because the mean of `Fare` becomes a fair summary once that tail is gone.
D) Standardise both columns to mean 0 and standard deviation 1 first, because scaling removes the skew and makes the averages comparable.

---

**End of quiz — put your pen down and follow the worked answers.**
