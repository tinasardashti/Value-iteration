def extract_policy(states, actions, transitions, rewards, V, gamma=0.9):

    #this will store the best action for each state
    policy = {}

    #go through each state
    for s in states:

        #skip terminal states (no actions)
        if s not in actions:
            continue

        best_action = None
        best_value = float("-inf")

        #Try all possible actions in this state
        for a in actions[s]:
            total = 0

            #compute expected value for this action
            for prob, s_next in transitions[(s, a)]:
                r = rewards[(s, a, s_next)]
                total += prob * (r + gamma * V[s_next])

            #keep track of the best action
            if total > best_value:
                best_value = total
                best_action = a

        #store best action for this state
        policy[s] = best_action

    return policy
