# Unit 2: Policy and Value-Based Methods | السياسات والطرق القائمة على القيمة
## AIAT 123 - Reinforcement Learning

## ✅ Prerequisites Checklist | قائمة المتطلبات الأساسية

Before starting this unit, confirm:

- [ ] Completed Unit 1: Introduction to Reinforcement Learning
- [ ] Understand MDPs, policies, and value functions
- [ ] Installed required libraries (`pip check` passes)
- [ ] Reviewed related topics in `COURSE_MAP.md` if needed

### Learning Objectives | أهداف التعلم

By the end of this unit, students will be able to:
- Understand why model-free methods are needed when the environment model is unknown
- Work with Dynamic Programming foundations and understand their limits
- Implement Monte Carlo and Temporal Difference (TD) methods
- Implement Q-learning and SARSA
- Compare policy iteration and value iteration in small environments

---

## Topics Covered | المواضيع المغطاة

Based on the instructor unit materials and the notebooks included in this folder, this
unit focuses on model-free prediction and control:

1. **Dynamic Programming Foundations**
   - Bellman equations
   - Policy evaluation
   - Policy iteration
   - Value iteration
   - Why DP becomes impractical in large or unknown environments

2. **Monte Carlo Methods**
   - First-visit vs every-visit estimation
   - Monte Carlo prediction
   - Monte Carlo control
   - Sampling-based value estimation

3. **Temporal Difference (TD) Learning**
   - TD(0)
   - n-step TD methods
   - TD vs Monte Carlo
   - Bootstrapping and online updates

4. **Q-Learning**
   - Off-policy learning
   - Q-table updates
   - Temporal difference target
   - Convergence behavior in simple environments

5. **SARSA**
   - On-policy learning
   - SARSA update rule
   - Comparison with Q-learning
   - Exploration-aware learning behavior

6. **Policy Iteration vs Value Iteration**
   - Convergence comparison
   - Computational trade-offs
   - Small environment experiments

### Note | ملاحظة

This folder also includes a short `policy_gradient` notebook as supplemental material.
The main policy-gradient treatment belongs to `unit3-deep-rl/`.

---

**Unit Duration:** 2 weeks  
**Difficulty:** Advanced  
**Prerequisites:** Unit 1 completion

