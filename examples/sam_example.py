from value_iteration.algorithm import value_iteration
from value_iteration.policy import extract_policy


def run_sam_example():
    print("Running Sam's Weekend Example...\n")

    # define states
    states = ["healthy", "sick"]

    # define available actions in each state
    actions = {
        "healthy": ["relax", "party"],
        "sick": ["relax", "party"]
    }

    # transition probabilities
    transitions = {
        ("healthy","relax"): [(0.95,"healthy"), (0.05,"sick")],
        ("healthy","party"): [(0.7,"healthy"), (0.3,"sick")],
        ("sick","relax"): [(0.5,"healthy"), (0.5,"sick")],
        ("sick","party"): [(0.1,"healthy"), (0.9,"sick")]
    }

    # rewards for each transition
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

    # first compute value function
    V = value_iteration(states, actions, transitions, rewards)

    # then extract optimal policy using V
    policy = extract_policy(states, actions, transitions, rewards, V)

    # print results nicely
    print("Optimal Policy:")
    for s in states:
        print(f"If {s}, choose: {policy[s]}")

    print("\nValue Function:")
    for s in states:
        print(f"V({s}) = {V[s]:.2f}")


if __name__ == "__main__":
    run_sam_example()
