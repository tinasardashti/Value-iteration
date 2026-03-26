from value_iteration.algorithm import value_iteration
from value_iteration.policy import extract_policy


def run_sam_example():

    # define the states in the problem
    states = ["healthy", "sick"]

    # available actions for each state
    actions = {
        "healthy": ["relax", "party"],
        "sick": ["relax", "party"]
    }

    # transition probabilities
    # each entry gives (probability, next_state)
    transitions = {
        ("healthy","relax"): [(0.95,"healthy"), (0.05,"sick")],
        ("healthy","party"): [(0.7,"healthy"), (0.3,"sick")],
        ("sick","relax"): [(0.5,"healthy"), (0.5,"sick")],
        ("sick","party"): [(0.1,"healthy"), (0.9,"sick")]
    }

    # rewards for each transition (s, a, s')
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

    # first compute the optimal value function
    V = value_iteration(states, actions, transitions, rewards)

    #derive the optimal policy from V
    policy = extract_policy(states, actions, transitions, rewards, V)

    print("\nOptimal Policy:")
    for s in states:
        print(f"{s}: {policy[s]}")

    print("\nValue Function:")
    for s in states:
        print(f"V({s}) = {V[s]:.2f}")


if __name__ == "__main__":
    run_sam_example()

