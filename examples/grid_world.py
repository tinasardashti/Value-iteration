from value_iteration.algorithm import value_iteration
from value_iteration.policy import extract_policy

# Define states
states = ["TL", "TR", "BL", "BR"]

#define actions available in each state
actions = {
    "TL": ["R", "D"],
    "TR": ["L", "D"],
    "BL": ["R", "U"]
    # BR is terminal, so no actions
}

#Define transition probabilities
transitions = {
    ("TL","R"): [(0.9,"TR"), (0.1,"BL")],
    ("TL","D"): [(0.9,"BL"), (0.1,"TR")],

    ("TR","L"): [(0.9,"TL"), (0.1,"BR")],
    ("TR","D"): [(0.8,"BR"), (0.2,"TL")],

    ("BL","R"): [(0.9,"BR"), (0.1,"TL")],
    ("BL","U"): [(0.8,"TL"), (0.2,"BR")]
}

#Define rewards
rewards = {
    ("TL","R","TR"): -1,
    ("TL","R","BL"): -2,
    ("TL","D","BL"): -2,
    ("TL","D","TR"): -1,

    ("TR","L","TL"): -1.5,
    ("TR","L","BR"): 10,
    ("TR","D","BR"): 15,
    ("TR","D","TL"): -1,

    ("BL","R","BR"): 20,
    ("BL","R","TL"): -2.5,
    ("BL","U","TL"): -0.5,
    ("BL","U","BR"): 5
}

V = value_iteration(states, actions, transitions, rewards)

#extract policy
policy = extract_policy(states, actions, transitions, rewards, V)

print("Optimal Values:", V)
print("Optimal Policy:", policy)
