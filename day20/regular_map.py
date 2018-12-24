#!/usr/bin/env python3
from sys import argv
import copy
import collections

def build_graph2(graph, re, start_row, start_col):
#    print('in build_graph2', re, start_row, start_col)
    row, col = start_row, start_col
    for idx in range(len(re)):
        if re[idx] == 'N':
            graph.add(f'{row},{col}:{row-1},{col}')
            graph.add(f'{row-1},{col}:{row},{col}')
            row -= 1
            idx += 1
        elif re[idx] == 'S':
            graph.add(f'{row},{col}:{row+1},{col}')
            graph.add(f'{row+1},{col}:{row},{col}')
            row += 1
            idx += 1
        elif re[idx] == 'E':
            graph.add(f'{row},{col}:{row},{col+1}')
            graph.add(f'{row},{col+1}:{row},{col}')
            col += 1
            idx += 1
        elif re[idx] == 'W':
            graph.add(f'{row},{col}:{row},{col-1}')
            graph.add(f'{row},{col-1}:{row},{col}')
            col -= 1
            idx += 1
        elif re[idx] == '$':
            break
        elif re[idx] == '(':
            # break into new paths and recurse
            paths = []
            level = 0
            start = idx+1
            for idx2 in range(idx+1, len(re)):
                if re[idx2] == '(':
                    level += 1
                elif re[idx2] == '|' and level == 0:
                    paths.append(re[start:idx2])
                    start = idx2+1
                elif re[idx2] == ')':
                    if level == 0:
                        paths.append(re[start:idx2])
                        break
                    else:
                        level -= 1
            remaining = re[idx2+1:]
#            print(paths)
#            print(remaining)
            for p in paths:
                build_graph2(graph, p+remaining, row, col)
            break
                    

def build_graph(graph, re, idx, start_row, start_col, cont_idx, matching):
    print('in build_graph', re, idx, start_row, start_col, cont_idx)
    row, col = start_row, start_col
    while True:
        if idx < len(re):
            print('looping', idx, re[idx], row, col, cont_idx)
        else:
            print('looping', idx, 'XX', row, col, cont_idx)
            return
        if re[idx] == 'N':
            # if f'{row},{col}:{row-1},{col}' in graph:
            #     break
            graph.add(f'{row},{col}:{row-1},{col}')
            graph.add(f'{row-1},{col}:{row},{col}')
            row -= 1
            idx += 1
        elif re[idx] == 'S':
            # if f'{row},{col}:{row+1},{col}' in graph:
            #     break
            graph.add(f'{row},{col}:{row+1},{col}')
            graph.add(f'{row+1},{col}:{row},{col}')
            row += 1
            idx += 1
        elif re[idx] == 'E':
            # if f'{row},{col}:{row},{col+1}' in graph:
            #     break
            graph.add(f'{row},{col}:{row},{col+1}')
            graph.add(f'{row},{col+1}:{row},{col}')
            col += 1
            idx += 1
        elif re[idx] == 'W':
            # if f'{row},{col}:{row},{col-1}' in graph:
            #     break
            graph.add(f'{row},{col}:{row},{col-1}')
            graph.add(f'{row},{col-1}:{row},{col}')
            col -= 1
            idx += 1
        elif re[idx] == '(':
            build_graph(graph, re, idx+1, row, col, cont_idx + [matching[idx]], matching)
            break
        elif re[idx] == '|':
            # if re[idx+1] != ')':
            #     build_graph(graph, re, idx+1, start_row, start_col, cont_idx, matching)
            build_graph(graph, re, idx+1, start_row, start_col, copy.deepcopy(cont_idx), matching)
            idx = cont_idx.pop() + 1
        elif re[idx] == ')':
            idx = cont_idx.pop() + 1
        elif re[idx] == '$':
            break

def print_graph(graph, size):
    print('#' * (size*2-1))
    for row in range(1,size):
        print('#', end='')
        for col in range(1,size):
            if row == size/2 and col == size/2:
                print('X', end='')
            else:
                print(' ', end='')
            if f'{row},{col}:{row},{col+1}' in graph:
                print('|', end='')
            else:
                print('#', end='')
        print()
        print('#', end='')
        for col in range(1,size):
            if f'{row},{col}:{row+1},{col}' in graph:
                print('-#', end='')
            else:
                print('##', end='')
        print()

filename = argv[1]
START = int(argv[2])
with open(filename) as f:
    re = f.read().rstrip()

# preprocess re to map out the matching parens
matching = {}
stack = []
for i in range(len(re)):
    if re[i] == '(':
        stack.append(i)
    elif re[i] == ')':
        matching[stack.pop()] = i

graph = set()
#build_graph(graph, re, 1, START, START, [len(re)-1], matching)
build_graph2(graph, re, START, START)
#print(graph)

#print_graph(graph, START*2)

# now search for longest path
q = collections.deque()
q.append((START, START, 0))
max_dist = -1
seen = set()
print('done parsing map')
while q:
    row, col, dist = q.popleft()
    seen.add((row, col))
    max_dist = max(dist, max_dist)
    # N
    if f'{row},{col}:{row-1},{col}' in graph and (row-1,col) not in seen:
        q.append((row-1, col, dist+1))
    # S
    if f'{row},{col}:{row+1},{col}' in graph and (row+1,col) not in seen:
        q.append((row+1, col, dist+1))
    # E
    if f'{row},{col}:{row},{col+1}' in graph and (row,col+1) not in seen:
        q.append((row, col+1, dist+1))
    # W
    if f'{row},{col}:{row},{col-1}' in graph and (row,col-1) not in seen:
        q.append((row, col-1, dist+1))

print('part1:', max_dist)
