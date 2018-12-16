#!/usr/bin/env python3
from sys import argv
import copy
from collections import deque

class Unit:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.hp = 200
        self.alive = True

    def sort_key(self):
        return self.row, self.col

    def move(self, d):
        if d == 'u':
            self.row -= 1
        elif d == 'd':
            self.row += 1
        elif d == 'l':
            self.col -= 1
        elif d == 'r':
            self.col += 1

    def find_in_range(self, grid, enemies):
        in_range = set()
        for e in enemies:
            if not e.alive:
                continue
            if grid[e.row-1][e.col] == '.':
                in_range.add((e.row-1,e.col))
            if grid[e.row+1][e.col] == '.':
                in_range.add((e.row+1,e.col))
            if grid[e.row][e.col-1] == '.':
                in_range.add((e.row,e.col-1))
            if grid[e.row][e.col+1] == '.':
                in_range.add((e.row,e.col+1))
        return in_range

    def move_dir(self, grid, enemies):
        in_range = self.find_in_range(grid, enemies)

        # if we're already next to an enemy, don't move
        if grid[self.row-1][self.col] == self.enemy:
            return ' '
        if grid[self.row+1][self.col] == self.enemy:
            return ' '
        if grid[self.row][self.col-1] == self.enemy:
            return ' '
        if grid[self.row][self.col+1] == self.enemy:
            return ' '

        # initialize queue with our neighbors
        queue = deque()
        visited = set()
        if grid[self.row-1][self.col] == '.':
            queue.append((self.row-1,self.col, 'u', 1))
            visited.add((self.row-1,self.col,'u'))
        if grid[self.row][self.col-1] == '.':
            queue.append((self.row,self.col-1, 'l', 1))
            visited.add((self.row,self.col-1,'l'))
        if grid[self.row][self.col+1] == '.':
            queue.append((self.row,self.col+1, 'r', 1))
            visited.add((self.row,self.col+1,'r'))
        if grid[self.row+1][self.col] == '.':
            queue.append((self.row+1,self.col, 'd', 1))
            visited.add((self.row+1,self.col,'d'))

        # loop until we find a point in in_range, or we hit the end
        # of the queue
        res = ' '
        dir_score = {
            'u': 4,
            'l': 3,
            'r': 2,
            'd': 1,
            ' ': 0
        }
        best_dist = 999999
        while len(queue) > 0:
            r, c, d, dist = queue.popleft()
            # if dist > best_dist:
            #     break
            if dist > best_dist:
                continue
            if (r,c) in in_range and dir_score[d] > dir_score[res]:
                if res != ' ':
                    print('override', r, c, d, dist)
                # print('override', r, c, d, dist)
                res = d
                best_dist = dist
            else:
                if grid[r-1][c] == '.' and (r-1,c,d) not in visited:
                    queue.append((r-1,c,d,dist+1))
                    visited.add((r-1,c,d))
                if grid[r][c-1] == '.' and (r,c-1,d) not in visited:
                    queue.append((r,c-1,d,dist+1))
                    visited.add((r,c-1,d))
                if grid[r][c+1] == '.' and (r,c+1,d) not in visited:
                    queue.append((r,c+1,d,dist+1))
                    visited.add((r,c+1,d))
                if grid[r+1][c] == '.' and (r+1,c,d) not in visited:
                    queue.append((r+1,c,d,dist+1))
                    visited.add((r+1,c,d))

