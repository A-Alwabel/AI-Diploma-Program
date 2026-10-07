# Retrieval Quiz — Week 27

**Week 27 of 35 · Course 10 — AIAT 124 (Generative Artificial Intelligence)**

- **15 minutes, in class, at the end of the session.** About 7 minutes to answer, about 8 minutes for your instructor to work the answers.
- **Not graded.** Nothing you write here is collected, and nothing counts towards your course grade.
- **The answers are worked immediately afterwards,** in the same session — being wrong now and corrected now is the point.
- **Ten questions, one letter each.** Some are from this week; some are from earlier in the programme, on purpose.

---

### Question 1

A teammate reruns Unit 1's side-by-side experiment with a new random seed, and this time **logistic regression edges out Gaussian Naive Bayes** on the held-out split. The team is choosing a model for a spam filter that must also flag mail unlike anything it has seen before, and the teammate says the rerun settles it in favour of logistic regression. Which piece of lesson evidence decides the question?

A) The right-hand panel: far from its boundary, logistic regression still answers confidently — it stored no picture of where data lives — so an accuracy swing does not make it a model that can flag unfamiliar mail.  
B) The accuracy printout: the model that scores higher on the held-out split has learned the data better, so a rerun that puts logistic regression ahead settles the choice in its favour for this filter as well.  
C) The left-hand panel: the Gaussian model's invented points land on top of the real ones, which shows that a generative model will also be the more accurate classifier once the random seed is held fixed across reruns.  
D) The probability field in the right-hand panel: an uncertain p(y|x) carries the same information as a low p(x), so logistic regression already flags unfamiliar mail without modelling the data distribution.  

---

### Question 2

Two loss readouts printed by Unit 1's GAN notebook:

```
2-D toy run   — Final G loss: 0.6610   D loss: 1.3927
MNIST run     — Epoch 1/5 — D_loss=0.8774  G_loss=1.4142
                Epoch 5/5 — D_loss=0.5101  G_loss=2.8917
```

A classmate says the 2-D run is the one in trouble, because its discriminator posts the larger loss. Which reading of the two logs is right?

A) The 2-D run is the one in trouble: a discriminator posting a larger loss than its generator has lost the game and stopped teaching it anything, and the repair is extra D updates per G step until D's loss falls back below G's.  
B) Both runs are healthy: the MNIST discriminator's falling loss shows it is learning the digits, and a generator loss that climbs to 2.8917 simply means G is now being graded by a stricter judge, which is how it improves.  
C) The 2-D run sits at the balance point — a D loss near 1.39 means D cannot tell real from fake — while the MNIST trend is the one to watch: D's loss falls as G's rises, and a D that wins outright starves G of gradient.  
D) The MNIST run has mode-collapsed: a generator loss that climbs while D's falls is the signature of G producing one output over and over, which the discriminator then learns to reject with growing confidence.  

---

### Question 3

Course 09 Unit 5 introduces hierarchical RL (the options framework). Which difficulty is it aimed at?

A) Continuous action spaces, where the greedy max over actions can no longer be taken by enumerating them  
B) Long-horizon tasks, where a flat policy has to chain hundreds of primitive steps to reach a reward  
C) Coordination between several agents that share one environment  
D) Sample efficiency, by replaying remembered transitions between real steps in the environment  

---

### Question 4

In the lesson's worked example, a trained digits classifier is converted with a single library call and no retraining. Measured on the same laptop CPU: stored size **70.2 KB → 22.2 KB** (**3.2×** smaller), accuracy **96.7%** before and after, and latency **0.228 → 0.360 ms/batch** — the converted model runs **1.6×** slower. Name the technique and the property of the model it modified.

A) Pruning — the number of surviving weights, with the smallest ones zeroed out so the file has fewer values to hold  
B) Distillation — the architecture, with a smaller student trained to match the 96.7% teacher's soft outputs  
C) ONNX export — the file format, so the model runs outside PyTorch, which is also why inference got slower in the new runtime  
D) Quantization — the precision each weight is stored at, FP32 down to INT8, with a scale and zero-point kept per layer  

---

### Question 5

Course 08 Unit 4 trains a standard autoencoder and a variational autoencoder (VAE) on the same images. What does the VAE do that the plain autoencoder does not?

A) It compresses each input to a shorter code, which is what lets the decoder rebuild the image  
B) It trains encoder and decoder as two networks competing against each other  
C) It scores each input by how far its reconstruction sits from the original, and flags the gap  
D) It encodes each input to a distribution and samples from that, so new points can be drawn  

---

### Question 6

Unit 1's value-iteration notebook reports that its 3x3 grid world (gamma = 0.90; -1 for an ordinary step, +10 for entering the goal, -10 for entering the pit) **converged in 5 sweeps**, printing:

```
State values:              Greedy policy:
  4.58   6.20   8.00         →   →   ↓
  6.20   8.00  10.00         →   →   ↓
  P     10.00   G            P   →   G
```

Look at the **bottom-row tile between the pit and the goal**. It reads **10.00** — as much as the goal reward itself, and more than the 8.00 in the top-right corner — although stepping left from it lands in the -10 pit. A classmate concludes the pit must have been left out of that tile's backup. What actually happened in the code?

