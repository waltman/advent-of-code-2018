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
    md_sum += sum(data[idx:idx+num_metadata])
    idx += num_metadata
    return idx, md_sum
    

filename = argv[1]
with open(filename) as f:
    for line in f:
        data = [int(x) for x in line.split(' ')]

idx, md_sum = walk_tree(data, 0)
print('part1', md_sum)