#        print('returning', res)
        return res

    def hit(self):
        self.hp -= 3
        if self.hp <= 0:
            self.alive = False
            self.row = 99999
            self.col = 99999

    def attack(self, grid, enemies):
        targets = []
        for e in enemies:
            if not e.alive:
                continue
            if self.row == e.row-1 and self.col == e.col:
                targets.append(e)
            elif self.row == e.row+1 and self.col == e.col:
                targets.append(e)
            elif self.row == e.row and self.col == e.col-1:
                targets.append(e)
            elif self.row == e.row and self.col == e.col+1:
                targets.append(e)

        low_hp = 999
        low_enemy = None
        for e in sorted(targets, key=lambda x: x.sort_key()):
            if e.hp < low_hp:
                low_hp = e.hp
                low_enemy = e
        # if len(targets) > 1:
        #     print('targets=')
        #     for t in targets:
        #         print(t)
        #     print('low_hp=', low_hp, 'low_enemy=', low_enemy)
        if low_enemy:
            print('hitting!')
            low_enemy.hit()
            if low_enemy.hp != low_hp-3:
                print(f"WTF!")
        else:
            print('skipping')    
        

class Elf(Unit):
    def __init__(self, row, col):
        super().__init__(row, col)
        self.sym = 'E'
        self.enemy = 'G'

    def __repr__(self):
        return f'Elf: row={self.row}, col={self.col}, hp={self.hp}, alive={self.alive}'

class Goblin(Unit):
    def __init__(self, row, col):
        super().__init__(row, col)
        self.sym = 'G'
        self.enemy = 'E'

    def __repr__(self):
        return f'Goblin: row={self.row}, col={self.col}, hp={self.hp}, alive={self.alive}'

def make_grid(cave, units):
    grid = copy.deepcopy(cave)
    for u in units:
        if u.alive:
            grid[u.row] = grid[u.row][:u.col] + u.sym + grid[u.row][u.col+1:]
    return grid

def print_grid(cave, units):
    grid = make_grid(cave, units)
    for row in grid:
        print(row)
    print()

def score(units, rnd):
    tot = 0
    for u in units:
        if u.alive:
            tot += u.hp
    print(f'tot={tot}, rnd={rnd}')
    return tot * rnd

# parse cave map
cave = []
filename = argv[1]
with open(filename) as f:
    for line in f:
        cave.append(line.rstrip())

# find elves and goblins on map
elves = []
goblins = []
for row in range(len(cave)):
    for col in range(len(cave[row])):
        if cave[row][col] == 'E':
            elves.append(Elf(row, col))
            cave[row] = cave[row][:col] + '.' + cave[row][col+1:]
        elif cave[row][col] == 'G':
            goblins.append(Goblin(row, col))
            cave[row] = cave[row][:col] + '.' + cave[row][col+1:]
units = elves + goblins

# for u in units:
#     print(u.row, u.col, u.sym)
# print()
# for u in sorted(units, key=lambda x: x.sort_key()):
#     print(u.row, u.col, u.sym)

rnd = 0
done = False
while not done:
    ulist = [u for u in sorted(units, key=lambda x: x.sort_key())]
#    for u in sorted(units, key=lambda x: x.sort_key()):
    for u in ulist:
        print(u)
    for u in ulist:
        num_elves = len([x for x in filter(lambda u: u.alive, elves)])
        num_goblins = len([x for x in filter(lambda u: u.alive, goblins)])
        if num_elves == 0 or num_goblins == 0:
            done = True
            break

        if not u.alive:
            continue

        grid = make_grid(cave, units)
        if u.sym == 'E':
            d = u.move_dir(grid, goblins)
        else:
            d = u.move_dir(grid, elves)
        u.move(d)
        grid = make_grid(cave, units)
        if u.sym == 'E':
            u.attack(grid, goblins)
        else:
            u.attack(grid, elves)
            
    rnd += 1
    num_elves = len([x for x in filter(lambda u: u.alive, elves)])
    num_goblins = len([x for x in filter(lambda u: u.alive, goblins)])
    print('round', rnd, 'num_elves', num_elves, 'num_goblins', num_goblins)
    print_grid(cave, units)
    # for u in sorted(units, key=lambda x: x.sort_key()):
    #     if u.alive:
    #         print(u)
    print()

if num_elves == 0:
#    print('part1', score(goblins, rnd-2))
    print('part1', score(goblins, rnd-1))
else:
#    print('part1', score(elves, rnd-2))
    print('part1', score(elves, rnd-1))
