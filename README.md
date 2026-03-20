# `value_iteration`

- [Description](#description)
- [Installation](#installation)
- [Example](#example)
  - [Simple 2-state MDP example](#simple-2-mdp-example)
  - [2x2 Gridworld example](#gridworld-example)
- [Pseudocode](#pseudocode)
- [License](#license)
- [GitHub Repository](#github-repository)
- [Contributors](#contributors)
- [References](#references)

## **Description**

The `value_iteration` Python package provides an implementation of the Value Iteration algorithm for solving Markov Decision Processes (MDPs).

Value iteration is a dynamic programming method that computes the optimal value function and derives the optimal policy by iteratively applying the Bellman optimality equation.

This implementation is designed to be simple, clear, and reusable for different MDP problems, including stochastic environments such as Grid World.

To learn more about MDPs and value iteration, see Sections [9.5](https://artint.info/2e/html2e/ArtInt2e.Ch9.S5.html) and [9.5.1](https://artint.info/2e/html2e/ArtInt2e.Ch9.S5.SS1.html) of *Artificial Intelligence: Foundations and Computational Agents (2nd Edition)*.

**Key Features**
- Simple and clear implementation of value iteration  
- Works with any MDP defined using states, actions, transitions, and rewards  
- Supports stochastic transitions  
- Includes unit tests for correctness  
- Provides practical examples (Sam problem and Grid World)  
- Designed for reproducibility and reuse  

## **Installation**

Create a virtual environment and install the package:

```bash
python -m venv env
source env/bin/activate
python -m pip install .
```

## **Example**

### Simple 2-state MDP example

This example is taken from [Example 9.27](https://artint.info/2e/html2e/ArtInt2e.Ch9.S5.html#Ch9.Thmciexamplered27) in *Artificial Intelligence: Foundations and Computational Agents (2nd Edition)*.

Sam must decide whether to party or relax, considering the risk of becoming sick. The problem is modelled as an MDP with:

States: healthy, sick  
Actions: relax, party  

Based on experience, the transition probabilities are:

| S        | A      | Probability of $s' =$ healthy |
|----------|--------|-------------------------------|
| healthy  | relax  | 0.95                          |
| healthy  | party  | 0.7                           |
| sick     | relax  | 0.5                           |
| sick     | party  | 0.1                           |

The rewards are:

| S        | A      | Reward |
|----------|--------|--------|
| healthy  | relax  | 7      |
| healthy  | party  | 10     |
| sick     | relax  | 0      |
| sick     | party  | 2      |

The implementation is provided in:

`examples/sam_example.py`

After running the code with a discount factor γ = 0.9, the optimal policy is:

If healthy → choose party  
If sick → choose relax  

### 2x2 Gridworld example

A stochastic Grid World problem is also implemented to demonstrate the algorithm in a spatial setting.

States represent positions in a grid  
Actions correspond to movements (up, down, left, right)  
Transitions are probabilistic (slipping behaviour)  

The implementation is provided in:

`examples/grid_world.py`

A full step-by-step explanation is available in:

`notebooks/grid_world.ipynb`

## **Pseudocode**

The implementation follows the Bellman optimality equation:

\[
V(s) = \max_a \sum_{s'} P(s'|s,a)\left[ R(s,a,s') + \gamma V(s') \right]
\]

The algorithm repeatedly updates state values until convergence, then extracts the optimal policy.

A full pseudocode description and comparison with Figure 9.16 from Poole and Mackworth is provided in:

`docs/pseudocode.md`

## **License**

This project is provided for academic and educational use.

## **GitHub Repository**

This repository contains the full implementation, examples, and documentation.

## **Contributors**

- Tina Sardashti (**Author**)

## **References**

Poole, D. L., & Mackworth, A. K. (2017).  
*Artificial Intelligence: Foundations of Computational Agents* (2nd ed.).  
Cambridge University Press.
