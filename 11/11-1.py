#!/usr/bin/env python3

def blink(stones):
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            s = str(stone)
            new_stones.append(int(s[:len(s)//2]))
            new_stones.append(int(s[len(s)//2:]))
        else:
            new_stones.append(stone * 2024)
    return new_stones

def blink_recursive(stones, blinks=75):
    """
    Each stone does not interact with other stones
    Recursively study the number of stones generated
    by each stone
    """

    mem = {}
   
    def aux(stone, blinks=75):
        if blinks == 0:
            return 1

        data = (stone, blinks)

        if data in mem:
            return mem[data]

        if stone == 0:
            mem[data] = aux(1, blinks - 1)
            return mem[data]

        s = str(stone)
        if len(s) % 2 == 0:
            mem[data] = aux(int(s[:len(s)//2]), blinks - 1)
            mem[data] += aux(int(s[len(s)//2:]), blinks - 1)
            return mem[data]

        mem[data] = aux(stone * 2024, blinks - 1)
        return mem[data]

    count = 0
    for stone in stones:
        count += aux(stone, blinks)
    return count


with open("inputs") as f:
    line = f.readline().rstrip()
    stones = line.split(' ')

stones = list(map(int, stones))

import time

print("25: ", end="")
s = time.perf_counter()
count = blink_recursive(stones, 25)
delta = time.perf_counter() - s
print(count)
print("Time: " + str(delta * 1000) + "ms")

print("75: ", end="")
s = time.perf_counter()
count = blink_recursive(stones, 75)
delta = time.perf_counter() - s
print(count)
print("Time: " + str(delta * 1000) + "ms")
