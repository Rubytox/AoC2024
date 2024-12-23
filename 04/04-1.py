#!/usr/bin/env python3

with open("inputs") as f:
    data = f.readlines()


data = list(map(str.rstrip, data))

matrix = [[]] * len(data)
for index, row in enumerate(data):
    matrix[index] = list(row)

def find_neighbours(x, y, M):
    """
    Returns list of indices that are neighbours of item (x,y) 
    in matrix M of size nxn
    - (x-1, y)
    - (x+1, y)
    - (x, y-1)
    - (x, y+1)
    - (x-1, y-1)
    - (x+1, y-1)
    - (x-1, y+1)
    - (x+1, y+1)
    """
    
    n = len(M)
    neighbours = []
    if x - 1 >= 0:
        neighbours.append((x-1, y))
        if y - 1 >= 0:
            neighbours.append((x-1, y-1))
        if y + 1 < n:
            neighbours.append((x-1, y+1))
    if x + 1 < n:
        neighbours.append((x+1, y))
        if y - 1 >= 0:
            neighbours.append((x+1, y-1))
        if y + 1 < n:
            neighbours.append((x+1, y+1))
    if y - 1 >= 0:
            neighbours.append((x, y-1))
    if y + 1 < n:
        neighbours.append((x, y+1))

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
        if matrix[x][y] == 'X':
            neighboursX = find_neighbours(x, y, matrix)
            for nX in neighboursX:
                xM, yM = nX
                if matrix[xM][yM] == 'M':
                    dx, dy = (xM - x, yM - y)
                    if 0 <= xM + dx < n and 0 <= yM + dy < n:
                        if matrix[xM + dx][yM + dy] == 'A':
                            if 0 <= xM + 2*dx < n and 0 <= yM + 2*dy < n:
                                if matrix[xM + 2*dx][yM + 2*dy] == 'S':
                                    xmas_count += 1
                            #mask[x][y] = 'X'
                            #mask[xM][yM] = 'M'
                            #mask[xA][yA] = 'A'
                            #mask[xS][yS] = 'S'
#print(print_matrix(mask))
print(xmas_count)
