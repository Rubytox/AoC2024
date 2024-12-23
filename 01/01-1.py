#!/usr/bin/env python3

import math as m

with open("inputs") as f:
    data = f.readlines()

data = list(map(str.rstrip, data))
list1 = []
list2 = []
for el in data:
    spl = el.split(' ')
    list1.append(int(spl[0]))
    list2.append(int(spl[-1]))

list1.sort()
list2.sort()
distances = [abs(l2 - l1) for (l1, l2) in zip(list1, list2)]

print(sum(distances))
