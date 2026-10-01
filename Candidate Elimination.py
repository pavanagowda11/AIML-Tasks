# Candidate Elimination Algorithm

# Training data
data = [
    ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change', 'No'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change', 'Yes']
]

# Initialize S and G
S = ['0', '0', '0', '0', '0', '0']
G = [['?', '?', '?', '?', '?', '?']]

print("Initial S:", S)
print("Initial G:", G)

# Process each training example
for example in data:
    attributes = example[:-1]
    label = example[-1]

    if label == 'Yes':
        # Generalize S
        for i in range(len(S)):
            if S[i] == '0':
                S[i] = attributes[i]
            elif S[i] != attributes[i]:
                S[i] = '?'

        # Remove inconsistent hypotheses from G
        G = [g for g in G if all(
            g[i] == '?' or g[i] == attributes[i]
            for i in range(len(attributes))
        )]

    else:
        # Remove hypotheses from G that cover negative example
        G = [g for g in G if not all(
            g[i] == '?' or g[i] == attributes[i]
            for i in range(len(attributes))
        )]

    print("\nExample:", example)
    print("S =", S)
    print("G =", G)

print("\nFinal Specific Boundary S:", S)
print("Final General Boundary G:", G)
