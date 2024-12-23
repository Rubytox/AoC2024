#!/usr/bin/env python3

from copy import deepcopy
import threading

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
    if map[new_x][new_y] == '#' or map[new_x][new_y] == 'O':
        # Rotate and move
        direction = rotate(direction)
        return move(x, y, direction, map)
    
    # 3. Guard can move
    return (new_x, new_y, direction)


def walk(initial_x, initial_y, initial_dir, map):
    """
    Walks the graph and returns the list of seens positions
    """
    seen = set()
    guard_x = initial_x
    guard_y = initial_y
    guard_dir = initial_dir
    
    #seen.add((guard_x, guard_y))
    new_coord = move(guard_x, guard_y, guard_dir, map)
    while new_coord:
        new_x, new_y, new_dir = new_coord
        guard_dir = new_dir
        guard_x = new_x
        guard_y = new_y
        seen.add((guard_x, guard_y))
        new_coord = move(guard_x, guard_y, guard_dir, map)
    return seen

def is_loop(initial_x, initial_y, initial_dir, xO, yO, map):
    map[xO][yO] = 'O'
    # Check if guard loops
    # 2 outcomes:
    # - guard leaves room
    # - guard loops i.e. moves to start point with same direction
    #   tip: update direction before checking

    guard_x = initial_x
    guard_y = initial_y
    guard_dir = initial_dir
    
    successive_positions = [(guard_x, guard_y, guard_dir)]
    new_coord = move(guard_x, guard_y, guard_dir, map)
    while new_coord:
        new_x, new_y, new_dir = new_coord
        guard_dir = new_dir
        guard_x = new_x
        guard_y = new_y
        if (guard_x, guard_y, guard_dir) in successive_positions:
            return True
        
        successive_positions.append((guard_x, guard_y, guard_dir))
        new_coord = move(guard_x, guard_y, guard_dir, map)
    return False

def split_range(M, N):
    """
    Splits the range [0, M[ into N subranges as evenly as possible.
    Returns a list of (start, end) tuples representing subranges.
    """
    chunk_size = M // N
    remainder = M % N
    ranges = []
    start = 0

    for i in range(N):
        end = start + chunk_size + (1 if i < remainder else 0)
        ranges.append((start, end))
        start = end

    return ranges

initial_x = guard_x
initial_y = guard_y
initial_dir = guard_dir

candidates = walk(guard_x, guard_y, guard_dir, M)
candidates_list = list(candidates)
nb_candidates = len(candidates)

nb_threads = 16
threads = []
number_of_looping_obstacles = [0] * nb_threads

ranges = split_range(nb_candidates, nb_threads)

def worker(initial_x, initial_y, initial_dir, indices, map, thread_id):
    global candidates_list
    global number_of_looping_obstacles
    nb = indices[1] - indices[0]
    j = 1
    for i in range(indices[0], indices[1]):
        xO, yO = candidates_list[i]
        j += 1
        if M[xO][yO] != '.':
            continue

        if is_loop(initial_x, initial_y, initial_dir, xO, yO, deepcopy(map)):
            number_of_looping_obstacles[thread_id] += 1

for i in range(nb_threads):
    t = threading.Thread(target=worker, args=(initial_x, initial_y, initial_dir, ranges[i], M, i))
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()

print(sum(number_of_looping_obstacles))
