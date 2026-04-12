# Quiz 04 Solution
## AIAT 123 - Reinforcement Learning

## Answer Key

**Teaching Notes**: Grade this quiz against the numbered Unit 4 student path only.
Keep answers anchored to epsilon-greedy, epsilon decay, UCB, Thompson Sampling,
Boltzmann exploration, and high-level curiosity language.

**Grading**: Use the student quiz point values.

## Part 1: Multiple Choice

### Question 1

- Correct Answer: `b`
- Explanation: UCB combines the current estimated reward with an exploration
  bonus that becomes larger for actions with higher uncertainty or fewer pulls.

### Question 2

- Correct Answer: `b`
- Explanation: Boltzmann (softmax) exploration converts action values into a
  probability distribution using `exp(Q / tau)`. Higher temperature means
  broader exploration; lower temperature makes the policy greedier.

### Question 3

- Correct Answer: `b`
- Explanation: Epsilon decay means the agent explores more at the beginning and
  gradually reduces random exploration as learning progresses.

### Question 4

- Correct Answer: `b`
- Explanation: Curiosity-driven exploration adds an intrinsic signal for novelty
  or surprise, encouraging the agent to visit states that may teach it
  something new.

## Part 2: Code Writing

### Question 5

```python
import numpy as np

n_actions = 4
epsilon_start = 1.0
epsilon_end = 0.05
epsilon_decay = 0.995


def select_action(q_values, epsilon):
    if np.random.rand() < epsilon:
        return np.random.randint(len(q_values))
    return int(np.argmax(q_values))


def update_epsilon(epsilon):
    return max(epsilon_end, epsilon * epsilon_decay)


epsilon = epsilon_start
epsilon_0 = epsilon

for _ in range(100):
    epsilon = update_epsilon(epsilon)
epsilon_100 = epsilon

epsilon = epsilon_start
for _ in range(500):
    epsilon = update_epsilon(epsilon)
epsilon_500 = epsilon

print("epsilon after 0 steps:", epsilon_0)
print("epsilon after 100 steps:", epsilon_100)
print("epsilon after 500 steps:", epsilon_500)
```

#### Expected interpretation

- After `0` steps: `1.0`
- After `100` steps: about `0.606`
- After `500` steps: clipped at `0.05`

Award full credit if the student:
- writes a correct epsilon-greedy selector
- applies the decay with a lower bound using `max`
- computes or clearly states the three requested epsilon values

## Part 3: Short Answer

### Question 6

#### Key points for Question 6

- Epsilon-greedy explores by taking a random action with probability `epsilon`.
- UCB explores more deliberately by adding an uncertainty bonus to less-tested
  actions.
- UCB is often preferred when action counts and reward estimates are available
  and the goal is to explore efficiently instead of randomly.
- A good scenario: online experiments or bandits where the agent must reduce
  wasted random exploration.

### Question 7

#### Key points for Question 7

- The exploration-exploitation dilemma is the tension between:
  - trying uncertain actions to learn more
  - choosing the action that currently looks best
- In a multi-armed bandit, this means deciding whether to keep testing weaker or
  less-certain arms versus repeatedly pulling the current best arm.
- Thompson Sampling addresses this by sampling from a belief distribution over
  each action's value.
- This naturally balances exploration and exploitation:
  - uncertain actions are still sampled sometimes
  - strong actions are sampled more often as evidence accumulates

## Part 4: Application

### Question 8

#### Expected answer shape

Students may choose any of the taught methods if the reasoning matches:

- `UCB`
  - good when efficient, uncertainty-aware exploration is needed
  - useful when less-tried actions should get a principled bonus

- `Thompson Sampling`
  - good when uncertainty should be represented probabilistically
  - useful in bandit-style online decision problems

- `epsilon-greedy with decay`
  - good as a simple baseline
  - useful when the student explains that exploration should be higher early and
    lower later

Award full credit when the student:
- chooses a taught Unit 4 method
- explains why it fits limited-data or uncertain-action settings
- shows they understand the exploration-exploitation trade-off

## Common Mistakes

- Confusing epsilon with learning rate or discount factor
- Describing UCB as random exploration
- Describing Thompson Sampling as deterministic greedy choice
- Treating curiosity as a fully implemented deep RL method in this unit instead
  of a high-level exploration idea

## Additional Resources

- `DOCS/GLOSSARY.md`
- `DOCS/ALGORITHM_CHEAT_SHEET.md`
- `unit4-exploration-exploitation/examples/01_exploration_strategies.ipynb`
- `unit4-exploration-exploitation/examples/03_adaptive_exploration_ucb.ipynb`
- `unit4-exploration-exploitation/examples/04_comparing_exploration_methods.ipynb`
