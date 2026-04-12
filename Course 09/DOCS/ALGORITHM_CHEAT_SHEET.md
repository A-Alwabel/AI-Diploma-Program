# Reinforcement Learning Algorithm Cheat Sheet

## Purpose

Use this page when you remember the algorithm names but forget:

- what each one learns
- when it is a good choice
- what its main weakness is

## Fast Comparison

- **Value Iteration**
  Learns optimal state values, then a policy. Best for small known MDPs. Watch
  out: it needs an environment model.
- **Policy Iteration**
  Learns a policy through evaluation and improvement. Best for small known MDPs.
  Watch out: it also needs an environment model.
- **Monte Carlo**
  Learns from full returns. Best for episodic tasks. Watch out: feedback is
  slower and variance is higher.
- **TD(0)**
  Learns state values through bootstrapping. Best for online incremental
  learning. Watch out: early estimates may be weak.
- **Q-Learning**
  Learns Q-values. Best for discrete off-policy control. Watch out: tabular
  versions do not scale well to large spaces.
- **SARSA**
  Learns Q-values from the current behavior policy. Best for more cautious
  learning under exploration. Watch out: it is sensitive to the actions
  actually taken.
- **Policy Gradient / REINFORCE**
  Learns the policy directly. Best for stochastic action selection. Watch out:
  updates can have high variance.
- **DQN**
  Learns Q-values with a neural network. Best for larger state descriptions.
  Watch out: replay and target networks are needed for stability.
- **Actor-Critic**
  Learns a policy and a value estimate together. Best for a stronger deep RL
  balance. Watch out: it has more moving parts.
- **PPO**
  Learns stable policy updates. Best for modern policy optimization. Watch out:
  it is more conceptually complex than tabular methods.
- **UCB**
  Learns through an uncertainty bonus. Best for bandits and structured
  exploration. Watch out: confidence bonuses must be interpreted correctly.

## By Unit

### Unit 1

#### MDP Formulation

- Focus: understanding the RL problem setup itself
- Use when: you still need to define states, actions, rewards, and transitions
- Do not ask first: "Which algorithm should I use?"
- Ask first: "Did I formulate the problem correctly?"

#### Value Iteration

- Learns: optimal values, then optimal policy
- Assumes: a known environment model
- Good student mental model:
  Update each state by asking, "If I act optimally from here, what is this
  state worth?"

### Unit 2

#### Monte Carlo

- Learns from: complete episodes
- Strength: conceptually clear because it uses real observed returns
- Weakness: must wait for the episode to finish

#### TD(0)

- Learns from: one step plus an estimate of the future
- Strength: faster online updates
- Weakness: early estimates may be noisy

#### Q-Learning

- Learns: action values
- Policy style: off-policy
- Update intuition:
  "Use the reward now plus the best next value I could get."

#### SARSA

- Learns: action values
- Policy style: on-policy
- Update intuition:
  "Use the reward now plus the value of the next action I actually chose."

#### Q-Learning vs SARSA

| Question | Q-Learning | SARSA |
| -------- | ---------- | ----- |
| Next target uses | Best next action | Actual next action taken |
| Style | Off-policy | On-policy |
| Behavior tendency | More aggressive | More cautious |

### Unit 3

#### Policy Gradient

- Learns: the policy directly
- Good when: action probabilities matter and direct policy learning is useful
- Weakness: updates can be noisy

#### DQN

- Learns: Q-values with a neural network
- Needs:
  - replay buffer
  - target network
  - epsilon-greedy or another exploration plan
- Good mental model:
  It is still Q-learning, but with a neural network replacing the table.

#### Actor-Critic

| Part | Job |
| ---- | --- |
| Actor | Chooses actions |
| Critic | Evaluates how good those decisions are |

#### PPO

- Main idea: improve the policy, but not too much in one update
- Why students should care:
  It is a stability method, not just a new formula

### Unit 4

#### Epsilon-Greedy

- Easiest exploration baseline
- Good for: understanding exploration vs exploitation
- Weakness: random exploration is simple, but not always efficient

#### UCB

- Main idea: add an uncertainty bonus
- Good for: principled exploration in bandit-style settings
- Weakness: students may focus on formula over intuition

#### Thompson Sampling

- Main idea: sample actions according to uncertainty-aware beliefs
- Good for: bandit-style problems where probabilistic uncertainty is useful
- Weakness: students may say "Bayesian" without explaining the actual decision
  logic

#### Boltzmann Exploration

- Main idea: turn action values into probabilities using a temperature parameter
- Good for: smoother exploration than purely random action choice
- Weakness: temperature can feel abstract unless students connect it to
  "more spread out" versus "more greedy" action probabilities

#### Epsilon Decay

- Main idea: explore more early, less later
- Good for: simple training schedules where a basic exploration plan is enough
- Weakness: if epsilon stays too high, the agent keeps acting too randomly late
  in training

#### Bandit vs Full RL

- Bandit setting:
  choose an action and observe reward, but there is no full state-transition
  story
- Full RL setting:
  actions change future states, so exploration affects the whole trajectory
- Student warning:
  Unit 4 often teaches the exploration intuition through bandits first because
  it isolates the trade-off more clearly

### Unit 5

#### Multi-Agent RL

- Use when: several agents act in the same environment
- Extra challenge: the environment changes because other agents also act

#### Hierarchical RL

- Use when: the task is long and easier to break into sub-goals
- Main student intuition:
  Solve a hard task by stacking smaller decisions

#### Model-Based RL

- Use when: planning with a learned or known model can reduce expensive real
  interaction
- Risk: poor models can mislead planning

#### Goal-Conditioned RL

- Use when: one policy should solve many related target goals
- Main idea:
  Give the goal to the agent as part of the input

## What To Ask Before Choosing an Algorithm

1. Is the environment model known?
2. Is the state space small enough for a table?
3. Is the action space discrete or continuous?
4. Do I need a direct policy or action values?
5. Is stability likely to be a major problem?
6. Is exploration the main challenge?

## Common Student Confusions

### "Q-Learning and DQN are different families."

Not really. DQN is the deep function-approximation version of the Q-learning
idea.

### "Actor-Critic means the critic chooses the action."

No. The actor chooses. The critic evaluates.

### "Model-based always beats model-free."

No. It may be more sample efficient, but it also depends on model quality and
planning cost.

### "Bandit exploration and RL exploration are exactly the same."

No. The exploration-exploitation trade-off is shared, but full RL also has
state transitions and long-term consequences that bandits do not.

### "More complex means more correct."

No. Often the best student project uses the simplest method that matches the
problem.

## Exam Tip

If you forget details in the exam, answer in this order:

1. what the method learns
2. whether it uses values, a policy, or both
3. when it is a reasonable choice
4. one limitation
