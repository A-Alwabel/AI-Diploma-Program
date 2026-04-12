# Quiz 03 Solution
## AIAT 123 - Reinforcement Learning

## Answer Key

**Teaching Notes**: This solution guide should be taught honestly. Unit 3 gives
students DQN implementation practice, actor-critic intuition, and simplified
PPO-style stability framing. The goal is not to pretend they completed an
advanced full-scale PPO or Atari engineering block.

**Grading**: Use the point values from the quiz. For open questions, give
partial credit for correct intuition, not only exact formal wording.

## Detailed Answers

### Question 1
- Correct answer: `b`
- Explanation: Experience replay stores transitions and samples them in a less
  correlated way, which makes gradient updates more stable and data-efficient
  than training only on consecutive online samples.

### Question 2
- Correct answer: `b`
- Explanation: The target network helps stabilize learning by changing the
  bootstrap target more slowly. Without that, the network may chase a moving
  target too aggressively.

### Question 3
- Correct answer: `b`
- Explanation: REINFORCE updates policy parameters using the gradient of the
  log-probability of the chosen action, weighted by return. The key idea is to
  increase the probability of actions that led to better returns.

### Question 4
- Correct answer: `b`
- Explanation: The actor chooses actions, while the critic evaluates how good
  states or state-action decisions are. Their combination can reduce variance
  and improve learning guidance.

### Question 5 (Code)
Accept equivalent PyTorch code or clear pseudocode if it shows:
- a network mapping CartPole state to Q-values,
- epsilon-greedy action selection,
- the Bellman target, and
- MSE loss between prediction and target.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class DQN(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(4, 64)
        self.fc2 = nn.Linear(64, 64)
        self.fc3 = nn.Linear(64, 2)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        return self.fc3(x)

policy_net = DQN()
gamma = 0.99
epsilon = 0.1

def select_action(state_tensor):
    if torch.rand(1).item() < epsilon:
        return torch.randint(0, 2, (1,)).item()
    with torch.no_grad():
        q_values = policy_net(state_tensor)
        return int(torch.argmax(q_values).item())

# one training example
state = torch.randn(1, 4)
next_state = torch.randn(1, 4)
action = 1
reward = torch.tensor([1.0])

predicted_q = policy_net(state)[0, action]
with torch.no_grad():
    next_q_max = torch.max(policy_net(next_state), dim=1).values
    target = reward + gamma * next_q_max

loss = F.mse_loss(predicted_q.unsqueeze(0), target)
print(loss.item())
```

### Question 6
Expected points:
- Reward shaping adds extra reward signals to guide learning.
- It is used to speed up learning or make sparse-reward tasks easier.
- Poor shaping can push the agent toward shortcuts or behavior that optimizes
  the shaped reward rather than the real goal.

Sample answer:
Reward shaping means modifying the reward signal so the agent gets more helpful
learning guidance. It is useful when the original reward is too sparse or too
hard to learn from directly. The risk is that a badly designed shaping reward
can cause reward hacking, where the agent learns behavior that scores well on
the shaped reward but fails the true task.

### Question 7
Expected points:
- PPO aims for more stable policy improvement than naive policy-gradient
  updating.
- Students should describe the idea of keeping updates from changing the policy
  too much at once.
- Mentioning clipping or a trust-region-like constraint earns full credit.

Sample answer:
PPO tries to keep policy updates more stable than vanilla REINFORCE. Its core
idea is to improve the policy while preventing the new policy from moving too
far from the old one in a single update. In practice, this is often explained
through a clipped objective or another constraint that limits overly large
policy changes.

### Question 8
Expected points:
- Early near-zero reward may reflect sparse success, weak exploration, or slow
  discovery of useful behaviors.
- Experience replay helps by reusing informative transitions and reducing sample
  correlation.
- Epsilon decay helps by encouraging exploration early and more exploitation
  later.

Sample answer:
The likely cause is that the agent has not yet found enough useful experience,
especially early in training when successful trajectories are rare. Experience
replay helps reuse valuable transitions and makes updates less correlated.
Epsilon decay helps because the agent explores more early on, then gradually
becomes more greedy after it has learned something useful.

## Common Mistakes
- Saying replay buffer replaces the target network.
- Treating DQN as unrelated to Q-learning.
- Describing the critic as if it directly chooses actions.
- Explaining PPO as if Unit 3 taught a full industrial PPO implementation.
- Forgetting that reward shaping can introduce new failure modes.

## Additional Resources
- Unit 3 numbered notebooks.
- `DOCS/GLOSSARY.md`
- `DOCS/ALGORITHM_CHEAT_SHEET.md`
