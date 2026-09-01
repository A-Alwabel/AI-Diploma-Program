# Case Study 01: AI Search Application
## Routing a delivery fleet, and knowing what you are promising

**Course:** Course 02 – AIAT 112 (Python for Artificial Intelligence)
**Type:** Case Study Analysis
**Points:** 100 (scaled to 10 of the course's 100 marks)
**Set:** session 16 · **Due:** session 21
**Length:** 1,200–1,500 words. Code optional; if you include any, it is evidence, not a separate mark.
**Time budget:** about one hour — 15 minutes reading and re-opening the two notebooks you will cite, 45 minutes writing.

---

## 1. The situation

This is a documented case, and it is the one this course opens Unit 1 with. See
`unit1-search-algorithms/examples/02_search_algorithms.ipynb`.

In **2016 UPS won INFORMS' Franz Edelman Award for ORION** (On-Road Integrated Optimization and
Navigation), the system that plans each driver's day across UPS's **55,000 US delivery routes**. UPS's
reported figures at full deployment: about **100 million fewer miles driven** and **10 million fewer gallons
of fuel** per year, worth an estimated **$300–400 million annually**. ORION evaluates more than **200,000
alternative orderings** for a single driver's route before it prints one.

Two things about that number are worth holding onto for the whole of this brief.

**First, 200,000 is not all of them.** A driver with 120 stops has 120! possible orderings — a number with
199 digits. Checking them all is not slow; it is impossible, this year and every year. ORION does not
return the best route. It returns a good route, quickly, and it can say what it did.

**Second, the alternative was not chaos — it was a habit.** Before a search system, a route is planned by
"go to the nearest remaining stop", which is fast, is sometimes badly wrong, and **never tells you that it
is wrong**. As `02_search_algorithms.ipynb` puts it: the failure of hand-tuning is not that it finds a bad
answer, it is that it gives you no way to know how much better the best answer is.

The same course shows the second half of that lesson with a measurement you ran yourself. In
`unit4-optimization-techniques/examples/01_optimization_techniques.ipynb`, gradient descent on
f(x) = (x−2)² + 2·sin(5x), starting from x = 5.0, prints **"Converged after 22 iterations"** and settles at
**f = 5.0674**. Simulated annealing, from the same start on the same function, reaches **f = −1.9610** —
seven units better. The gradient-descent run announced success.

**Sources.** INFORMS, 2016 Franz Edelman Award (UPS ORION), with UPS's own reported deployment figures ·
Hart, Nilsson and Raphael, *A Formal Basis for the Heuristic Determination of Minimum Cost Paths*, IEEE
Transactions on Systems Science and Cybernetics, 1968 (A\*, built for the Shakey robot at SRI) ·
Kirkpatrick, Gelatt and Vecchi, *Optimization by Simulated Annealing*, *Science* 220, 671–680, 1983.

---

## 2. The decision you have to make

A regional e-commerce retailer runs **40 vans** out of one warehouse. Each van does **60 to 90 stops a day**
in a city you know. Today the dispatcher builds the routes in a spreadsheet the evening before, using
experience and postcode grouping. Nobody has measured how good those routes are.

The retailer has read about ORION and wants "the same thing". They have given you:

- one year of delivery records — addresses, timestamps, van id, parcel weight;
- a road network they can pull from an open map service;
- three constraints the dispatcher enforces by hand today: each driver's shift is capped at 9 hours,
  some customers have a two-hour delivery window, and a van cannot exceed its weight limit;
- a budget for one developer for three months;
- an expectation, in writing, of "20% fewer kilometres".

**You must decide and defend:** which algorithm you would build this on, **what guarantee you can put in the
proposal**, and whether the 20% figure is a promise you are willing to sign.

There is no correct answer. A well-argued A\*-based system, a well-argued metaheuristic, and a well-argued
"buy an existing vehicle-routing solver and spend the three months on the data" can all score full marks.

---

## 3. The evidence you must bring

Your analysis must **cite at least three of this course's own notebooks by filename**, and quote a specific
number or guarantee from each. An answer that names algorithms without citing anything you measured cannot
pass the middle of the mark range.

| Question you have to answer | Where the course already answered it |
|---|---|
| Which algorithm, and what does it guarantee? | `unit1/02_search_algorithms.ipynb` — BFS returns the fewest edges, Dijkstra the lowest cost, A\* the lowest cost *if* the heuristic never overshoots, DFS guarantees only that it found a path |
| Why not just try everything? | `unit1/02_search_algorithms.ipynb` — 120 stops, 120! orderings, 199 digits |
| Why is "converged" not "solved"? | `unit4/01_optimization_techniques.ipynb` — f = 5.0674 with a success message, against f = −1.9610 on the same problem |
| What number do I report from a stochastic method? | `unit4/01_optimization_techniques.ipynb` — `seed = 42` buys reproducibility and hides variance; report a median of 20 runs with the spread |
| Where do the client's real constraints go? | `unit4/01_optimization_techniques.ipynb` — Parts 2–5 handle none, which is why Part 8 switches to `scipy.optimize.minimize` with an explicit constraint list |
| When should I not use a heuristic at all? | `unit4/01_optimization_techniques.ipynb` — if the problem is convex or linear, a proper solver beats every heuristic *and* certifies the answer |
| Has someone already solved my problem class? | `unit3/04_mdp_value_iteration.ipynb` — when the optimal policy for a problem class is already known, looking it up is the professional move |
| How do I compare two candidate systems honestly? | `unit5/01_ai_learning_models.ipynb` — five cross-validation folds ranged from MSE 0.5230 to 0.8388 on the same model, same data, same day |
| What does a small specification error cost? | `unit2/02_propositional_logic_truth_tables.ipynb` — five missing entries in a lookup table, and a $475 million charge announced on 17 January 1995 |

