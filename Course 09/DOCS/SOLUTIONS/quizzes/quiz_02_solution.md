# Quiz 02 Solution
## AIAT 123 - Reinforcement Learning

## Answer Key

**Teaching Notes**: This quiz should confirm that students understand the shift
from dynamic programming to model-free learning, and that they can compare
Monte Carlo, TD, Q-learning, and SARSA conceptually.

**Grading**: Use the point values from the quiz. Award partial credit when the
student shows the right idea even if the wording is informal.

## Detailed Answers

### Question 1
- Correct answer: `b`
- Explanation: Q-learning updates toward the greedy best estimated next action
  value, while SARSA updates from the value of the next action actually chosen
  by the current behavior policy.

### Question 2
- Correct answer: `b`
- Explanation: Monte Carlo methods estimate values by averaging returns from
  complete sampled episodes. They do not require a model, but they do wait for
  full episode outcomes.

### Question 3
- Correct answer: `b`
- Explanation: TD learning updates after each step using a target built from
  reward plus a discounted estimate of the next value. That is why TD is called
  a bootstrapping method.

### Question 4
- Correct answer: `b`
- Explanation: Policy iteration alternates between evaluating the current
  policy and improving it using the resulting values.

### Question 5 (Code)
Accept equivalent code if it includes a Q-table, epsilon-greedy choice logic,
and one correct Q-update.

```python
import numpy as np

Q = np.zeros((25, 4))
alpha = 0.1
gamma = 0.95
epsilon = 0.1

def select_action(state):
    if np.random.rand() < epsilon:
        return np.random.randint(4)
    return int(np.argmax(Q[state]))

def q_update(state, action, reward, next_state):
    td_target = reward + gamma * np.max(Q[next_state])
    td_error = td_target - Q[state, action]
    Q[state, action] += alpha * td_error

state = 5
action = 2
reward = -1
next_state = 6

print("Before:", Q[5, 2])
q_update(state, action, reward, next_state)
print("After:", Q[5, 2])
```

If the table starts at zero:
- `max(Q[6]) = 0`
- Update becomes `0 + 0.1 * (-1 + 0 - 0) = -0.1`

### Question 6
Expected points:
- Dynamic programming needs a known model of transitions/rewards and usually
  small discrete state spaces.
- In many real problems, the model is unknown or too large to use directly.
- Model-free methods learn from sampled experience instead of requiring full
  transition knowledge.

Sample answer:
Dynamic programming is powerful in small environments when the transition model
is known, but many practical RL problems do not provide that model explicitly.
Model-free methods like Q-learning are preferred because they can learn from
interaction data alone, even when the environment is unknown or too large for
exact tabular planning.

### Question 7
Expected points:
- First-visit Monte Carlo updates from the first time a state appears in an
  episode.
- Every-visit Monte Carlo uses every occurrence of that state in the episode.
- Students should mention that both average sampled returns, but they differ in
  data usage and update frequency.

Sample answer:
First-visit Monte Carlo updates a state's value from only its first occurrence
in each episode, while every-visit Monte Carlo uses all occurrences. First
visit can be conceptually cleaner, while every-visit may use more data from a
single episode. In practice, both can work well, but every-visit often gives
more updates when states repeat frequently.

### Question 8
Expected points:
- High alpha can make updates too aggressive.
- That can cause oscillation or instability because each new sample changes the
  value estimate too strongly.
- A valid fix is lowering alpha or decaying it over time.

Sample answer:
If alpha is too high, Q-values can swing too much after each new experience,
which makes learning unstable and can prevent convergence to a good policy. A
good fix is to reduce alpha, or decay it gradually as training proceeds so
early learning is faster but later updates become more stable.

## Common Mistakes
- Saying Q-learning requires a model.
- Mixing Monte Carlo bootstrapping with TD bootstrapping.
- Forgetting that SARSA depends on the next action actually taken.
- Explaining policy iteration without mentioning evaluation first.
- Treating alpha and gamma as if they play the same role.

## Additional Resources
- Unit 2 numbered notebooks.
- `DOCS/GLOSSARY.md`
- `DOCS/ALGORITHM_CHEAT_SHEET.md`
