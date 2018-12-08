#!/usr/bin/env python3
from sys import argv

def walk_tree(data, idx):
    num_children, num_metadata = data[idx:idx+2]
    idx += 2
    md_sum = 0
    for i in range(num_children):
        new_idx, child_sum = walk_tree(data, idx)
        md_sum += child_sum
        idx = new_idx
    return idx+num_metadata, md_sum+sum(data[idx:idx+num_metadata])

def value(data, idx):
    num_children, num_metadata = data[idx:idx+2]
    idx += 2
    if num_children == 0:
        return idx+num_metadata, sum(data[idx:idx+num_metadata])
    else:
        child_values = [0]
        for i in range(num_children):
            new_idx, child_value = value(data, idx)
            child_values.append(child_value)
            idx = new_idx
        metadata = data[idx:idx+num_metadata]
        md_sum = 0
        for md in metadata:
            if md <= num_children:
                md_sum += child_values[md]
        return idx+num_metadata, md_sum

filename = argv[1]
with open(filename) as f:
    for line in f:
        data = [int(x) for x in line.split(' ')]

idx, md_sum = walk_tree(data, 0)
print('part1', md_sum)

idx, value = value(data, 0)
print('part2', value)
