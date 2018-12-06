#!/usr/bin/env python3
from sys import argv
import numpy as np
from scipy.spatial import Voronoi

def poly_area(verts):
#    print('verts =', verts)
    tot = 0
    for i in range(len(verts)):
        j = (i+1) % len(verts)
#        print('i =', i, 'j =', j)
        tot += verts[i][0] * verts[j][1] - verts[i][1] * verts[j][0]
#        print('tot =', tot)
    return abs(tot) / 2

def vor_area(region, points):
    if len(region) == 0:
        return -1
    if -1 in region:
        return -1
    verts = [points[p] for p in region]
    return poly_area(verts)

filename = argv[1]
pts = []
with open(filename) as f:
    for line in f:
        line = line.strip()
        pts.append([int(x) for x in line.split(", ")])
print(pts)
pts = np.array(pts)
print(pts)
vor = Voronoi(pts)
print(vor.points)
print(vor.regions)
print(vor.point_region)

# print('test', poly_area([[2,1], [4,5], [7,8]]))
for region in vor.regions:
#    print(region)
    print('area =', vor_area(region, vor.vertices))
