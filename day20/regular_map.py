#!/usr/bin/env python3
from sys import argv
import copy

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
build_graph(graph, re, 1, START, START, [len(re)-1], matching)
print(graph)

print_graph(graph, START*2)
