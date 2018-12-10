#!/usr/bin/env python
from sys import argv

class Node:
    def __init__(self, val, next_node = None, prev_node = None):
        self.val = val
        self.next_node = next_node
        self.prev_node = prev_node

class Circle_List:
    def __init__(self, node):
        self.idx = node

    def forward(self, cnt):
        """ go forward cnt nodes """
        for _ in range(cnt):
            self.idx = self.idx.next_node

    def backward(self, cnt):
        """ go backwards cnt nodes """
        for _ in range(cnt):
            self.idx = self.idx.prev_node

    def insert(self, val):
        """ insert node containing val after idx """
        next_idx = self.idx.next_node
        node = Node(val, next_idx, self.idx)
        self.idx.next_node = node
        next_idx.prev_node = node
        self.idx = node

    def remove(self):
        """ remove the node at idx """
        next_idx = self.idx.next_node
        prev_idx = self.idx.prev_node
        prev_idx.next_node = next_idx
        next_idx.prev_node = prev_idx
        self.idx = next_idx

num_players = int(argv[1])
num_marbles = int(argv[2])

score = [0] * num_players
player = 0

node = Node(0)
node.next_node = node
node.prev_node = node
circle = Circle_List(node)
start = node
num_nodes = 1

for marble in range(1, num_marbles+1):
    if marble % 100000 == 0:
        print('marble =', marble)
    if marble % 23 == 0:
        circle.backward(7)
        score[player] += marble + circle.idx.val
        circle.remove()
        num_nodes -= 1
    else:
        circle.forward(1)
        circle.insert(marble)
        num_nodes += 1
    player = (player + 1) % num_players

print('part1', max(score))
