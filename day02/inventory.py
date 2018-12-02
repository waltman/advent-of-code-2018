#!/usr/bin/env python3
from sys import argv
from collections import defaultdict

def count_appear(s):
    d = defaultdict(int)
    for c in s:
        d[c] += 1

    has2 = False
    has3 = False
    for _, v in d.items():
        if v == 2:
            has2 = True
        elif v == 3:
            has3 = True

    return has2, has3

def letters_in_common(s, t):
    res = ''
    for i in range(len(s)):
        if s[i] == t[i]:
            res += s[i]
    return res

num2 = 0
num3 = 0
ids = []
filename = argv[1]
with open(filename) as f:
    for line in f:
        id = line.rstrip()
        ids.append(id)
        has2, has3 = count_appear(id)
        if has2:
            num2 += 1
        if has3:
            num3 += 1

print(f'checksum = {num2 * num3}')

target_len = len(ids[0]) - 1
for i in range(len(ids)-1):
    for j in range(i+1, len(ids)):
        common = letters_in_common(ids[i], ids[j])
        if len(common) == target_len:
            print(common)
