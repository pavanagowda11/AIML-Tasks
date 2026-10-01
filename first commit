# K-Means Clustering Algorithm

import numpy as np
from sklearn.cluster import KMeans

# Dataset
data = np.array([
    [1, 2],
    [1, 4],
    [2, 3],
    [8, 8],
    [9, 10],
    [10, 9]
])

# Create K-Means model
kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)

# Train the model
kmeans.fit(data)

# Print cluster centers
print("Cluster Centers:")
print(kmeans.cluster_centers_)

# Print cluster labels
print("\nCluster Labels:")
print(kmeans.labels_)

# Predict clusters
print("\nPredicted Clusters:")
for point, label in zip(data, kmeans.labels_):
    print(point, "-> Cluster", label)
