#!/usr/bin/env python
from sys import argv

num_players = int(argv[1])
num_marbles = int(argv[2])

circle = [0, 1]
score = [0] * num_players
idx = 1
player = 0
for marble in range(2, num_marbles+1):
    if marble % 100000 == 0:
        print('marble =', marble)
    if marble % 23 == 0:
        idx = (idx - 7) % len(circle)
        score[player] += marble + circle.pop(idx)
    else:
        idx += 2
        if idx == len(circle):
            circle.append(marble)
        else:
            idx %= len(circle)
            circle.insert(idx, marble)
#    print(idx, circle)
    player = (player + 1) % num_players

print('part1:', max(score))