> Paths in the table are abbreviated. `unit4/01_optimization_techniques.ipynb` means
> `unit4-optimization-techniques/examples/01_optimization_techniques.ipynb`; the unit folder names are in
> the course README.

---

## 4. What you submit

Five sections, in this order.

**1. Problem analysis.** State the routing problem in one sentence a warehouse manager would understand.
What are the constraints — including at least one the brief above does not state outright? What data exists,
and what data does **not**? Define success as a number you could actually measure next quarter.

**2. Solution design.** Your algorithm choice, justified against the constraints you just listed — not
against fashion. Name one alternative you considered and rejected, with the reason. Say what the graph is
(what is a node, what is an edge, what is the edge cost), where the road data enters, and what the
dispatcher sees at 6 a.m. Name the Python libraries you would use and why.

**3. Implementation plan.** Five to eight ordered steps someone could start on Monday. Include the step
almost everyone omits: **measuring the dispatcher's current routes** before you build anything. Include
what happens after go-live — who watches it, what breaks it, how you roll back.

**4. Evaluation.** Which numbers you would report and how you would obtain them. If your method is
stochastic, say explicitly which statistic goes in the client report. Say what you would measure besides
kilometres — runtime per night, driver acceptance, late deliveries.

**5. Recommendation, limits and ethics.** Your decision in one sentence. Then two limitations that would
genuinely make *your* proposal fail, with a response to each. Then: the system is timing human beings.
Say what the route data can and cannot be used for, and who decides that.

---

## 5. Analysis questions

Answer these inside your five sections; do not answer them as a separate list. None has a single right
answer.

1. **ORION evaluates 200,000 orderings and does not claim to have found the best route.** Write the single
   sentence about guarantees that you would put in your proposal to this client. Then write the sentence a
   competitor might write that sounds stronger and is dishonest, and say what the difference is.

2. **The client wants 20% fewer kilometres.** UPS reported $300–400M a year across 55,000 routes. Your client
   has 40 vans, one city and one warehouse. What is the honest way to use the UPS figure in your proposal,
   and what exactly would you refuse to promise before you have measured the dispatcher's current routes?

3. **A\* is only optimal if the heuristic never overshoots the true remaining cost.** Straight-line distance
   satisfies that on an open road network. The city then adds one-way streets, a toll road and a bridge that
   closes at 22:00. Which of those breaks the guarantee, which does not, and what do you do about the ones
   that do? Start from the condition itself — h must never exceed the true remaining cost — and be precise
   about *which* cost you are minimising: kilometres, minutes, or riyals. The three do not give the same
   answer.

4. **Run your metaheuristic twenty times and you get twenty answers.** Which one goes in the client report —
   the best, the median, or the worst? Defend your choice, and say what each of the other two choices would
   hide from the client.

5. **Two of the three stated constraints (shift cap, delivery windows, weight limit) are not handled by
   anything you built in Units 1 and 4.** Choose the one you consider hardest, and describe what changes in
   your design once it is real. If your answer is "use a library that handles it", say what you then have to
   verify about that library and how.

---

## 6. What a strong answer contains

This is not a list of the right answers. It is what the marker is looking for.

- **The guarantee, stated as a guarantee.** The single strongest signal in this brief is a candidate who can
  say, in one sentence, what their system promises and what it does not.
- **A constraint the brief did not state.** It is in there.
- **A measured baseline before anything is built.** A proposal that compares a new routing system to nothing
  has made exactly the mistake Unit 1 opens with.
- **An alternative considered and rejected** — including the alternative of buying a vehicle-routing solver
  and spending the three months on data quality.
- **Named course evidence.** Three notebooks, three specific numbers or guarantees, used to carry an
  argument.
- **Honest treatment of variance.** A single run of a stochastic method quoted as "the result" is the error
  this course's own notebook flags in its limits section.
- **Two limitations that would genuinely sink your own proposal**, each with a response. "More data would
  help" earns nothing.
- **Something concrete about the drivers.** The system produces a per-minute record of a person's working
  day. A section 5 that does not notice this is incomplete.

"There are no limitations" is not an available answer on this brief.

---

## Submission

- Markdown or PDF, 1,200–1,500 words. Code snippets, if any, go in an appendix outside the word count.
- If you used an AI assistant, declare it in one line at the end: which tool, for what. Declared use is
  permitted; you will be asked to talk through your section 3 aloud.
- Submit by session 21.

---

**For:** Course 02 – AIAT 112 · Python for Artificial Intelligence
