# Case Study 01: The balloon controller that worked, and the company that closed
## Deciding whether reinforcement learning should staff an emergency dispatch centre

**Course:** Course 09 — AIAT 123, Reinforcement Learning
**Type:** Case-study analysis (official assessment instrument)
**Points:** 100, scaled to 10 of the course's 100
**Set:** session 96 · **Due:** session 101
**Effort:** one hour. 10 min reading · 15 min collecting numbers from your own notebook runs · 30 min writing · 5 min checking
**Length:** 1,200–1,500 words. Individual work.

---

## 1. The situation

### What happened

A Loon superpressure balloon has no engine and no rudder. It can only change altitude — pump air in
to sink, pump it out to rise — and ride whatever wind blows at that height. Keeping one balloon
within reach of a ground station for weeks is a sequential decision problem with a partially
observed state, and in December 2020 a team from Google Brain and Loon published a reinforcement
learning controller for it in *Nature*.

| Fact | Figure |
|---|---|
| Paper | Bellemare et al., *Autonomous navigation of stratospheric balloons using reinforcement learning*, *Nature* **588**, 77–82, published **2 December 2020** |
| Field test | a **39-day** controlled experiment over the Pacific; the notebooks date it 17 December 2019 to 25 January 2020 |
| Flight hours compared | **2,884** hours under the learned controller against **7,475** under Loon's hand-tuned `StationSeeker` at the same station |
| Time within 50 km of the station | **79%** against **72%** |
| Power used for altitude control | **29 W** against **33 W** |
| The baseline it beat | `StationSeeker`, tuned over more than **150,000** flight hours — not a strawman |
| How it was trained | entirely in simulation, from historical wind data with procedural noise added so the controller would not learn the simulator's quirks |

Seven weeks after the paper, on **21 January 2021**, Loon's chief executive Alastair Westgarth
announced that the company was winding down: *"we haven't found a way to get the costs low enough
to build a long-term, sustainable business."* The controller had worked. The business had not.

### The second case, and the four safeguards

The same course puts a second deployed controller next to Loon's. In August 2018 DeepMind and
Google described an RL agent in **direct control** of data-centre cooling, reporting *"consistent
energy savings of around 30 percent on average"*. The engineering around the agent is the part
worth studying: operators *"can choose to exit AI control mode at any time"*; every proposed action
is *"vetted against an internal list of safety constraints defined by our data centre operators"*,
then checked again by the local control system; and for every candidate action the agent
*"calculates its confidence that this is a good action. Actions with low confidence are eliminated
from consideration."*

### The part that is not in the headline

Loon's result was a technical success by a metric the engineers chose — 50 km, 79% against 72% —
and that metric was never the one the business was decided on. The cooling agent's 30% is the
number everyone quotes, and it was only deployable because of the safeguards nobody quotes. Both
cases are in `unit1-rl-fundamentals/examples/01_mdp_example.ipynb`,
`unit3-deep-rl/examples/01_dqn_implementation.ipynb` and
`unit5-applications/examples/03_resource_optimization.ipynb`, where the same problem — provision
capacity against a demand that rises and falls through the day — is solved on a real emergency-call
log.

**Sources:** Bellemare, M. G., Candido, S., Castro, P. S., Gong, J., Machado, M. C., Moitra, S.,
Ponda, S. S. & Wang, Z., *Nature* 588, 77–82, 2 December 2020 (the 39-day experiment; the flight
hours, 50 km figures and power figures are as reported in the paper and reproduced in the notebooks
above); TechCrunch, *Alphabet is shutting down Loon connectivity firm*, 21 January 2021 (the Westgarth quotation);
DeepMind, *Safety-first AI for autonomous data centre cooling and industrial control*,
17 August 2018 (the 30% figure and the safeguard quotations).

---

## 2. The decision you must make

You advise the **emergency dispatch centre of a Saudi region**. Every three hours a duty officer
decides how many ambulance crews to keep on shift. Too few and calls wait; too many and crews sit
idle at a cost the region's budget office reads every month. Three years of call logs exist, at
the same shape as the county log in `unit5-applications/examples/03_resource_optimization.ipynb`.
A vendor has offered "an AI agent that learns the optimal staffing policy". The fire chief has
said, in a meeting you attended: *"I am not letting software decide how many crews I have tonight."*

The director wants one recommendation from you, in writing, within a month.

**Choose exactly one and defend it:**

