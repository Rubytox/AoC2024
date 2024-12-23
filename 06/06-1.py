#!/usr/bin/env python3

with open("inputs") as f:
    data = f.readlines()

data = list(map(str.rstrip, data))

M = []
for line in data:
    M.append(list(line))

n = len(M)
guard_x = -1
guard_y = -1
guard_dir = '^'
for x in range(n):
    for y in range(n):
        if M[x][y] == '^':
            guard_x = x
            guard_y = y
            break

def dir_to_vec(direction):
    match direction:
        case '^':
            return (-1, 0)
        case '>':
            return (0, 1)
        case '<':
            return (0, -1)
        case _:
            return (1, 0)

def rotate(direction):
    match direction:
        case '^':
            return '>'
        case '>':
            return 'v'
        case 'v':
            return '<'
        case '<':
            return '^'

def move(x, y, direction, map):
    """
    3 cases:
    1. Guard can move
    2. There is an obstacle -> rotate then move
    3. Guard is at the edge of map
    """
    rows = len(map)
    cols = len(map[0])
    dx, dy = dir_to_vec(direction)

    new_x = x+dx
    new_y = y+dy

    # 1. Check if guard is about to leave
    if new_x < 0 or new_x >= rows or new_y < 0 or new_y >= cols:
        return None

    # 2. Check if there is an obstacle
    if map[new_x][new_y] == '#':
        # Rotate and move
        direction = rotate(direction)
        return move(x, y, direction, map)
    
    # 3. Guard can move
    return (new_x, new_y, direction)

new_coord = move(guard_x, guard_y, guard_dir, M)
while new_coord:
    new_x, new_y, new_dir = new_coord
    M[guard_x][guard_y] = 'X'
    guard_x = new_x
    guard_y = new_y
    guard_dir = new_dir
    new_coord = move(guard_x, guard_y, guard_dir, M)
M[guard_x][guard_y] = 'X'
number_X = 0
for rows in M:
    for el in rows:
        if el == 'X':
            number_X += 1
print(number_X)
