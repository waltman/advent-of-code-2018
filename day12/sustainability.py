#!/usr/bin/env python3
from sys import argv

# parse input
rules = {}
filename = argv[1]
with open(filename) as f:
    for line in f:
        line = line.rstrip()
        if len(line) == 0:
            next
        elif line[0] == 'i':
            init_state = line[15:]
        else:
            pattern = line[0:5]
            result = line[9]
            rules[pattern] = result

plants = '.' * 100 + init_state + '.' * 100
offset = -100
for gen in range(1,21):
    new_plants = '..'
    for i in range(2, len(plants)-2):
        pattern = plants[i-2:i+3]
        new_plants += rules.get(pattern, '.')
    plants = new_plants + '..'
score = 0
for i in range(len(plants)):
    if plants[i] == '#':
        score += i + offset
print('part1:', score)

# let's see if there's a pattern...
plants = '.' * 100 + init_state + '.' * 1000
offset = -100
for gen in range(1,120):
    new_plants = '..'
    for i in range(2, len(plants)-2):
        pattern = plants[i-2:i+3]
        new_plants += rules.get(pattern, '.')
    plants = new_plants + '..'
    score = 0
    for i in range(len(plants)):
        if plants[i] == '#':
            score += i + offset
    print(gen, score)
    if gen > 114:
        predict = 10600 + 80 * (gen - 114)
        print(predict)

print('part2:', 10600 + 80 * (50000000000 - 114))
