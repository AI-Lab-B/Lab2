import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from sklearn.datasets import load_iris  
import numpy as np

def q1():
    group_A = [12, 15, 14, 13, 16, 18, 19, 15, 14, 20, 17, 14, 15,40,45,50,62] 
    group_B = [12, 17, 15, 13, 19, 20, 21, 18, 17, 16, 15, 14, 16, 15]

    plt.suptitle("Group A")
    plt.boxplot(group_A, labels=['Group A'], showfliers=True) 
    plt.title('Box Plot of Group A')
    plt.ylabel('Values')
    plt.show()
    plt.savefig("Q1 GroupA plot")
    
    plt.suptitle("Group B")
    plt.boxplot(group_B, labels=['Group B'], showfliers=True) 
    plt.title('Box Plot of Group B')
    plt.ylabel('Values')
    plt.show()
    plt.savefig("Q1 GroupB plot")
    
def q2():
    file = open("genome.txt", "r")
    genome_text = file.read()
    genome_text = list(genome_text)
    genome_text.pop() #endline character
    print(genome_text)
    genome_length = len(genome_text)
    print("Length of sequence: " + str(genome_length))
    # We'll use the parametric equations for a helix: 
    #   x = cos(t), y = sin(t), z = t (or a scaled version of t) 
    # We want to span a range so that the helix makes a few turns. 
    t = np.linspace(0, 4 * np.pi, genome_length)  # 4*pi gives about 2 turns 
    x = np.cos(t) 
    y = np.sin(t) 
    z = np.linspace(0, 5, genome_length)  # z increases linearly to spread out the helix vertically 
    # Combine the coordinates into a (genome_length x 3) array 
    coordinates = np.column_stack((x, y, z)) 
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    colors = {'A': 'red', 'T': 'blue', 'C': 'green', 'G': 'orange'} 
    for i, nucleotide in enumerate(genome_text): 
        ax.scatter(coordinates[i, 0], coordinates[i, 1], coordinates[i, 2], 
                color=colors[nucleotide], marker='o') 
    
    ax.set_xlabel("X") 
    ax.set_ylabel("Y") 
    ax.set_zlabel("Z") 
    ax.set_title("Genome Visualization") 
    
    plt.show()
    plt.savefig("Q2 Genome Visualization") 
 
def q3():
    img = Image.open('stalin.jpg')
    numpydata = np.asarray(img)
    plt.imshow(np.rot90(numpydata))
    plt.title("Rotated")
    plt.show()
    plt.savefig("Q3 ROT90")
    plt.imshow(np.fliplr(numpydata))
    plt.title("Flipped")
    plt.show()
    plt.savefig("Q3 FLIPPED")
    gray_img = np.dot(numpydata[..., :3], [0.299, 0.587, 0.114]) 
    plt.imshow(gray_img, cmap='gray')
    plt.title("Gray Image")
    plt.show()
    plt.savefig("Q3 GRAY-IMAGE")
    

def q4():
    # Load the Iris dataset  
    iris = load_iris()  
    # Accessing the features (data) using NumPy array  
    X = np.array(iris.data) # (Features (sepal length, sepal width, petal length, petal width) #Accessing the target labels (species)   
    Y = np.array(iris.target) # Target variable (species: 0 for setosa, 1 for versicolor, 2 for  virginica)
    sepal_length = X[:, 0]
    sepal_width = X[:, 1]
    petal_length = X[:, 2]
    petal_width = X[:, 3]
    
    print("Mean(X): " + str(np.mean(X)))
    print("Mean(Y): " + str(np.mean(Y)))
    
    print("Median(X): " + str(np.median(X)))
    print("Median(Y): " + str(np.median(Y)))
    
    print("STD(X): " + str(np.std(X)))
    print("STD(Y): " + str(np.std(Y)))
    
    print("Min(X): " + str(np.min(X)))
    print("Min(Y): " + str(np.min(Y)))
    
    print("Max(X): " + str(np.max(X)))
    print("Max(Y): " + str(np.max(Y)))
    
    plt.scatter(sepal_length, sepal_width)
    plt.title("Sepal Length vs Sepal Width")
    plt.show()
    plt.savefig("Q4 Sepal Length vs Sepal Width")
    
    plt.hist(sepal_length, bins=30, color='skyblue', edgecolor='black')
    
    plt.xlabel('Sepal Length')
    plt.title('Histogram of Sepal Length')
    
    plt.show()
    plt.savefig("Q4 Histogram")
    
    plt.plot(petal_length, petal_width)
    plt.title("Petal Length vs Petal Width")
    plt.show()
    plt.savefig("Q4 Petal Length vs Petal Width")
    
if __name__ == "__main__":
    q4()