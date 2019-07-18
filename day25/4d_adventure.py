#!/usr/bin/env python3
from sys import argv
import networkx as nx

def l1_dist(p1, p2):
    dist = 0
    for i in range(len(p1)):
        dist += abs(p1[i] - p2[i])
    return dist

pts = []
filename = argv[1]
with open(filename) as f:
    for line in f:
        line = line.strip()
        pts.append(tuple([int(x) for x in line.split(',')]))

G = nx.Graph()
for i in range(len(pts)):
    G.add_node(pts[i])
    for j in range(i):
        if l1_dist(pts[i], pts[j]) <= 3:
            G.add_edge(pts[i], pts[j])

print('part1:', len(list(nx.connected_components(G))))
