from sklearn.datasets import load_iris

iris = load_iris()


import numpy as np
import matplotlib.pyplot as plt

# Calculate the mean, median, and standard deviation for each feature
mean = np.mean(iris.data, axis=0)
median = np.median(iris.data, axis=0)
std_dev = np.std(iris.data, axis=0)
print('Mean:', mean)
print('Median:', median)
print('Standard Deviation:', std_dev)

# Find the minimum and maximum values for each feature
min_values = np.min(iris.data, axis=0)
max_values = np.max(iris.data, axis=0)

print('Minimum Values:', min_values)
print('Maximum Values:', max_values)

# Extract only the sepal length and sepal width as a NumPy array
sepal_length_width = iris.data[:, :2]

# Create a scatter plot of sepal length vs sepal width
plt.scatter(sepal_length_width[:, 0], sepal_length_width[:, 1])
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.title('Scatter Plot of Sepal Length vs Sepal Width')
plt.show()

# Plot a histogram showing the distribution of sepal length
plt.hist(iris.data[:, 0], bins=20)
plt.xlabel('Sepal Length')
plt.ylabel('Frequency')
plt.title('Histogram of Sepal Length')
plt.show()

# Create a line plot to visualize the relationship between petal length and petal width
plt.plot(iris.data[:, 2], iris.data[:, 3])
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.title('Line Plot of Petal Length vs Petal Width')
plt.show()

