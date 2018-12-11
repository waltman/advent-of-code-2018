#!/usr/bin/env python3
from sys import argv
import re
import numpy as np

def hundreds_digit(n):
    return int(n/100) % 10

def power_level(x, y, serial):
    rack_id = x + 10
#    print("rack_id =", rack_id)
    level = rack_id * y
#    print("level =", level)
    level += serial
#    print("level =", level)
    level *= rack_id
#    print("level =", level)
    return hundreds_digit(level) - 5

# print(power_level(3,5,8))
# print(power_level(122,79,57))
# print(power_level(217,196,39))
# print(power_level(101,153,71))

serial = int(argv[1])
DIM = 300
grid = np.zeros((DIM, DIM))
for row in range(DIM):
    for col in range(DIM):
        grid[row][col] = power_level(col, row, serial)

best_sum = -1e100
best_row = -1
best_col = -1

for row in range(DIM-2):
    for col in range(DIM-2):
        power = sum(sum(grid[row:row+3,col:col+3]))
        if power > best_sum:
            best_sum = power
            best_row = row
            best_col = col

print(f'part1: {best_col},{best_row} {int(best_sum)}')

best_sum = -1e100
best_row = -1
best_col = -1
best_size = -1

for size in range(1,DIM+1):
    if size % 10 == 0:
        print('size =', size)
    for row in range(DIM-(size-1)):
        for col in range(DIM-(size-1)):
            power = sum(sum(grid[row:row+size,col:col+size]))
            if power > best_sum:
                best_sum = power
                best_row = row
                best_col = col
                best_size = size

print(f'part2: {best_col},{best_row},{best_size} {int(best_sum)}')
