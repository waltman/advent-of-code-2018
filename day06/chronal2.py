#!/usr/bin/env python3
from sys import argv
import numpy as np

def l1_dist(x, y, pt):
    return abs(x-pt[0]) + abs(y-pt[1])

DIM = 400
THRESH = 10000
filename = argv[1]
pts = []
with open(filename) as f:
    for line in f:
        line = line.strip()
        pts.append([int(x) for x in line.split(", ")])

# initialize grid
grid = np.zeros((DIM, DIM))

# set cell to 1 if dist to all pts below THRESH
for x in range(DIM):
    for y in range(DIM):
        if sum([l1_dist(x, y, p) for p in pts]) < THRESH:
            grid[y][x] = 1

print('part2:', int(sum(sum(grid))))
