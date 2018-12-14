#!/usr/bin/env python3
from sys import argv

pattern = argv[1]
scores = "37"
p1 = 0
p2 = 1
while True:
    score_sum = str(int(scores[p1]) + int(scores[p2]))
    scores += score_sum
    p1 = (p1+1+int(scores[p1])) % len(scores)
    p2 = (p2+1+int(scores[p2])) % len(scores)

    start = max(0, len(scores)-10)
    p = scores[start:].find(pattern)
    if p != -1:
        print('part2', p+start)
        break
