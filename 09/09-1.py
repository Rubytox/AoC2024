#!/usr/bin/env python3

memory = []
with open("inputs") as f:
    line = f.readline().rstrip()
    free = False
    file_id = 0
    for c in line:
        number = int(c)
        if free:
            memory += ['.'] * number
        else:
            memory += [str(file_id)] * number
            file_id += 1
        free = not free

def swap(i, j, L):
    """
    Swaps L[i] and L[j]
    """
    L[i], L[j] = L[j], L[i]

def find_first_free_block(L):
    """
    Returns index of first '.'
    """
    try:
        return L.index('.')
    except ValueError:
        return None

def find_last_number(L):
    # Find index of last number
    index = len(L) - 1
    while L[index] == '.' and index >= 0:
        index -= 1
    return index


def is_organised(L):
    """
    Checks whether all free space is at the end of the list
    """
    index = find_last_number(L)
    return find_first_free_block(L[:index]) is None

def organise(L):
    while not is_organised(L):
        idx_free = find_first_free_block(L)
        idx_number= find_last_number(L)
        swap(idx_free, idx_number, L)

def checksum(L):
    """
    Computes checksum of organised list
    """
    checksum = 0
    for position, file_id in enumerate(L):
        if file_id == '.':
            break
        checksum += position * int(file_id)
    return checksum


organise(memory)
print(checksum(memory))
