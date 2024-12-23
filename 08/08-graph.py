#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.animation import FuncAnimation

# Maps frequency to list of positions
antennas = {}
with open("inputs") as f:
    line = f.readline().rstrip()
    cols = len(line)
    rows = 0
    while line:
        for i, c in enumerate(line):
            if c != '.':
                if c not in antennas:
                    antennas[c] = []
                antennas[c].append(i + rows * 1j)

        line = f.readline().rstrip()
        rows += 1


antinodes = set()
for frequency in antennas:
    n = len(antennas[frequency])
    for i in range(n):
        for j in range(n):
            if i != j:
                a = antennas[frequency][i]
                b = antennas[frequency][j]
                distance = b - a
                
                k = 0
                antinode = a + k*distance
                while 0 <= antinode.real < cols and 0 <= antinode.imag < rows:
                    if antinode != a and antinode != b:
                        antinodes.add(antinode)
                    k += 1
                    antinode = a + k*distance
                k = -1
                antinode = a + k*distance
                while 0 <= antinode.real < cols and 0 <= antinode.imag < rows:
                    if antinode != a and antinode != b:
                        antinodes.add(antinode)
                    k -= 1
                    antinode = a + k*distance



mask = []
for i in range(rows):
    mask.append([])
    for j in range(cols):
        mask[i].append('.')

for a in antinodes:
    x = int(a.real)
    y = int(a.imag)
    mask[y][x] = '#'

for f in antennas:
    for value in antennas[f]:
        x = int(value.real)
        y = int(value.imag)
        mask[y][x] = f

with open("mask", "w") as f:
    for line in mask:
        f.write(''.join(line))
        f.write("\n")

fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1], frameon=False)

for f in antennas:
    x = [val.real for val in antennas[f]]
    y = [val.imag for val in antennas[f]]
    ax.scatter(x, y)
    for x_i, y_i in zip(x, y):
        ax.annotate(f, (x_i, y_i))

antinodes_l = list(antinodes)
def update(frame_number):
    # Plot antinodes
    print(frame_number)
    x = antinodes_l[frame_number].real
    y = antinodes_l[frame_number].imag 
    ax.scatter(x, y)

animation = FuncAnimation(fig, update, interval=10)
plt.show(block=False)
