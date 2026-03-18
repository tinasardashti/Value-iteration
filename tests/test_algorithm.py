from value_iteration.algorithm import value_iteration

def test_value_iteration_runs():

    states = ["A", "B"]
    actions = {"A": ["go"], "B": []}

    transitions = {
        ("A","go"): [(1.0,"B")]
    }

    rewards = {
        ("A","go","B"): 10
    }

    V = value_iteration(states, actions, transitions, rewards)

    assert "A" in V
    assert V["A"] > 0

