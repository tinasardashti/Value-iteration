def value_iteration(states, actions, transitions, rewards, gamma=0.9, theta=1e-6):

    # initialize value function and policy
    V = {s: 0 for s in states}
    policy = {s: None for s in states}

    while True:
        delta = 0

        for s in states:

            # skip terminal states
            if s not in actions or len(actions[s]) == 0:
                continue

            old_v = V[s]

            best_value = float("-inf")
            best_action = None

            for a in actions[s]:
                total = 0

                for prob, s_next in transitions[(s, a)]:
                    r = rewards[(s, a, s_next)]
                    total += prob * (r + gamma * V[s_next])

                if total > best_value:
                    best_value = total
                    best_action = a

            V[s] = best_value
            policy[s] = best_action

            delta = max(delta, abs(old_v - V[s]))

        if delta < theta:
            break

    return V, policy

