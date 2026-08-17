# Implementation of Find-S Algorithm for Concept Learning

# Training data
# Attributes: Sky, Temperature, Humidity, Wind
# Last column: EnjoySport (Yes/No)

data = [
    ["Sunny", "Warm", "Normal", "Strong", "Yes"],
    ["Sunny", "Warm", "High", "Strong", "Yes"],
    ["Rainy", "Cold", "High", "Strong", "No"],
    ["Sunny", "Warm", "High", "Weak", "Yes"]
]

# Initialize the hypothesis with the most specific values
hypothesis = ["Ø", "Ø", "Ø", "Ø"]

# Find-S algorithm
for row in data:
    attributes = row[:-1]
    target = row[-1]

    # Consider only positive examples
    if target == "Yes":
        for i in range(len(hypothesis)):

            # First positive example
            if hypothesis[i] == "Ø":
                hypothesis[i] = attributes[i]

            # If values are different, generalize
            elif hypothesis[i] != attributes[i]:
                hypothesis[i] = "?"

# Display result
print("Final Hypothesis:")
print(hypothesis)