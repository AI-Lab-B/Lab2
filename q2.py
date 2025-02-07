import numpy as np
import matplotlib.pyplot as plt




with open("genome.txt", "r") as file:
    hehe = file.read().strip()

g_seq=list(hehe)
print(g_seq)
genome_length = len(g_seq)
print("Genome length:", genome_length)

t = np.linspace(0, 4 * np.pi, genome_length)  
x = np.cos(t)                    # x = cos(t)
y = np.sin(t)                    # y = sin(t)
z = np.linspace(0, 5, genome_length)  # z increases linearly to spread out the helix

coordinates = np.column_stack((x, y, z))




fig = plt.figure()
ax = fig.add_subplot( projection='3d')
colors = {'A': 'red', 'T': 'blue', 'C': 'hotpink', 'G': 'yellow'}
# Plot each nucleotide with its corresponding color and coordinates
for i, nucleotide in enumerate(g_seq):
 ax.scatter(coordinates[i, 0], coordinates[i, 1], coordinates[i, 2],
 color=colors[nucleotide], marker='o')



# Set the axis labels and title.
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("3D Helix Structure with Color-coded Molecules")

plt.show()

