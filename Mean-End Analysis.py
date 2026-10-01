# Mean-End Analysis

def mean_end_analysis(current, goal):
    print("Current State:", current)
    print("Goal State:", goal)

    while current != goal:
        if current < goal:
            difference = goal - current
            print("Difference:", difference)
            print("Action: Increase value")
            current += 1
        elif current > goal:
            difference = current - goal
            print("Difference:", difference)
            print("Action: Decrease value")
            current -= 1

        print("New State:", current)
        print()

    print("Goal State Reached!")


# Example
mean_end_analysis(2, 5)
