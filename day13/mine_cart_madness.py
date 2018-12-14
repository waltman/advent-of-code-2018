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
        self.crashed = False

    def __repr__(self):
        return f'x: {self.x}, y: {self.y}, d: {self.d}, t: {self.t}, crashed: {self.crashed}'

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

    def crash(self):
        self.crashed = True
        self.x = 999999999
        self.y = 999999999
        

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

remaining = len(carts)

for c in sorted(carts, key=lambda cart: (cart.y,cart.x)):
    print(c)

# move carts until collision
tick = 0
done = False
while not done:
    # move and turn carts
    k = 0
    for cart in sorted(carts, key=lambda c: (c.y,c.x)):
        if cart.crashed:
            continue
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
            if carts[i].crashed:
                continue
            for j in range(i+1, len(carts)):
                if carts[j].crashed:
                    continue
                if carts[i].x == carts[j].x and carts[i].y == carts[j].y:
                    print(f'crash: {carts[i].x},{carts[i].y}, tick={tick}, i={i}, j={j}')
                    carts[i].crash()
                    carts[j].crash()
                    remaining -= 2
                    break
    if remaining == 1:
        for cart in carts:
            if not cart.crashed:
                print(f'part2: {cart.x},{cart.y}, tick={tick}')
                break
        done = True
    if remaining == 0:
        print(f'no more cars left, tick={tick}')
        done = True
    tick += 1
            