- **A — An RL agent in direct control**, wrapped in safeguards of the kind Google used. You must
  write the reward in one line, name the four safeguards, and say what the chief can switch off.
- **B — An RL agent in advisory or shadow mode.** The agent proposes; the duty officer decides;
  every proposal and decision is logged and compared. You must say how long shadow mode runs,
  what number ends it, and what happens if the officer always overrides.
- **C — No learning.** A scheduling model — a demand curve per block and a fixed rota fitted to
  it, or a linear programme over the historical demand. You must say what the learned policy in
  `03_resource_optimization` beat and why your model would not lose to it.
- **D — Do not do it.** Keep the duty officer's judgement and spend the money on something else.
  You must say who pays for that, and what measurement would change your mind.

There is no correct option. There are defensible arguments and indefensible ones, and the
difference is whether you brought numbers.

---

## 3. Evidence you must bring from this course

Your analysis must cite **at least three** of the following by notebook filename, with the number
from **your own run** (they will differ slightly from the figures quoted here, and where they do,
report yours). An analysis that argues from principle alone cannot pass Section 1 or Section 5.

| Notebook | What it gives you |
|---|---|
| `unit1-rl-fundamentals/examples/01_mdp_example.ipynb` | Loon's problem written down as five parts — states, actions, rewards, transitions, policy — before anything was trained. The 50 km in the reward is a decision, not a fact about the sky. On the toy grid a four-step rollout returns **4.7**; change the trap penalty and the policy changes with it. |
| `unit5-applications/examples/03_resource_optimization.ipynb` | Real demand: **11,688** three-hour blocks; the busiest block (15–18) averages **2.88** calls against **0.66** in the quietest, a **4.4×** spread no fixed crew level can be right for. On 3,507 held-out blocks the learned Q-table policy costs **−0.509** per block against **−0.755** for the best fixed crew level (a 33% saving), **−1.102** for always-maximum crew, **−2.061** for always-minimum, and **−0.466** for the hindsight reference. Every count is on a 1-in-27 sample of the real volume. |
| `unit5-applications/examples/01_rl_applications.ipynb` | The suitability checklist: resource optimisation scores 4/4, static image classification 1/4 — and nothing in it was measured; every "no" is a judgement you may argue with. Two exit rules: if your action does not change the state, use a bandit; if you are choosing a fixed allocation under known constraints, use optimisation. |
| `unit3-deep-rl/examples/01_dqn_implementation.ipynb` | CartPole DQN: average reward **29.0** at episode 0, **66.1** at episode 270, with ε still **0.257** — a quarter of the actions in that average were random. DQN needs a fast simulator: 50 million Atari frames is about 38 days of game time per game. Loon needed a simulator because that much real flight was impossible. |
| `unit3-deep-rl/examples/05_training_evaluation_monitoring.ipynb` | The well-tuned agent's training curve ended at **0.498** and its greedy evaluation scored **0.726**; the badly-tuned agent scored **0.040** — and had the *lower* standard deviation (0.099 against 0.500), because a run that always fails has no spread. Never read variance without the mean beside it. |
| `unit4-exploration-exploitation/examples/04_comparing_exploration_methods.ipynb` | One seed: Thompson 702, UCB 638, Boltzmann 546, ε-greedy 525. The "luck" column — measured minus expected — is **+56.3** for UCB and **−35.5** for Boltzmann. One seed cannot rank close strategies. |

---

## 4. Analysis questions

These have no single right answer. Answer all five inside the five sections in §5 — the mapping is
in the table there.

**Q1 — Is it an RL problem at all?** Apply the checklist in `01_rl_applications` to crew
provisioning, then apply its two exit rules. Does tonight's staffing decision change tomorrow's
demand? Are the constraints known? Say which of A–D the checklist supports, and why the 33% saving
in `03_resource_optimization` does not settle it: the sample is 1-in-27 of the real volume, the test
slice is the same county and the same era as the training slice, and the reference it lost to
(**−0.466**) was computed with hindsight.

**Q2 — The reward is a policy decision.** Loon paid `r = 1` inside a 50 km ring. Write the dispatch
centre's reward in one line. Name what it prices — an idle crew-hour against a call that waits —
and who should set that ratio; it is not the engineer. Predict the behaviour a naive version
produces (`unit1-rl-fundamentals/examples/06_solving_rl_problems_states_actions_rewards.ipynb`:
a strong agent finds the exploit in a bad proxy faster than a weak one).

