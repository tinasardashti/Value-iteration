def extract_policy(states, actions, transitions, rewards, V, gamma=0.9):
    """
    Extract optimal policy from a value function.
    """

    policy = {}

    for s in states:

        if s not in actions or len(actions[s]) == 0:
            policy[s] = None
            continue

        best_action = None
        best_value = float("-inf")

        for a in actions[s]:
            total = 0

            for prob, s_next in transitions[(s, a)]:
                r = rewards[(s, a, s_next)]
                total += prob * (r + gamma * V[s_next])

            if total > best_value:
                best_value = total
                best_action = a

        policy[s] = best_action

    return policy

