#!/usr/bin/env python3
from sys import argv
import re

class Fabric:
    def __init__(self, size):
        self.size = size
        self.grid = [[0 for col in range(size)] for row in range(size)]
        self.claims = {}

    def __str__(self):
        s = ''
        for row in range(self.size):
            for col in range(self.size):
                s += str(self.grid[row][col])
            s += '\n'
        return s

    def add_claim(self, id, coff, roff, w, h):
        self.claims[id] = (coff, roff, w, h)
        for col in range(coff, coff+w):
            for row in range(roff, roff+h):
                self.grid[row][col] += 1

    def multi_claims(self):
        cnt = 0
        for row in range(self.size):
            for col in range(self.size):
                if self.grid[row][col] > 1:
                    cnt += 1
        return cnt

    def is_intact(self, coff, roff, w, h):
        for col in range(coff, coff+w):
            for row in range(roff, roff+h):
                if self.grid[row][col] != 1:
                    return False
        return True

    def find_intact_claim(self):
        for claim in self.claims:
            (coff, roff, w, h) = self.claims[claim]
            if self.is_intact(coff, roff, w, h):
                print(f'claim {claim} is intact')


fabric = Fabric(1000)
filename = argv[1]
with open(filename) as f:
    for line in f:
        m =re.match('#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', line)
        id = m.group(1)
        coff = int(m.group(2))
        roff = int(m.group(3))
        w = int(m.group(4))
        h = int(m.group(5))
        fabric.add_claim(id, coff, roff, w, h)

print(fabric.multi_claims())

fabric.find_intact_claim()
