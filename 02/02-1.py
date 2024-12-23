#!/usr/bin/env python3

with open("inputs") as f:
    data = f.readlines()

reports = list(map(str.rstrip, data))

unsafe = 0
for report in reports:
    levels = list(map(int, report.split(' ')))

    if len(levels) <= 1:
        continue

    if levels[0] == levels[1]:
        unsafe += 1
        continue

    increasing = levels[0] < levels[1]
    decreasing = levels[0] > levels[1]

    for i in range(len(levels) - 1):
        if levels[i] == levels[i+1]:
            unsafe += 1
            break

        diff = abs(levels[i+1] - levels[i])
        if diff < 1 or diff > 3:
            unsafe += 1
            break

        if increasing:
            if levels[i] > levels[i+1]:
                unsafe += 1
                break
        if decreasing:
            if levels[i] < levels[i+1]:
                unsafe += 1
                break

print(len(reports) - unsafe)
