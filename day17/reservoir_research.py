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
#    print_grid(grid)

    # see if we can flood this area
    if grid[y][startx] == '#':
        y -= 1

        # find left wall
        for left_x in range(startx-1, -1, -1):
            if grid[y][left_x] == '#':
                break
        # find right wall
        for right_x in range(startx+1, len(grid[y])):
            if grid[y][right_x] == '#':
                break
        prev_left = left_x
        prev_right = right_x
        flooded = False
        while not flooded:
            # do we still have walls on each side?
            # find left wall
            for left_x in range(startx-1, -1, -1):
                if grid[y][left_x] == '#':
                    break
            # find right wall
            for right_x in range(startx+1, len(grid[y])):
#                print('checking right wall, y =', y, 'right_x=', right_x)
                if grid[y][right_x] == '#':
                    break

            # are we flooding?
            flooded = (left_x < prev_left) or (right_x > prev_right)
            # print(left_x, prev_left, right_x, prev_right)
            # print('flooded', flooded)

            if not flooded:
                for x in range(left_x+1, right_x):
                    grid[y][x] = '~'
                prev_left = left_x
                prev_right = right_x
                y -= 1
            else:
                # this row gets flow above prev row
                for x in range(prev_left+1, prev_right):
                    grid[y][x] = '|'

                # recursively overflow to left
                if grid[y][prev_left] == '.':
                    x = prev_left
                    while x >= 0 and grid[y][x] == '.' and grid[y+1][x] == '#':
                        grid[y][x] = '|'
                        x -= 1
                    grid[y][x] = '|'
                    fill_grid(grid, x, y)
                # recursively overflow to right
                if grid[y][prev_right] == '.':
                    x = prev_right
                    while x < len(grid[y]) and grid[y][x] == '.' and grid[y+1][x] == '#':
                        grid[y][x] = '|'
                        x += 1
                    grid[y][x] = '|'
                    fill_grid(grid, x, y)
#        print_grid(grid)

        
        

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
#        print(line, m.group(1), m.group(2), m.group(3), m.group(4))
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

#print(min_x, max_x, min_y, max_y)

# reduce grid to something printable
grid = [g[min_x-1:max_x+2] for g in grid[:max_y+2]]
#print_grid(grid)

start_x = 500 - min_x + 1;
fill_grid(grid, start_x, 0)
print_grid(grid)
tot = 0
for y in range(1, len(grid)-1):
    for x in range(len(grid[y])):
        if grid[y][x] == '~' or grid[y][x] == '|':
            tot += 1
print('part1', tot)