A) The -10 is multiplied by gamma = 0.90 once per sweep, so by the time the 5 sweeps are over it has shrunk too far to pull the tile below the 10.00 that the goal side offers.  
B) Four targets were computed and the largest kept: stepping right enters the goal for +10 with no future to discount, so 10.00 wins and the -10 target loses the comparison.  
C) The pit is in `TERMINAL_STATES`, so the sweep's `continue` skips it and `transition(7, 'left')` therefore returns no -10 for this tile's backup.  
D) The four targets are averaged rather than maximised, and the right-hand move into the goal lifts the mean far enough to cancel the single -10 that the pit contributes.  

---

### Question 7

The Dask lesson's per-operation table on the 14,015-flow CIC-IDS2017 sample reads:

```
Filter   pandas 0.0005 s | Dask 0.0105 s -> faster here: pandas
Sort     pandas 0.0007 s | Dask 0.0094 s -> faster here: pandas
```

Its closing note adds that pandas was only in the race because the code read **5 of the file's 79 columns**, and that the 708 MB original is about **165x** this sample. A teammate reads the table as proof that Dask is simply a slower pandas. Which conclusion do the printed timings and the note together support?

A) Dask lost because 14,015 rows are too few to spread across cores; with more cores on the same sample, parallel partitions would pull the 0.0105 s filter below pandas's 0.0005 s  
B) Dask lost on filter and sort but gains on operations that move rows between partitions, such as a merge or a high-cardinality groupby, so the ranking depends on which operation you time  
C) Dask's case is size, not speed: once a file is too big to materialise, `dd.read_csv` still works partition by partition where `pd.read_csv` fails, and this sample cannot show that  
D) Dask lost because reading 5 columns is cheap; requesting the full 79 would let Dask parse the columns in parallel and overtake pandas even on this sample  

---

### Question 8

In the same Dask lesson two consecutive calls behaved differently. `df_dask.head()` printed five real BENIGN flows straight away, but `df_dask['Flow Duration'].mean()` printed

```
<dask_expr.expr.Scalar: expr=(...)['Flow Duration'].mean(), dtype=float64>
   ^ that is a task graph, not a number
```

For comparison, `pd.read_csv` had already returned in **0.01 s** with all **14,015** rows in memory. Why did `head()` hand back rows while `mean()` handed back an object?

A) `head()` needs the first partition alone, so Dask reads just that one and returns real rows; `mean()` needs each of the four partitions, so it stays a graph node until `.compute()` runs it  
B) `head()` is served from rows that `dd.read_csv` loaded during its 0.003 s open; `mean()` ignores those rows because a Scalar result is recomputed from disk on each `.compute()`  
C) `head()` is not a reduction, so it returns a pandas object; `mean()` is a reduction whose value has been computed but is stored as a Scalar until `.compute()` casts it to float64  
D) `head()` fits inside Dask's per-partition memory budget, so it runs at once; a mean across four 1 MB partitions would exceed that budget, so Dask defers it until it can spill partitions to disk  

---

### Question 9

In the knowledge-representation lesson, `classify_animal` returned `is a fish` for the whale and the printout marked it `WRONG`. After the repair the same printout read `is a mammal`, and the heading said the function's code was untouched. Which part of the knowledge-based system was changed to get the right answer?

A) The rule store: `breathes air -> is a mammal` was inserted at the front of `animal_kb.rules`, and the old loop reached it first  
B) The inference loop: `classify_animal` was rewritten so that it tests `breathes air` before it tests `lives in water`  
C) The training data: the whale's row was relabelled `mammal` and the classifier was refitted on the four observed animals  
D) The fact table: an index on the fact `lives in water` was rebuilt so that a lookup for the whale returned mammal instead of fish  

---

### Question 10

The Unit 1 libraries notebook timed the doubling of 1,000,000 numbers twice. A one-shot timing cell printed:

```
   Python list comprehension :    11.05 ms
   NumPy, whole array at once:     0.71 ms
   Speed-up measured here    :     15.5x

Against the "100x faster" line in the Part 2 text above:
   this run measured 15.5x - well short of 100x.
```

The next cell re-timed six array sizes, keeping the best of three trials after a warm-up, and closed with:

```
Smallest N (10):        NumPy is SLOWER (0.5x)
Largest N (1,000,000): NumPy is 62x faster
```

A teammate wants to vectorise a helper that is called thousands of times per second on arrays of about ten values, and quotes the 62x as the gain to expect. Which printed line actually bears on that helper, and what does it say?

A) `Largest N (1,000,000): NumPy is 62x faster` — the compiled loop is the same code at any N, so the factor carries over to ten values  
B) `Smallest N (10): NumPy is SLOWER (0.5x)` — on ten values the per-call setup cost is the whole job, so the plain list stays ahead  
C) `this run measured 15.5x` — one honest measurement on this machine, so that is the realistic gain for the helper to expect  
D) The Part 2 text's `100x faster` — the 15.5x and 62x were pulled down by timing noise, so the tutorial figure is the safer planning estimate  

---
