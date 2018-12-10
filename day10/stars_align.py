#!/usr/bin/env python3
from sys import argv
import re
import numpy as np

pos_list = []
vel_list = []

filename = argv[1]
with open(filename) as f:
    for line in f:
        line = line.rstrip()
        m = re.search('position=<([\d \-]+),([\d \-]+)> velocity=<([\d \-]+),([\d \-]+)>', line)
        xp = int(m.group(1))
        yp = int(m.group(2))
        xv = int(m.group(3))
        yv = int(m.group(4))
        pos_list.append([xp, yp])
        vel_list.append([xv, yv])

pos = np.array(pos_list)
vel = np.array(vel_list)

minx, miny = pos.min(0)
maxx, maxy = pos.max(0)
n = 0
while maxy - miny > 9 or (miny < 0 or maxy < 0 or minx < 0 or maxx < 0):
    pos += vel
    minx, miny = pos.min(0)
    maxx, maxy = pos.max(0)
    n += 1

minx, miny = pos.min(0)
maxx, maxy = pos.max(0)
pos -= np.array([minx, miny])
minx, miny = pos.min(0)
maxx, maxy = pos.max(0)

stars = np.zeros((maxy+1, maxx+1))
for row in range(pos.shape[0]):
    xpos, ypos = pos[row,:]
    stars[ypos][xpos] = 1

for row in range(maxy+1):
    for col in range(maxx+1):
        if stars[row][col] == 1:
            print('#', end='')
        else:
            print(' ', end='')
    print('')

print('part2:', n, 'seconds')
