#!/usr/bin/env python3

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
    # For each pair of positions:
    # 1. Compute symmetric over each other
    # 2. If in range, add to set
    n = len(antennas[frequency])
    for i in range(n):
        for j in range(n):
            # Symmetric of a over b is -a+2b
            if i != j:
                a = antennas[frequency][i]
                b = antennas[frequency][j]
                distance = b - a
                
                k = 0
                antinode = a + k*distance
                while 0 <= antinode.real < cols and 0 <= antinode.imag < rows:
                    antinodes.add(antinode)
                    k += 1
                    antinode = a + k*distance
                k = -1
                antinode = a + k*distance
                while 0 <= antinode.real < cols and 0 <= antinode.imag < rows:
                    antinodes.add(antinode)
                    k -= 1
                    antinode = a + k*distance


print(len(antinodes))

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
