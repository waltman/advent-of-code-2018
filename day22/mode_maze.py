#!/usr/bin/env python3
from sys import argv
import copy

depth, tx, ty = (int(x) for x in argv[1:])
maxx, maxy = tx+5, ty+5
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
for tot in range(2, maxx+maxy+1):
#    print('tot=', tot)
    for x in range(1, maxx+1):
        y = tot - x
        if y > maxy:
            continue
        if y < 1:
            break
#        print('x =', x, 'y =', y)
        if x == tx and y == ty:
            geoindex[x][y] = 0
        else:
            geoindex[x][y] = erosion[x][y-1] * erosion[x-1][y]
        erosion[x][y] = (geoindex[x][y] + depth) % 20183

# erosion at target is a special case
#erosion[tx][ty] = (geoindex[tx][ty] + depth) % 20183

# calculate geotypes
for x in range(maxx+1):
    for y in range(maxy+1):
        geotype[x][y] = erosion[x][y] % 3

# print('geoindex')
# for x in geoindex:
#     print(x)
# print('erosion')
# for x in erosion:
#     print(x)
# print('geotype')
# for x in geotype:
#     print(x)

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
for row in geotype[:ty+1]:
    tot += sum(row[:tx+1])
print('part1', tot)


