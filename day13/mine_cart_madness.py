#!/usr/bin/env python3
from sys import argv

class Cart:
    def __init__(self, x, y, d):
        self.x = x
        self.y = y
        self.d = d
        self.turn = 0

    def __repr__(self):
        return f'x: {self.x}, y: {self.y}, d: {self.d}, turn: {self.turn}'

# parse input
track = []
filename = argv[1]
with open(filename) as f:
    for line in f:
        track.append(line.rstrip())

# find carts on track
carts = []
for y in range(len(track)):
    for x in range(len(track[y])):
        if track[y][x] == '^':
            carts.append(Cart(x, y, 'u'))
            track[y] = track[y][:x] + '|' + track[y][x+1:]
        elif track[y][x] == 'v':
            carts.append(Cart(x, y, 'd'))
            track[y] = track[y][:x] + '|' + track[y][x+1:]
        elif track[y][x] == '>':
            carts.append(Cart(x, y, 'r'))
            track[y] = track[y][:x] + '-' + track[y][x+1:]
        elif track[y][x] == '<':
            carts.append(Cart(x, y, 'l'))
            track[y] = track[y][:x] + '-' + track[y][x+1:]

# move carts until collision
tick = 1
while True:
    for cart in carts:
        
