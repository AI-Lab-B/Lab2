
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris


 # numpy array:

# Load the Iris dataset
iris = load_iris()
# Accessing the features (data) using NumPy array
X = np.array(iris.data) # (Features (sepal length, sepal width, petal length, petal width) #Accessing the target labels (species)
Y = np.array(iris.target) # Target variable (species: 0 for setosa, 1 for versicolor, 2 for virginica)



# 1. Use NumPy to:
# o Calculate the mean, median, and standard deviation for each
# feature. o Find the minimum and maximum values for each feature.
# o Extract only the sepal length and sepal width as a NumPy


mean = np.mean(X, axis=0)
median = np.median(X, axis=0)

std_dev = np.std(X, axis=0)
min_val = np.min(X, axis=0)
max_val = np.max(X, axis=0)

sepal_length_width = X[:, :2]


print('Mean:', mean)
print('Median:', median)
print('Standard Deviation:', std_dev)
print('Minimum:', min_val)
print('Maximum:', max_val)

# print('Sepal Length and Width:', sepal_length_width)


plt.scatter(sepal_length_width[:, 0], sepal_length_width[:, 1], c=Y)
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.title('Scatter Plot of Sepal Length vs Sepal Width')
plt.show()


plt.hist(X[:, 0], bins=20, color='skyblue', edgecolor='black')
plt.xlabel('Sepal Length')
plt.ylabel('Frequency')
plt.title('Distribution of Sepal Length')
plt.show()


plt.plot(X[:, 2], iris.data[:, 3])
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.title('Line Plot of Petal Length and Petal Width')
plt.show()



