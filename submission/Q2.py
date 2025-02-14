import numpy as np
import matplotlib.pyplot as plt

#Given a text file having helix-sequences, read that file into a genome_seqeunce, create
# a list and find its length using list() and len() built-in functions. Then use this code for
# computation of helix structure

# Read the file
file = open('genome.txt', 'r')
genome_sequence = file.read().strip()

# Create a list
helix_list = list(genome_sequence)

# Find the length of the list
helix_length = len(helix_list)

# print(helix_length)
# We'll use the parametric equations for a helix:
# x = cos(t), y = sin(t), z = t (or a scaled version of t)
# We want to span a range so that the helix makes a few turns.
t = np.linspace(0, 4 * np.pi, helix_length) # 4*pi gives about
# 2 turns
x = np.cos(t)
y = np.sin(t)
z = np.linspace(0, 5, helix_length) # z increases linearly to
# spread out the helix vertically
# Combine the coordinates into a (genome_length x 3) array
coordinates = np.column_stack((x, y, z))


# Plot the helix
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(coordinates[:, 0], coordinates[:, 1], coordinates[:, 2])

# assign colour of your choice to each molecule like A=red,etc

# Create a dictionary to map each nucleotide to a colour
nucleotide_to_color = {'A': 'red', 'T': 'blue', 'G': 'green', 'C': 'yellow'}
# Map the nucleotides to colours
colors = [nucleotide_to_color[nucleotide] for nucleotide in helix_list]
# Plot the helix with the colours
ax.scatter(coordinates[:, 0], coordinates[:, 1], coordinates[:, 2], c=colors)
# Set the aspect ratio of the plot to be equal
ax.set_aspect('equal')
# Set the axis labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
# Show the plot
plt.show()






