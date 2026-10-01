# Naive Bayes Algorithm

from sklearn.naive_bayes import GaussianNB
import numpy as np

# Training data
X = np.array([
    [1, 20],
    [2, 21],
    [3, 22],
    [8, 30],
    [9, 31],
    [10, 32]
])

# Class labels
y = np.array([0, 0, 0, 1, 1, 1])

# Create Naive Bayes model
model = GaussianNB()

# Train the model
model.fit(X, y)

# Test data
test = np.array([
    [2, 20],
    [9, 30]
])

# Prediction
prediction = model.predict(test)

print("Predicted Classes:")
print(prediction)
