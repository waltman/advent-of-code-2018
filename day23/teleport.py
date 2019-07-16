#!/usr/bin/env python3
from sys import argv
import re

def l1_dist(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1]) + abs(p1[2]-p2[2])

def in_range_p(p1, p2, r):
    return l1_dist(p1, p2) <= r

nanobot_pos = []
nanobot_r = []
filename = argv[1]
with open(filename) as f:
    for line in f:
        m = re.match('pos=<(-?\d+),(-?\d+),(-?\d+)>, r=(\d+)', line)
        x = int(m.group(1))
        y = int(m.group(2))
        z = int(m.group(3))
        r = int(m.group(4))
        nanobot_pos.append((x, y, z))
        nanobot_r.append(r)

best_r = -1
best_idx = -1
for idx in range(len(nanobot_r)):
    if nanobot_r[idx] > best_r:
        best_r = nanobot_r[idx]
        best_idx = idx

in_range = 0
bx,by,bz = nanobot_pos[best_idx]
for nb_pos in nanobot_pos:
    if l1_dist((bx,by,bz), (nb_pos)) <= best_r:
        in_range += 1

print('part1', in_range)
