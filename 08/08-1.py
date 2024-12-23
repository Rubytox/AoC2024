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
                sym_a_over_b = -a + 2*b
                sym_b_over_a = -b + 2*a

                # Check if they are in bounds
                if 0 <= sym_a_over_b.real < cols and 0 <= sym_a_over_b.imag < rows:
                    antinodes.add(sym_a_over_b)
                if 0 <= sym_b_over_a.real < cols and 0 <= sym_b_over_a.imag < rows:
                    antinodes.add(sym_b_over_a)

print(len(antinodes))
