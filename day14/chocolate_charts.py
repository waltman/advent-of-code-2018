#!/usr/bin/env python3
from sys import argv

stop_at = int(argv[1])
target_len = stop_at + 10
scores = [3, 7]
p1 = 0
p2 = 1
while len(scores) < target_len:
    score_sum = str(scores[p1] + scores[p2])
    for s in score_sum:
        scores.append(int(s))
    p1 = (p1+1+scores[p1]) % len(scores)
    p2 = (p2+1+scores[p2]) % len(scores)

print('part1', ''.join([str(n) for n in scores[stop_at:stop_at+10]]))

