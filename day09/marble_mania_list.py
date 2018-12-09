#!/usr/bin/env python
from sys import argv

class Node:
    def __init__(self, val):
        self.val = val
        self.next_node = None
        self.prev_node = None

num_players = int(argv[1])
num_marbles = int(argv[2])

score = [0] * num_players
player = 0

node = Node(0)
node.next_node = node
node.prev_node = node
idx = node
start = node
num_nodes = 1

for marble in range(1, num_marbles+1):
    if marble % 100000 == 0:
        print('marble =', marble)
    if marble % 23 == 0:
        for _ in range(7):
            idx = idx.prev_node
        score[player] += marble + idx.val
        next_idx = idx.next_node
        prev_idx = idx.prev_node
        prev_idx.next_node = next_idx
        next_idx.prev_node = prev_idx
        idx = next_idx
        num_nodes -= 1
    else:
        idx = idx.next_node
        next_idx = idx.next_node
        node = Node(marble)
        node.next_node = next_idx
        node.prev_node = idx
        idx.next_node = node
        next_idx.prev_node = node
        idx = node
        num_nodes += 1
    player = (player + 1) % num_players

print('part1', max(score))
