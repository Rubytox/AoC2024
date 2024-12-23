#!/usr/bin/env python3

def neighbours(x, y, rows, cols):
    offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for offset in offsets:
        dx, dy = offset
        if 0 <= x + dx < rows and 0 <= y + dy < cols:
            yield (x + dx, y + dy)

def score_trailheads(x, y, M, rows, cols):
    """
    Count trailheads starting from (x,y)
    """
    seen_levels = []
    visited = set()

    def dfs(x, y):
        if M[x][y] == 9:
            seen_levels.append(9)
            return

        visited.add((x,y))

        for neighbour in neighbours(x, y, rows, cols):
            new_x, new_y = neighbour
            if M[new_x][new_y] == M[x][y] + 1:
                dfs(new_x, new_y)

        visited.remove((x,y))

    dfs(x, y)
    print(seen_levels)
    return seen_levels.count(9)


M = []
with open("inputs") as f:
    line = f.readline().rstrip()
    while line:
        M.append(list(map(int, line)))
        line = f.readline().rstrip()

rows = len(M)
cols = len(M[0])
score = 0
for x in range(rows):
    for y in range(cols):
        if M[x][y] != 0:
            continue
        score += score_trailheads(x, y, M, rows, cols)

print(score)
