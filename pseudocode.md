# Algorithm & Pseudocode Comparison

This document outlines the Value Iteration algorithm used in this project and contrasts it with the theoretical foundation provided in *Artificial Intelligence: Foundations and Computational Agents* (Poole and Mackworth).

## 1. Original Textbook Pseudocode (Figure 9.16)

The standard synchronous Value Iteration algorithm as defined by Poole and Mackworth follows this structure:

```text
procedure Value_iteration_original(S, A, P, R, gamma):
    Initialize V_k[s] arbitrarily for all s in S
    Initialize V_k_minus_1[s] arbitrarily for all s in S
   
    // Value Update Loop
    repeat:
        for each state s in S:
            V_k[s] = max_a (R(s,a) + gamma * sum over s' of P(s'|s,a) * V_k_minus_1[s'])
       
        V_k_minus_1 = V_k
    until convergence
   
    // Policy Extraction Loop
    Initialize policy[s] for all s in S
    for each state s in S:
        policy[s] = argmax_a (R(s,a) + gamma * sum over s' of P(s'|s,a) * V_k[s'])
       
    return V_k, policy
```

## 2. Custom Implementation Pseudocode

The Value Iteration algorithm implemented in this project operates as follows:

```text
procedure Value_iteration_custom(S, A, P, R, gamma, theta):
    Initialize V[s] = 0 for all s in S
   
    // Value Update Loop
    repeat:
        delta = 0
       
        for each state s in S:
            if s has no available actions:
                continue
           
            best_value = -∞
           
            for each action a available in s:
                total = 0
               
                for each (probability p, next state s') in P(s,a):
                    total = total + p * (R(s,a,s') + gamma * V[s'])
               
                best_value = max(best_value, total)
           
            delta = max(delta, |V[s] - best_value|)
            V[s] = best_value
           
    until delta < theta
   
    return V
```
 After computing the optimal value function, the optimal policy is obtained separately:
 
```text
procedure Extract_policy(S, A, P, R, V, gamma):
    Initialize policy[s] = None for all s in S
   
    for each state s in S:
        if s has no available actions:
            policy[s] = None
            continue
       
        best_action = None
        best_value = -∞
       
        for each action a available in s:
            total = 0
           
            for each (probability p, next state s') in P(s,a):
                total = total + p * (R(s,a,s') + gamma * V[s'])
           
            if total > best_value:
                best_value = total
                best_action = a
       
        policy[s] = best_action
   
    return policy
```

## 3. Differences

This implementation introduces several differences from the textbook pseudocode to improve clarity and practical usability:


In-Place (Asynchronous) Updates:
    The textbook version uses two separate value functions ($V_k$ and $V_{k-1}$) and updates them synchronously. In contrast, this implementation updates a single value function $V$ directly in-place. This allows newly computed values to be reused immediately and simplifies the implementation.


Explicit Convergence Criterion:
    The textbook leaves the stopping condition unspecified ("until termination"). This implementation defines convergence explicitly using a threshold $\theta$, stopping when the maximum change in values (delta) becomes smaller than $\theta$.


Reward Function Structure:
    The textbook defines rewards as $R(s,a)$, depending only on the current state and action. This implementation uses $R(s,a,s')$, allowing rewards to depend on the resulting next state. This is particularly useful for modelling environments such as Grid World.


Handling of Terminal States:
    Terminal states are handled explicitly by checking whether a state has available actions. If not, the state is skipped during value updates and assigned a policy of None.


Separate Policy Extraction:
    Unlike some optimized approaches, this implementation computes the policy after the value function has converged, using a separate loop. This keeps the structure clear and closely aligned with the theoretical formulation.
