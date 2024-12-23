#!/usr/bin/env python3

with open("inputs") as f:
    data = f.readlines()

reports = list(map(str.rstrip, data))

def is_report_safe(levels):
    if len(levels) <= 1:
        return False

    if levels[0] == levels[1]:
        return False

    increasing = levels[0] < levels[1]
    decreasing = levels[0] > levels[1]

    for i in range(len(levels) - 1):
        if levels[i] == levels[i+1]:
            return False

        diff = abs(levels[i+1] - levels[i])
        if diff < 1 or diff > 3:
            return False

        if increasing:
            if levels[i] > levels[i+1]:
                return False
        if decreasing:
            if levels[i] < levels[i+1]:
                return False
    return True

safe = 0
for report in reports:
    levels = list(map(int, report.split(' ')))

    if is_report_safe(levels):
        safe += 1
        continue

    for i in range(len(levels)):
        new_levels = [levels[j] for j in range(len(levels)) if j != i]
        if is_report_safe(new_levels):
            safe += 1
            break

print(safe)
