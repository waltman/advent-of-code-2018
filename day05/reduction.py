#!/usr/bin/env python3
from sys import argv
from string import ascii_lowercase, ascii_uppercase

def reduce(polymer, remove=None):
    s = polymer
    opp = {}
    for c in ascii_lowercase:
        opp[c] = c.upper()
    for c in ascii_uppercase:
        opp[c] = c.lower()
        
    if remove:
        t = ''
        for i in range(len(s)):
            if not(s[i] == remove or s[i] == opp[remove]):
                t += s[i]
        s = t

    done = False
    while not done:
        i = 0
        t = ''
        done = True
        while i < len(s)-1:
            if s[i] == opp[s[i+1]]:
                i += 2
                done = False
            else:
                t += s[i]
                i += 1
        if i == len(s)-1:
            t += s[i]

        if not done:
            s = t
    return t
        

filename = argv[1]
with open(filename) as f:
    for line in f:
        polymer = line.strip()
        res = reduce(polymer)
        print('part1:', len(res))

        best = 1e100
        for c in ascii_lowercase:
            res = reduce(polymer, c)
            if len(res) < best:
                best = len(res)
                print(c, best)
        print('part2:', best)

