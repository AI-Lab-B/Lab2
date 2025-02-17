import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()
X = np.array(iris.data)
Y = np.array(iris.target)

means = np.mean(X, axis=0)
medians = np.median(X, axis=0)
stds = np.std(X, axis=0)

# Find minimum and maximum values for each feature
mins = np.min(X, axis=0)
maxs = np.max(X, axis=0)

# Extract sepal length and sepal width
sepal_features = X[:, :2] 


# Print the results (optional)
print("Means:", means)
print("Medians:", medians)
print("Standard Deviations:", stds)
print("Minimums:", mins)
print("Maximums:", maxs)
print("\nSepal Features:\n", sepal_features)

# scatter plot 
plt.figure(figsize=(12, 4))
plt.subplot(1, 3, 1)
plt.scatter(X[:, 0], X[:, 1], c=Y)
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Sepal Width (cm)")
plt.title("Sepal Length vs. Sepal Width")


#  histogram 
plt.subplot(1, 3, 2)
plt.hist(X[:, 0], bins=10, edgecolor='black')
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")
plt.title("Distribution of Sepal Length")


# petal plot
plt.subplot(1, 3, 3)
plt.plot(X[:, 2], X[:, 3], marker='o', linestyle='-') 
plt.xlabel("Petal Length (cm)")
plt.ylabel("Petal Width (cm)")
plt.title("Petal Length vs. Petal Width")


plt.tight_layout()
plt.show()
