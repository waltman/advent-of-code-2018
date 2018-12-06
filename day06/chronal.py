#!/usr/bin/env python3
from sys import argv
import numpy as np

def l1_dist(x, y, pt):
    return abs(x-pt[0]) + abs(y-pt[1])

DIM = 400
filename = argv[1]
pts = []
with open(filename) as f:
    for line in f:
        line = line.strip()
        pts.append([int(x) for x in line.split(", ")])

# initialize grid
grid = np.zeros((DIM, DIM))

# fill in grid with closest coord
for x in range(DIM):
    for y in range(DIM):
        best_d = 1e100
        best_idx = []
        for i in range(len(pts)):
            d = l1_dist(x, y, pts[i])
            if d < best_d:
                best_d = d
                best_idx = [i+1]
            elif d == best_d:
                best_idx.append(i+1)
        if len(best_idx) == 1:
            grid[y][x] = best_idx[0]

# 0 out the regions hitting the edge
for r in grid[0,:]:
    grid[grid == r] = 0
for r in grid[-1,:]:
    grid[grid == r] = 0
for r in grid[:,0]:
    grid[grid == r] = 0
for r in grid[:,-1]:
    grid[grid == r] = 0
print('part1:', max([len(grid[grid == p]) for p in range(1, len(pts)+1)]))
