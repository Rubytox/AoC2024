#!/usr/bin/env python3

import math as m

def count(value, L):
    """
    Counts occurrences of value in sorted list L.
    """
    occurrences = 0
    for element in L:
        if element == value:
            occurrences += 1
        if element > value:
            break

    return occurrences

with open("inputs") as f:
    data = f.readlines()

data = list(map(str.rstrip, data))
list1 = []
list2 = []
for el in data:
    spl = el.split(' ')
    list1.append(int(spl[0]))
    list2.append(int(spl[-1]))

list2.sort()

similarity = 0
for number in list1:
   similarity += number * count(number, list2) 

print(similarity)
