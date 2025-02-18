import numpy as np
import matplotlib.pyplot as plt
file = open("genome.txt", "r")
g_text = file.read()
g_text= list(g_text)
g_length = len(g_text)
print(g_text)

t = np.linspace(0, 4 * np.pi, g_length) 
x = np.cos(t)
y = np.sin(t)
z = np.linspace(0, 5, g_length)
coordinates = np.column_stack((x, y, z))

fig = plt.figure() 
ax = fig.add_subplot(projection='3d')
colors = {'A': 'red', 'T': 'blue', 'C': 'green', 'G': 'orange'}
for i, nucleotide in enumerate(g_text): 
    ax.scatter(coordinates[i, 0], coordinates[i, 1], coordinates[i, 2], 
    color=colors[nucleotide], marker='o') 
ax.set_xlabel("X") 
ax.set_ylabel("Y") 
ax.set_zlabel("Z") 
ax.set_title("Genome Visualization") 
<<<<<<< HEAD
<<<<<<< HEAD
#plt.show()
plt.savefig("Question2")
=======
plt.show()
plt.savefig("Genome Visualization")
>>>>>>> 4785f2f043781628b8d3ac5b770f467e24c323d6
=======
plt.show()
plt.savefig("Genome Visualization")
>>>>>>> 4785f2f043781628b8d3ac5b770f467e24c323d6
