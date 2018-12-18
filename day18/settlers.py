#!/usr/bin/env python3
from sys import argv
from collections import defaultdict
import copy

def print_forest(forest):
    for row in forest:
        print(''.join(row))
    print

def check_open(forest, row, col):
    num_trees = 0
    for r in range(row-1, row+2):
        for c in range(col-1, col+2):
            if forest[r][c] == '|':
                num_trees += 1
    return '|' if num_trees >= 3 else '.'

def check_tree(forest, row, col):
    num_lumber = 0
    for r in range(row-1, row+2):
        for c in range(col-1, col+2):
            if forest[r][c] == '#':
                num_lumber += 1
    return '#' if num_lumber >= 3 else '|'

def check_lumber(forest, row, col):
    num_trees = 0
    num_lumber = 0
    for r in range(row-1, row+2):
        for c in range(col-1, col+2):
            if r == row and c == col:
                continue
            if forest[r][c] == '#':
                num_lumber += 1
            elif forest[r][c] == '|':
                num_trees += 1
    if num_trees >= 1 and num_lumber >= 1:
        return '#'
    else:
        return '.'

def update_forest(forest):
    new_forest = copy.deepcopy(forest)
    for row in range(len(forest)):
        for col in range(len(forest[row])):
            if forest[row][col] == '.':
                new_forest[row][col] = check_open(forest, row, col)
            elif forest[row][col] == '|':
                new_forest[row][col] = check_tree(forest, row, col)
            elif forest[row][col] == '#':
                new_forest[row][col] = check_lumber(forest, row, col)
            else:
                new_forest[row][col] = ' '
    return copy.deepcopy(new_forest)

# parse input 
filename = argv[1]
minutes = int(argv[2])
forest = []
with open(filename) as f:
    for line in f:
        forest.append(line.rstrip())

# add blanks all around to make calculations simpler
tmp = [[' '] * (len(forest[0]) + 2)]
for row in forest:
    tmp.append([' '] + [c for c in row] + [' '])
tmp.append([' '] * (len(forest[0]) + 2))
forest = copy.deepcopy(tmp)
orig_forest = copy.deepcopy(forest)

for min in range(minutes):
    forest = update_forest(forest)

num_trees = 0
num_lumber = 0
for row in range(len(forest)):
    for col in range(len(forest[row])):
        if forest[row][col] == '|':
            num_trees += 1
        elif forest[row][col] == '#':
            num_lumber += 1
print('part1', num_trees * num_lumber)


# forest = copy.deepcopy(orig_forest)
# seen = {}
