def value_iteration(states, actions, transitions, rewards, gamma=0.9, theta=1e-6):

    #assigning value 0 to all states
    V = {s: 0 for s in states}

    #I keep updating values until they stop changing
    while True:
        delta = 0  #this will track the biggest change in this iteration

        #go through each state one by one
        for s in states:

            #if the state has no actions, we treat it as terminal and skip it
            if s not in actions:
                continue

            #store the old value so we can check how much it changes
            v = V[s]

            #I will calculate the value for each possible action
            action_values = []

            #We try all actions available in this state
            for a in actions[s]:
                total = 0

                # for each possible next state, compute expected value
                for prob, s_next in transitions[(s, a)]:
                    r = rewards[(s, a, s_next)]

                    # Bellman update: reward + discounted future value
                    total += prob * (r + gamma * V[s_next])

                action_values.append(total)

            #the best action (maximum value)
            V[s] = max(action_values)

            #update delta (how much the value changed)
            delta = max(delta, abs(v - V[s]))

        #If values are no longer changing much, we stop
        if delta < theta:
            break

    return V

