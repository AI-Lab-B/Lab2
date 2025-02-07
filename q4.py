from sklearn.datasets import load_iris
import numpy as np
import matplotlib.pyplot as plt

iris = load_iris()
# Accessing the features (data) using NumPy array
X = np.array(iris.data) # (Features (sepal length, sepal width, petal length, petalwidth) #Accessing the target labels (species)
Y = np.array(iris.target) # Target variable (species: 0 for setosa, 1 for versicolor, 2 for virginica)
#calculates mean for each column(down the rows) (axis=0) axis=1 means across the columns(for each row)
means = np.mean(X, axis=0)

medians = np.median(X, axis=0)

stds = np.std(X, axis=0)

print("Means for each feature:", means)
print("Medians for each feature:", medians)
print("Standard deviations for each feature:", stds)

mins = np.min(X, axis=0)
maxs = np.max(X, axis=0)

print("Minimum value for each feature:", mins)
print("Maximum value for each feature:", maxs)

# sepals = X[:, :2] 
# print("Extracted sepal data (length and width):")
# print(sepals)

sepal_len=X[:, 0]
sepal_width=X[:, 1]

# scatter plot
plt.scatter(sepal_len, sepal_width)
plt.title('Iris Sepal Length vs Sepal Width')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width ')
plt.grid(True)
plt.show()

plt.hist(sepal_len, color='hotpink')
plt.xlabel('Sepal Length')
plt.ylabel('frequency distribution ')
plt.grid(True)
plt.show()


petal_len=X[:, 2]
petal_width=X[:, 3]

plt.plot(petal_len,petal_width,color='hotpink',linestyle='dashed')
plt.xlabel('petal Length')
plt.ylabel('petal widht ')
plt.grid(True)
plt.show()