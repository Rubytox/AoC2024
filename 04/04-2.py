#!/usr/bin/env python3

with open("inputs") as f:
    data = f.readlines()


data = list(map(str.rstrip, data))

matrix = [[]] * len(data)
for index, row in enumerate(data):
    matrix[index] = list(row)

def find_neighbours_diag(x, y, M):
    """
    Returns list of indices that are neighbours of item (x,y) 
    in matrix M of size nxn
    - (x-1, y-1)
    - (x+1, y-1)
    - (x-1, y+1)
    - (x+1, y+1)
    """
    
    n = len(M)
    neighbours = []
    if x - 1 >= 0:
        if y - 1 >= 0:
            neighbours.append((x-1, y-1))
        if y + 1 < n:
            neighbours.append((x-1, y+1))
    if x + 1 < n:
        if y - 1 >= 0:
            neighbours.append((x+1, y-1))
        if y + 1 < n:
            neighbours.append((x+1, y+1))

    return neighbours

def found_xmas(x, y, M, next):
    """
    Starting from position (x,y) in M of size nxn,
    looks for the word XMAS and counts 1 when found
    """
    if M[x][y] == 'S':
        return True

def print_matrix(M):
    str = ""
    for row in M:
        for col in row:
            str += col
        str += "\n"
    return str
    

xmas_count = 0
n = len(matrix)
mask = [['.'] * n] * n

for x in range(n):
    for y in range(n):
        if matrix[x][y] == 'A':
            neighbours = find_neighbours_diag(x, y, matrix)
            if len(neighbours) != 4:
                continue
            
            if ((matrix[x-1][y-1] == 'M' and matrix[x+1][y+1] == 'S') or (matrix[x-1][y-1] == 'S' and matrix[x+1][y+1] == 'M')) and ((matrix[x+1][y-1] == 'M' and matrix[x-1][y+1] == 'S') or (matrix[x+1][y-1] == 'S' and matrix[x-1][y+1] == 'M')):
                xmas_count += 1


print(xmas_count)
