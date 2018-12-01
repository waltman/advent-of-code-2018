#!/usr/bin/env python3
from sys import argv

script, filename = argv
freq = 0
deltas = []
with open(filename) as f:
    for line in f:
        line = line.rstrip()
        freq += int(line)
        deltas.append(int(line))

print(f'resulting frequency = {freq}')

freq = 0
seen = set()
i = 0
while True:
    freq += deltas[i]
    if freq in seen:
        print(f'{freq} is first seen twice')
        break

    seen.add(freq)
    i = (i + 1) % len(deltas)
    
