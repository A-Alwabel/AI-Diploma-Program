# Final Exam Solution Guide
## AIAT 123 - Reinforcement Learning

## Instructor Use Only

This guide matches the required numbered student path. It should be used for
fair grading, not for introducing supplemental-only topics during correction.

## Part 1: Multiple Choice

1. B
2. B
3. B
4. B

Short explanations:

- Q1: An MDP includes states, actions, rewards, and transitions.
- Q2: Q-learning updates toward the greedy next action value even if the
  behavior policy explored differently.
- Q3: Experience replay breaks sample correlation and reuses data.
- Q4: Model-based RL uses or learns a model and can plan with it.

## Part 2: Short Answer Guidance

### Question 5

Strong answers define:

- **state** as what the agent observes
- **action** as a valid choice the agent can take
- **reward** as the feedback signal
- **policy** as the mapping from state to action

The answer should include one concrete environment example.

### Question 6

Strong answers should note:

- Q-learning learns action values and is off-policy
- SARSA learns action values and is on-policy
- Policy Gradient learns policy parameters directly
- Each has different trade-offs for stability, action spaces, and exploration

### Question 7

Strong answers should explain:

- why always exploiting is risky
- why always exploring is inefficient
- how epsilon-greedy works
- how UCB or Thompson Sampling uses uncertainty more explicitly

## Part 3: Practical / Coding

### Question 8

Look for:

- loop over non-terminal states
- evaluation of all actions
- Bellman optimality update
- special handling of terminal states

Sample structure:

```python
for s in states:
    if s in terminal_states:
        new_V[s] = 0
    else:
        action_values = []
        for a in actions:
            total = 0
            for prob, next_state, reward in transitions[s][a]:
                total += prob * (reward + gamma * V[next_state])
            action_values.append(total)
        new_V[s] = max(action_values)
```

### Question 9

Look for:

- Q-table initialization
- epsilon-greedy action selection
- environment step
- Q-update rule
- episode loop

Sample structure:

```python
Q = np.zeros((num_states, num_actions))

for episode in range(num_episodes):
    state = env.reset()
    done = False

    while not done:
        if np.random.rand() < epsilon:
            action = np.random.randint(num_actions)
        else:
            action = np.argmax(Q[state])

        next_state, reward, done, _ = env.step(action)
        Q[state, action] += alpha * (
            reward + gamma * np.max(Q[next_state]) - Q[state, action]
        )
        state = next_state
```

## Part 4: Application and Judgment

### Question 10

Strong answers should define a coherent RL problem:

- state
- action
- reward
- one challenge such as delayed reward, sparse reward, or reward
  hacking

Full-credit answers also make the formulation realistic rather than listing
abstract labels only.

### Question 11

Strong answers should mention at least one real risk and one evaluation
method, for example:

- unsafe exploration
- manipulation or unfair exposure
- offline evaluation
- held-out environments
- simulation before deployment
- reward and regret tracking

High-scoring answers connect the risk to the task and explain why the proposed
evaluation method would catch it.
