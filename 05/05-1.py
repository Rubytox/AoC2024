#!/usr/bin/env python3

from functools import cmp_to_key

def compare(a, b, rules):
    """
    Compares a and b with respect to the rules described in rules
    """
    if a in rules:
        if b in rules[a]:
            return -1
        if b in rules:
            if a in rules[b]:
                return 1
            return 0
    return 0


with open("inputs") as f:
    rules = {}
    updates = []

    line = f.readline().rstrip()
    while line != '':
        first, second = line.split('|')
        first = int(first)
        second = int(second)

        if first in rules:
            rules[first].append(second)
        else:
            rules[first] = [second]
        line = f.readline().rstrip()

    line = f.readline().rstrip()
    while line:
        pages = line.split(',')
        pages = list(map(int, pages))
        updates.append(pages)
        line = f.readline().rstrip()

key = lambda first, second: compare(first, second, rules)
correct_updates = []
corrected_updates = []
for update in updates:
    new = sorted(update, key=cmp_to_key(key))
    if new == update:
        correct_updates.append(new)
    else:
        corrected_updates.append(new)

middle_sum = 0
for update in correct_updates:
    n = len(update)
    middle_sum += update[n//2]

print(middle_sum)

middle_sum = 0
for update in corrected_updates:
    n = len(update)
    middle_sum += update[n//2]

print(middle_sum)
