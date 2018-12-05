#!/usr/bin/env python3
from sys import argv
import re
import numpy as np

class Fabric:
    def __init__(self, size):
        self.size = size
        self.grid = np.zeros((size, size))
        self.claims = {}

    def __str__(self):
        return str(self.grid)

    def add_claim(self, id, coff, roff, w, h):
        self.claims[id] = (coff, roff, w, h)
        self.grid[roff:roff+h][:,coff:coff+w] += 1

    def multi_claims(self):
        return len(self.grid[self.grid > 1])

    def is_intact(self, coff, roff, w, h):
        return np.array_equal(self.grid[roff:roff+h][:,coff:coff+w], np.ones((h,w)))

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
