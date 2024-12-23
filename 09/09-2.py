#!/usr/bin/env python3

class Block:
    def __init__(self, free, file_id=None):
        self.free = free
        self.file_id = file_id
        self.organised = False

    def __str__(self):
        if self.free:
            return '.'
        return str(self.file_id)
    
    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.free == other.free and self.file_id == other.file_id
        return False

memory = []
with open("inputs") as f:
    line = f.readline().rstrip()
    free = False
    file_id = 0
    for c in line:
        number = int(c)
        if free:
            memory += [Block(free)] * number
        else:
            memory += [Block(free, file_id)] * number
            file_id += 1
        free = not free


def swap(i, j, L):
    """
    Swaps L[i] and L[j]
    """
    L[i], L[j] = L[j], L[i]

def find_first_free_blocks_before(L, count, sup):
    """
    Returns index of first '.' * count
    """
    find = [Block(True)] * count
    for idx in (i for i, e in enumerate(L) if e == Block(True)):
        if L[idx:idx+count] == find:
            return idx if idx + count <= sup else None
    return None

def find_last_unorganised_block(L):
    current_block = None
    end_index = len(L) - 1
    for block in reversed(L):
        if block != Block(True) and not block.organised:
            current_block = block
            break
        end_index -= 1

    if current_block is None:
        return None
    
    start_index = end_index
    for i in range(end_index - 1, -1, -1):
        if L[i] != current_block:
            break
        start_index -= 1
    return start_index, end_index - start_index + 1


def is_organised(L):
    free = Block(1, True)
    for block in L:
        if block != free and not block.organised:
            return False
    return True

def display(L):
    s = ""
    for block in L:
        s += str(block)
    return s


def organise(L):
    free = Block(True)
    last_block = find_last_unorganised_block(L)
    while last_block is not None:
        start_index, size = last_block
        free_index = find_first_free_blocks_before(L, size, start_index)
        if free_index is None:
            for i in range(start_index, start_index + size):
                L[i].organised = True
            last_block = find_last_unorganised_block(L)
            continue

        offset = 0
        for i in range(start_index, start_index + size):
            swap(i, free_index + offset, L)
            offset += 1
            L[i].organised = True
        last_block = find_last_unorganised_block(L)


def checksum(L):
    """
    Computes checksum of organised list
    """
    checksum = 0
    for position, block in enumerate(L):
        if block == Block(True):
            continue
        checksum += position * block.file_id
    return checksum

organise(memory)
print(checksum(memory))
