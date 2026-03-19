from value_iteration.algorithm import value_iteration


def run_sam_example():
    print("Running Sam's Weekend Example...\n")

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

    V, policy = value_iteration(states, actions, transitions, rewards)

    print("Optimal Policy:")
    for s in states:
        print(f"If {s}, choose: {policy[s]}")

    print("\nValue Function:")
    for s in states:
        print(f"V({s}) = {V[s]:.2f}")


if __name__ == "__main__":
    run_sam_example()
