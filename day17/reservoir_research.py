#!/usr/bin/env python3
from sys import argv
import re

def print_grid(grid):
    for g in grid:
        gg = []
        for i in range(len(g)):
            if g[i] == '.':
                gg.append(' ')
            else:
                gg.append(g[i])
        print(''.join(gg))
    print()

def fill_grid(grid, startx, starty):
    # go down until we hit something or 
    for y in range(starty+1, len(grid)):
        if grid[y][startx] == '.':
            grid[y][startx] = '|'
        else:
            break

    # see if we can flood this area
    if grid[y][startx] == '#' or grid[y][startx] == '~':
        y -= 1

        flooded = False
        while not flooded:
            # find left edge
            for left_x in range(startx-1, -1, -1):
                if grid[y][left_x] == '#':
                    break
                elif grid[y+1][left_x] == '.':
                    flooded = True
                    break
            # find right edge
            for right_x in range(startx+1, len(grid[y])):
                if grid[y][right_x] == '#':
                    break
                elif grid[y+1][right_x] == '.':
                    flooded = True
                    break
            if not flooded:
                for x in range(left_x+1, right_x):
                    grid[y][x] = '~'
                y -= 1
            else:
                # this row gets flow above prev row
                for x in range(left_x+1, right_x):
                    grid[y][x] = '|'

                # recursively overflow to left
                if grid[y+1][left_x] == '.':
                    grid[y][left_x] = '|'
                    fill_grid(grid, left_x, y)
                # recursively overflow to right
                if grid[y][right_x] == '.':
                    grid[y][right_x] = '|'
                    fill_grid(grid, right_x, y)

# parse input and make grid
filename = argv[1]
MAX_Y = 2000
grid = [['.'] * 2000 for _ in range(MAX_Y+1)]
grid[0][500] = '+'
min_x = 999999
min_y = 999999
max_x = -1
max_y = -1
with open(filename) as f:
    for line in f:
        m = re.match('^(.)=(\d+),.*=(\d+)\.\.(\d+)', line)
        if m.group(1) == 'x': # column
            x = int(m.group(2))
            y1 = int(m.group(3))
            y2 = int(m.group(4))
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            min_y = min(min_y, y1)
            max_y = max(max_y, y2)
            for y in range(y1, y2+1):
                grid[y][x] = '#'
        else: # row
            y = int(m.group(2))
            x1 = int(m.group(3))
            x2 = int(m.group(4))
            min_x = min(min_x, x1)
            max_x = max(max_x, x2)
            min_y = min(min_y, y)
            max_y = max(max_y, y)
            for x in range(x1, x2+1):
                grid[y][x] = '#'

# reduce grid to something printable
grid = [g[min_x-1:max_x+2] for g in grid[:max_y+2]]

# recursively flood the grid
start_x = 500 - min_x + 1;
fill_grid(grid, start_x, 0)
print_grid(grid)
tot1 = 0
tot2 = 0
for y in range(min_y, len(grid)-1):
    for x in range(len(grid[y])):
        if grid[y][x] == '~':
            tot1 += 1
        elif grid[y][x] == '|':
            tot2 += 1
print('part1', tot1+tot2)
print('part2', tot1)
