# Quiz 01 Solution
## AIAT 123 - Reinforcement Learning

## Answer Key

**Teaching Notes**: This quiz checks Unit 1 understanding at the
concept-and-intuition level. Students should show they understand what RL
problems look like, how MDP pieces fit together, what `gamma` means, and why
basic exploration is needed.

**Grading**: Use the point values from the quiz. Award partial credit for
correct reasoning even when wording differs from the sample answers.

## Detailed Answers

### Question 1
- Correct answer: `b`
- Explanation: Supervised learning trains from labeled input-output examples.
  RL learns from interaction with an environment and feedback in the form of
  rewards rather than direct labels for the correct action.

### Question 2
- Correct answer: `b`
- Explanation: The Markov property means the current state, together with the
  chosen action, contains the information needed for predicting the next step.
  The full earlier history does not need to be stored explicitly in the model.

### Question 3
- Correct answer: `b`
- Explanation: The discount factor `gamma` controls how much future rewards
  matter relative to immediate rewards. Smaller values make the agent more
  short-term; larger values make it care more about long-term consequences.

### Question 4
- Correct answer: `b`
- Explanation: In epsilon-greedy, the agent explores by choosing a random
  action with probability epsilon and exploits by choosing the best-known
  action the rest of the time.

### Question 5 (Code)
Accept equivalent code if it initializes the Q-table correctly and applies the
Q-learning update rule to `Q[2, 1]`.

```python
import numpy as np

Q = np.zeros((5, 4))

state = 2
action = 1
reward = 10
next_state = 3
alpha = 0.1
gamma = 0.9

Q[state, action] += alpha * (
    reward + gamma * np.max(Q[next_state, :]) - Q[state, action]
)

print(Q[2, 1])  # 1.0
```

Why the result is `1.0`:
- All Q-values start at zero.
- `max(Q[next_state, :]) = 0`.
- So the update becomes `0 + 0.1 * (10 + 0 - 0) = 1.0`.

### Question 6
Expected points:
- A policy is a rule that tells the agent what action to take in each state.
- A deterministic policy chooses one specific action for a given state.
- A stochastic policy gives a probability distribution over actions.
- Students should include a simple example.

Sample answer:
A policy is the agent's decision rule. In a deterministic policy, the same
state always maps to the same action, such as "if the cart leans left, push
left." In a stochastic policy, the agent may assign probabilities to actions,
such as taking action A with probability 0.8 and action B with probability
0.2. Stochastic policies are useful when uncertainty or exploration matters.

### Question 7
Expected points:
- Exploration means trying actions that may not yet look best.
- Exploitation means choosing the best-known action so far.
- The dilemma is that too much exploration wastes time, but too little may miss
  better actions.
- Valid practical answers include epsilon decay, a scheduled reduction in
  randomness, or a better-tuned exploration phase.

Sample answer:
The exploration-exploitation dilemma exists because the agent must balance
trying unfamiliar actions against using what it already believes is best. If it
only exploits, it may get stuck with a poor policy. If it only explores, it
learns slowly. One practical fix is epsilon decay, where the agent explores
more early in training and then gradually becomes more greedy as knowledge
improves.

### Question 8
Expected points:
- Students should mention overfitting to the training setup, weak exploration,
  too little training, or poor reward design as plausible causes.
- They should suggest one concrete improvement such as more episodes, improved
  exploration scheduling, or better reward shaping.

Sample answer:
High training reward but weak evaluation performance may mean the agent has not
generalized well, explored enough, or learned a reward signal that does not
match the true task objective. A reasonable fix is to train longer with a
better exploration schedule, then reevaluate using a more stable testing setup.
If the reward is misleading, reward shaping or cleaner reward design may also
help.

## Common Mistakes
- Treating reward as if it were the same thing as state.
- Saying `gamma` is a learning-rate parameter.
- Describing epsilon-greedy as "always random" or "never random."
- Defining policy without explaining that it belongs to the agent.
- Giving an exploration answer that does not actually address the trade-off.

## Additional Resources
- Unit 1 numbered notebooks.
- `DOCS/GLOSSARY.md`
- `DOCS/ALGORITHM_CHEAT_SHEET.md`
