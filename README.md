# Value Iteration for Markov Decision Processes

## Abstract

This project implements the value iteration algorithm to solve Markov Decision Processes (MDPs). The algorithm computes the optimal value function and derives the optimal policy.

This repository is developed as part of the STOR609 module.

---

## Value Iteration:

Value iteration is a dynamic programming method used to find the optimal policy in an MDP.

It is based on the Bellman optimality equation:

V(s) = max_a Σ P(s'|s,a) [ R(s,a,s') + γ V(s') ]

Where:
- s is a state
- a is an action
- s' is the next state
- γ is the discount factor

---

## Project Structure

value_iteration/
    algorithm.py      # core value iteration implementation

examples/
    grid_world.py     # grid world example
    sam_example.py    # Example 9.27 (Sam’s decision problem)

notebooks/
    grid_world.ipynb  # required notebook for assessment

tests/
    test_algorithm.py # unit tests

docs/
    pseudocode.md     # pseudocode and comparison with textbook

---

## Installation

Create a virtual environment and install the package:

python -m venv env
source env/bin/activate
python -m pip install .

---

## Usage

### Run Grid World

python examples/grid_world.py

### Run Sam Example (Exercise 9.27)

python examples/sam_example.py

### Run Tests

python -m pytest tests

---

## Example Output (Grid World)

Values:
{'TL': 14.86, 'TR': 14.47, 'BL': 19.08, 'BR': 0}

Policy:
{'TL': 'D', 'TR': 'D', 'BL': 'R', 'BR': None}

---

## Reproducibility

This project is reproducible:

- The package can be installed using pip
- Examples can be rerun using provided scripts
- Unit tests validate correctness
- The notebook demonstrates usage step-by-step

---

## Design Choices

- Dictionary-based representation for flexibility
- Modular design for reuse in different MDPs
- In-place updates for faster convergence
- Policy extraction integrated with value iteration

---

## Author

Tina Sardashti
STOR609 – Assessment 2
