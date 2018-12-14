#!/usr/bin/env python3
from sys import argv

class Cart:
    left_turn = {
        'u': 'l',
        'r': 'u',
        'd': 'r',
        'l': 'd'
    }
    right_turn = {
        'u': 'r',
        'l': 'u',
        'd': 'l',
        'r': 'd'
    }

    def __init__(self, x, y, d):
        self.x = x
        self.y = y
        self.d = d
        self.t = 0

    def __repr__(self):
        return f'x: {self.x}, y: {self.y}, d: {self.d}, t: {self.t}'

    def move(self):
        if self.d == 'u':
            self.y -= 1
        elif self.d == 'd':
            self.y += 1
        elif self.d == 'l':
            self.x -= 1
        else:
            self.x += 1

    def turn_left(self):
        self.d = self.left_turn[self.d]

    def turn_right(self):
        self.d = self.right_turn[self.d]

    def turn(self, loc):
        if loc == '/':
            if self.d == 'u' or self.d == 'd':
                self.turn_right()
            else:
                self.turn_left()
        else:
            if self.d == 'u' or self.d == 'd':
                self.turn_left()
            else:
                self.turn_right()

    def junct(self):
        if self.t == 0:
            self.turn_left()
        elif self.t == 2:
            self.turn_right()
        self.t = (self.t+1) % 3
        

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

# for t in track:
#     print(t)

for c in sorted(carts, key=lambda cart: (cart.y,cart.x)):
    print(c)

# move carts until collision
tick = 0
done = False
while not done:
    # move and turn carts
    k = 0
#     for cart in carts:
    for cart in sorted(carts, key=lambda c: (c.y,c.x)):
        cart.move()
        loc = track[cart.y][cart.x]
        if loc == '/' or loc == '\\':
            cart.turn(loc)
        elif loc == '+':
            cart.junct()
        elif loc == ' ':
            raise IndexError(f'off the track at {cart.y},{cart.x}')
        print(f'tick={tick},k={k}, {cart}')
        k += 1
        # check for collisions
        for i in range(len(carts)-1):
            for j in range(i+1, len(carts)):
                if carts[i].x == carts[j].x and carts[i].y == carts[j].y:
                    print(f'part1: {carts[i].x},{carts[i].y}, tick={tick}, i={i}, j={j}')
                    done = True
                    break
    tick += 1

            
