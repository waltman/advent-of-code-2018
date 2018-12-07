#!/usr/bin/env python3
from sys import argv
from collections import defaultdict

remaining = set()
parents = defaultdict(set)
children = defaultdict(set)

filename = argv[1]
with open(filename) as f:
    for line in f:
        step1 = line[5]
        step2 = line[36]
        remaining.add(step1)
        remaining.add(step2)
        children[step1].add(step2)
        parents[step2].add(step1)

# initialize queue with root
queue = set()
for step in remaining:
    if len(parents[step]) == 0:
        queue.add(step)

res1 = ''
while queue:
    # which to do next?
    for step in sorted(queue):
        if len(parents[step] & remaining) == 0:
            break

    # ok, we're picking step
    queue.remove(step)
    remaining.remove(step)
    res1 += step
    for child in children[step]:
        if child in remaining:
            queue.add(child)

print('step1:', res1)

