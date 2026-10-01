import math

# Calculate Entropy
def entropy(data):
    total = len(data)
    counts = {}

    for row in data:
        label = row[-1]
        counts[label] = counts.get(label, 0) + 1

    ent = 0
    for count in counts.values():
        p = count / total
        ent -= p * math.log2(p)

    return ent


# Calculate Information Gain
def information_gain(data, attribute):
    total_entropy = entropy(data)

    values = set(row[attribute] for row in data)
    weighted_entropy = 0

    for value in values:
        subset = [row for row in data if row[attribute] == value]
        weighted_entropy += (len(subset) / len(data)) * entropy(subset)

    return total_entropy - weighted_entropy


# ID3 Algorithm
def id3(data, attributes):
    labels = [row[-1] for row in data]

    # If all examples have the same class
    if len(set(labels)) == 1:
        return labels[0]

    # If no attributes are left
    if not attributes:
        return max(set(labels), key=labels.count)

    # Select attribute with highest information gain
    best_attribute = max(
        attributes,
        key=lambda a: information_gain(data, a)
    )

    tree = {best_attribute: {}}

    values = set(row[best_attribute] for row in data)

    for value in values:
        subset = [row for row in data if row[best_attribute] == value]

        remaining_attributes = [
            a for a in attributes if a != best_attribute
        ]

        tree[best_attribute][value] = id3(
            subset, remaining_attributes
        )

    return tree


# Dataset
# [Outlook, Temperature, Humidity, Wind, Play]
data = [
    ['Sunny', 'Hot', 'High', 'Weak', 'No'],
    ['Sunny', 'Hot', 'High', 'Strong', 'No'],
    ['Overcast', 'Hot', 'High', 'Weak', 'Yes'],
    ['Rain', 'Mild', 'High', 'Weak', 'Yes'],
    ['Rain', 'Cool', 'Normal', 'Weak', 'Yes'],
    ['Rain', 'Cool', 'Normal', 'Strong', 'No'],
    ['Overcast', 'Cool', 'Normal', 'Strong', 'Yes'],
    ['Sunny', 'Mild', 'High', 'Weak', 'No'],
    ['Sunny', 'Cool', 'Normal', 'Weak', 'Yes'],
    ['Rain', 'Mild', 'Normal', 'Weak', 'Yes'],
    ['Sunny', 'Mild', 'Normal', 'Strong', 'Yes'],
    ['Overcast', 'Mild', 'High', 'Strong', 'Yes'],
    ['Overcast', 'Hot', 'Normal', 'Weak', 'Yes'],
    ['Rain', 'Mild', 'High', 'Strong', 'No']
]

# Attribute indexes
attributes = [0, 1, 2, 3]

# Build Decision Tree
tree = id3(data, attributes)

print("ID3 Decision Tree:")
print(tree)
