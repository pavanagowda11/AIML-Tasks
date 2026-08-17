# Implementation of Means-End Analysis for Problem Solving

def means_end_analysis(current, goal):
    print("Initial State:", current)
    print("Goal State:", goal)

    while current != goal:
        print("\nCurrent State:", current)

        # Find the first position where current differs from goal
        difference = -1
        for i in range(len(current)):
            if current[i] != goal[i]:
                difference = i
                break

        if difference == -1:
            break

        # Apply an operator to reduce the difference
        temp = list(current)
        temp[difference] = goal[difference]
        current = ''.join(temp)

        print("Operator applied: Change position", difference + 1)
        print("New State:", current)

    print("\nGoal Reached:", current)


# Example
initial_state = "ABC"
goal_state = "BAC"

means_end_analysis(initial_state, goal_state)