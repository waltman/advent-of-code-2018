#!/usr/bin/env python3
from sys import argv
import re

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
        nanobot_pos.append([x, y, z])
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
    x,y,z = nb_pos
    if abs(bx-x) + abs(by-y) + abs(bz-z) <= best_r:
        in_range += 1

print('part1', in_range)

