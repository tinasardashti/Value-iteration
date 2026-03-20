from value_iteration.algorithm import value_iteration
from value_iteration.policy import extract_policy


def test_basic_behavior():
    """
    simple test to check that the algorithm works on a small MDP
    """

    states = ["A", "B"]

    actions = {
        "A": ["move", "wait"],
        "B": []
    }

    transitions = {
        ("A", "move"): [(1.0, "B")],
        ("A", "wait"): [(1.0, "A")]
    }

    rewards = {
        ("A", "move", "B"): 10,
        ("A", "wait", "A"): -2
    }

    V = value_iteration(states, actions, transitions, rewards)
    policy = extract_policy(states, actions, transitions, rewards, V)

    # value should be positive (moving is good)
    assert V["A"] > 0

    # best action should be "move"
    assert policy["A"] == "move"

    # terminal state has no action
    assert policy["B"] is None


def test_sam_example():
    """
    test using Sam's example (stochastic case)
    """

    states = ["healthy", "sick"]

    actions = {
        "healthy": ["relax", "party"],
        "sick": ["relax", "party"]
    }

    transitions = {
        ("healthy","relax"): [(0.95,"healthy"), (0.05,"sick")],
        ("healthy","party"): [(0.7,"healthy"), (0.3,"sick")],
        ("sick","relax"): [(0.5,"healthy"), (0.5,"sick")],
        ("sick","party"): [(0.1,"healthy"), (0.9,"sick")]
    }

    rewards = {
        ("healthy","relax","healthy"): 7,
        ("healthy","relax","sick"): 7,
        ("healthy","party","healthy"): 10,
        ("healthy","party","sick"): 10,
        ("sick","relax","healthy"): 0,
        ("sick","relax","sick"): 0,
        ("sick","party","healthy"): 2,
        ("sick","party","sick"): 2
    }

    V = value_iteration(states, actions, transitions, rewards)
    policy = extract_policy(states, actions, transitions, rewards, V)

    # values should be numbers
    assert isinstance(V["healthy"], float)

    # policy should choose valid actions
    assert policy["healthy"] in actions["healthy"]


def test_gamma_zero():
    """
    when gamma = 0, only immediate rewards matter
    """

    states = ["A"]

    actions = {
        "A": ["small", "big"]
    }

    transitions = {
        ("A", "small"): [(1.0, "A")],
        ("A", "big"): [(1.0, "A")]
    }

    rewards = {
        ("A", "small", "A"): 1,
        ("A", "big", "A"): 5
    }

    V = value_iteration(states, actions, transitions, rewards, gamma=0.0)
    policy = extract_policy(states, actions, transitions, rewards, V, gamma=0.0)

    # should choose the highest immediate reward
    assert V["A"] == 5
    assert policy["A"] == "big"
