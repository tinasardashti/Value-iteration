#value iteration algorithm

def value_iteration(states, actions, transitions, rewards, gamma=0.9, theta=1e-6):

    # initialize value function (start with 0 for all states)
    V = {s: 0 for s in states}

    while True:
        delta = 0

        for s in states:

            # skip terminal states (no actions)
            if s not in actions or len(actions[s]) == 0:
                continue

            best_value = float("-inf")

            # check all actions
            for a in actions[s]:
                total = 0

                for prob, s_next in transitions[(s, a)]:
                    r = rewards[(s, a, s_next)]
                    total += prob * (r + gamma * V[s_next])

                best_value = max(best_value, total)

            # update difference
            delta = max(delta, abs(V[s] - best_value))
            V[s] = best_value

        # stop when values converge
        if delta < theta:
            break

    # after values → extract policy
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

    return V, policy

