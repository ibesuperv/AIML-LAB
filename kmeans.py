import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2) ** 2))

def kmeans(X, k, max_iters=100):
    np.random.seed(42)
    centroids = X[np.random.choice(len(X), k, replace=False)]
    
    for _ in range(max_iters):
        clusters = []
        for x in X:
            dist = [distance(x, c) for c in centroids]
            clusters.append(np.argmin(dist))
        clusters = np.array(clusters)
        new_centroids = []
        for i in range(k):
            new_centroids.append(X[clusters == i].mean(axis=0))
        new_centroids = np.array(new_centroids)
        if np.allclose(centroids, new_centroids):
            break
        centroids = new_centroids
    return clusters, centroids # type: ignore

data = pd.read_csv("iris.csv")

X = data.drop("class", axis=1).values

k = 3

clusters, centroids  = kmeans(X, k)
plt.scatter(X[:,2 ], X[:, 3], c=clusters,  cmap="viridis")
plt.scatter(centroids[:, 2], centroids[:, 3], color="red", marker="X", s=200)
plt.xlabel("Petal Length")
plt.ylabel("Petal Width")
plt.title("K-Means Clustering on Iris Dataset")
plt.show()