**Q3 — Evidence before equipment.** Loon trained in a deliberately noisy simulator and only then
flew; Google's agent ran behind four safeguards. List what you would require before any policy
touches a real roster: where the simulator comes from (three years of logs — and which years),
how many seeds (`05_training_evaluation_monitoring`, `04_comparing_exploration_methods`), how long
the shadow period is, and the rule that lets the chief exit. Be prepared to defend the item the
vendor will want to cut.

**Q4 — It worked, and it was still shut down.** Loon's controller beat a 150,000-hour baseline and
the company closed seven weeks later. Separate the *technical* success criterion (the reward) from
the *business* one for the dispatch centre. Name the number the chief and the budget office will
actually decide on — response time at the 90th percentile? idle crew-hours per month? — and how you
would measure it in the first ninety days, against what baseline.

**Q5 — Your recommendation and its price.** Commit to A, B, C or D from §2. Argue the strongest
case *against* your own choice, say what it costs the region if you are wrong — a late ambulance
is not a lost reward — and state what evidence, within ninety days, would make you reverse it.

---

## 5. What you submit

One document, five sections, marked out of 100.

| Section | Points | Feeds from |
|---|---:|---|
| 1. Problem analysis | 20 | Q1, Q2 |
| 2. Solution design | 25 | Q2, Q3 |
| 3. Implementation plan | 25 | Q3 |
| 4. Evaluation | 15 | Q4, Q1 |
| 5. Recommendations, limits and ethics | 15 | Q5 |

### What a strong answer contains

This is a description of **properties**, not of content. Two students can recommend opposite things
and both score full marks.

- **A constraint the brief did not state.** The brief gives you three years of logs, a duty
  officer, a budget office and a chief who has said no. A strong Section 1 names something else
  that binds — crews cannot be added at 03:00 even if the policy asks; a Ramadan month looks like
  no other month in the log; the log records dispatches, not the calls that were never answered —
  and says how it was inferred.
- **Success defined as a number with a target**, never as "optimal staffing". A metric the chief
  recognises, a threshold, and what happens when it is missed.
- **An alternative considered and rejected, with the reason.** A design that names only what it
  chose has not been designed. "No learning" is a full-credit design if it is specified as
  concretely as any other.
- **A baseline that appears before the agent in the plan.** For this problem the baseline exists
  already: the duty officer's decisions for the last three years, scored with the same reward. If
  your agent cannot beat the officer in shadow mode, it has no product in it.
- **Something that happens after deployment.** A monitor on the demand distribution, a rule for
  retraining when the county changes, a rollback to the rota, and the named person who receives
  the alert.
- **Two limitations that would genuinely make your proposal fail**, and what you would do about
  each. "RL needs a lot of data" is true of every RL project ever written and earns nothing.
- **Who is affected who never uses the system** — the patient whose ambulance was the one the
  policy decided not to staff, the crew sent home on the policy's advice, the duty officer whose
  judgement is now a number to be overridden.
- **At least three references to this course's own material**, by filename, with your own numbers.

### Rules

- Submit markdown or PDF. Code is optional; if you include a snippet it must match your written
  design.
- Over the word count by more than 25% loses marks. Length is not the deliverable.
- If you used an AI assistant, declare it in one line at the end: which tool, for what. Declared
  assistance is permitted. You will be asked to walk through your Section 3 plan aloud.

---

## 6. Sources

- Bellemare, M. G. et al., *Autonomous navigation of stratospheric balloons using reinforcement
  learning*, *Nature* 588, 77–82, 2 December 2020. doi:10.1038/s41586-020-2939-8.
- TechCrunch, *Alphabet is shutting down Loon connectivity firm*, 21 January 2021 — the Westgarth statement.
- DeepMind, *Safety-first AI for autonomous data centre cooling and industrial control*,
  17 August 2018 — the 30% figure and the safeguards.
- Henderson, P. et al., *Deep Reinforcement Learning that Matters*, AAAI 2018 — the seed-variance
  result cited in `unit3-deep-rl/examples/05_training_evaluation_monitoring.ipynb`, if you use it
  for Q3.
- Ng, A. Y., Harada, D. & Russell, S., *Policy invariance under reward transformations*, ICML 1999
  — the shaping theorem cited in `unit1-rl-fundamentals/examples/06_solving_rl_problems_states_actions_rewards.ipynb`,
  if you use it for Q2.

**For:** Course 09 — AIAT 123
