import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def read_genome_sequence(file_path):
    with open(file_path, 'r') as file:
        sequence = file.read().strip().replace("\n", "")
    return list(sequence)

def generate_helix_coordinates(genome_length, turns=5, radius=1.0):
    theta = np.linspace(0, 2 * np.pi * turns, genome_length)
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
    z = np.linspace(0, genome_length / 10, genome_length)
    return x, y, z

def assign_colors(sequence):
    color_map = {'A': 'red', 'T': 'blue', 'G': 'green', 'C': 'yellow'}
    return [color_map.get(nucleotide, 'black') for nucleotide in sequence]

def plot_helix(sequence, x, y, z, colors):
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z, c=colors, s=50, edgecolors='k', alpha=0.8)
    ax.set_title("3D Genome Visualization on a Helix")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    plt.show()

def main():
    file_path = "genome.txt"
    sequence = read_genome_sequence(file_path)
    genome_length = len(sequence)
    x, y, z = generate_helix_coordinates(genome_length)
    colors = assign_colors(sequence)
    plot_helix(sequence, x, y, z, colors)

if __name__ == "__main__":
    main()