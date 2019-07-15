#!/usr/bin/env python3
from sys import argv
import copy
from collections import deque

def pick_tool(g1, g2, t):
    TOOLS = [set(['c','t']),
             set(['c','n']),
             set(['t','n'])]

    if g1 == g2:
        t2 = t
    else:
        t2 = list(TOOLS[g2]&TOOLS[g1])[0]

    if t == t2:
        return t2, 1
    else:
        return t2, 8


depth, tx, ty = (int(x) for x in argv[1:])
maxx, maxy = tx+25, ty+25
geoindex = [[0] * (maxy+1) for _ in range(maxx+1)]
erosion = copy.deepcopy(geoindex)
geotype = copy.deepcopy(geoindex)

# do first row
for x in range(1, maxx+1):
    geoindex[x][0] = x * 16807
    erosion[x][0] = (geoindex[x][0] + depth) % 20183
# do first col
for y in range(1, maxy+1):
    geoindex[0][y] = y * 48271
    erosion[0][y] = (geoindex[0][y] + depth) % 20183

# now fill in the rest
for y in range(1, maxy+1):
    for x in range(1, maxx+1):
        if x == tx and y == ty:
            geoindex[x][y] = 0
        else:
            geoindex[x][y] = erosion[x][y-1] * erosion[x-1][y]
        erosion[x][y] = (geoindex[x][y] + depth) % 20183

# calculate geotypes
for x in range(maxx+1):
    for y in range(maxy+1):
        geotype[x][y] = erosion[x][y] % 3

print('map')
terrain = {0: '.', 1: '=', 2: '|'}
for y in range(maxy+1):
    for x in range(maxx+1):
        if x == 0 and y == 0:
            print('M', end='')
        elif x == tx and y == ty:
            print('T', end='')
        else:
            print(terrain[geotype[x][y]], end='')
    print()

# compute result
tot = 0
for row in geotype[:tx+1]:
    tot += sum(row[:ty+1])
print('part1', tot)

queue = deque()
best_mins = (tx+ty) * 7
queue.append((0, 0, 't', 0))
seen = {}
while len(queue) > 0:
    x, y, tool, mins = queue.popleft()
    if mins > best_mins:
        continue

    if x == tx and y == ty:
        print(x,y,tool,mins)
        print('at target!')
        if tool != 't':
            mins += 7
        if mins < best_mins:
            best_mins = mins
            print('new best of', best_mins)
        else:
            print('not new best of', best_mins)
        continue

    if x > maxx or y > maxy:
        continue

    if (x,y, tool) in seen and seen[(x,y, tool)] <= mins:
        continue
    seen[(x,y,tool)] = mins
#    print(x,y,tool,mins)

    g1 = geotype[x][y]
    # north
    if y > 0:
        t2, delta = pick_tool(g1, geotype[x][y-1], tool)
        queue.append((x, y-1, t2, mins+delta))

    # east
    if x < maxx:
        t2, delta = pick_tool(g1, geotype[x+1][y], tool)
        queue.append((x+1, y, t2, mins+delta))

    # south
    if y < maxy:
        t2, delta = pick_tool(g1, geotype[x][y+1], tool)
        queue.append((x, y+1, t2, mins+delta))

    # west
    if x > 0:
        t2, delta = pick_tool(g1, geotype[x-1][y], tool)
        queue.append((x-1, y, t2, mins+delta))

print('part2:', best_mins)
