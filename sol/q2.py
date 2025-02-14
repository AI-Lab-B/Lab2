import numpy as np
import matplotlib.pyplot as plt


genomeList = []

with open('genome.txt', 'r') as f:
    genomes = f.readlines()

    for line in genomes:
        if line.strip() != '':
            genomeList = list(line.strip())


genome_length = len(genomeList)

print(genome_length)

# We'll use the parametric equations for a helix:
# x = cos(t), y = sin(t), z = t (or a scaled version of t)
# We want to span a range so that the helix makes a few turns.
t = np.linspace(0, 4 * np.pi, genome_length) # 4*pi gives about 2 turns
x = np.cos(t)
y = np.sin(t)
z = np.linspace(0, 5, genome_length) # z increases linearly to spread out the helix vertically
# Combine the coordinates into a (genome_length x 3) array
coordinates = np.column_stack((x, y, z))



# do visualization on the helix
# assign colour of your choice to each molecule like A=red,etc
# > create a 3D scatter plot as made in the guide.

# Create a figure and a 3D Axes
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the helix
ax.plot(x, y, z, color='b', alpha=0.5)

# Plot the atoms
for i, (x, y, z) in enumerate(coordinates):
    if genomeList[i] == 'A':
        ax.scatter(x, y, z, color='red', s=30)
    elif genomeList[i] == 'T':
        ax.scatter(x, y, z, color='blue', s=30)
    elif genomeList[i] == 'C':
        ax.scatter(x, y, z, color='green', s=30)
    elif genomeList[i] == 'G':
        ax.scatter(x, y, z, color='yellow', s=30)

# Set the aspect ratio of the Axes
ax.set_box_aspect([1,1,1])

plt.show()
# Save the figure

