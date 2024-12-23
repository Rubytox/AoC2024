#!/usr/bin/env python3

with open("instructions") as f:
    data = f.readlines()

data = list(map(str.rstrip, data))

instructions = []
skip = False
for line in data:
    if line == "do(":
        skip = False
        continue

    if line == "don't(":
        skip = True
        continue

    if not skip:
        instructions.append(line)

with open("instructions_cleaned", "w") as f:
    for line in instructions:
        f.write(line)
        f.write("\n")
