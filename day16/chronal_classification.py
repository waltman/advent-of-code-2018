#!/usr/bin/env python3
from sys import argv
import copy
import re

def addr(regs, a, b, c):
    new_regs = copy.deepcopy(regs)
    new_regs[c] = regs[a] + regs[b]
    return new_regs

def addi(regs, a, b, c):
    new_regs = copy.deepcopy(regs)
    new_regs[c] = regs[a] + b
    return new_regs

def mulr(regs, a, b, c):
    new_regs = copy.deepcopy(regs)
    new_regs[c] = regs[a] * regs[b]
    return new_regs

def muli(regs, a, b, c):
    new_regs = copy.deepcopy(regs)
    new_regs[c] = regs[a] * b
    return new_regs

def banr(regs, a, b, c):
    new_regs = copy.deepcopy(regs)
    new_regs[c] = regs[a] & regs[b]
    return new_regs

def bani(regs, a, b, c):
    new_regs = copy.deepcopy(regs)
    new_regs[c] = regs[a] & b
    return new_regs

def borr(regs, a, b, c):
    new_regs = copy.deepcopy(regs)
    new_regs[c] = regs[a] | regs[b]
    return new_regs

def bori(regs, a, b, c):
    new_regs = copy.deepcopy(regs)
    new_regs[c] = regs[a] | b
    return new_regs

def setr(regs, a, b, c):
    new_regs = copy.deepcopy(regs)
    new_regs[c] = regs[a]
    return new_regs

def seti(regs, a, b, c):
    new_regs = copy.deepcopy(regs)
    new_regs[c] = a
    return new_regs

def gtir(regs, a, b, c):
    new_regs = copy.deepcopy(regs)
    new_regs[c] = 1 if a > regs[b] else 0
    return new_regs

def gtri(regs, a, b, c):
    new_regs = copy.deepcopy(regs)
    new_regs[c] = 1 if regs[a] > b else 0
    return new_regs

def gtrr(regs, a, b, c):
    new_regs = copy.deepcopy(regs)
    new_regs[c] = 1 if regs[a] > regs[b] else 0
    return new_regs

def eqir(regs, a, b, c):
    new_regs = copy.deepcopy(regs)
    new_regs[c] = 1 if a == regs[b] else 0
    return new_regs

def eqri(regs, a, b, c):
    new_regs = copy.deepcopy(regs)
    new_regs[c] = 1 if regs[a] == b else 0
    return new_regs

def eqrr(regs, a, b, c):
    new_regs = copy.deepcopy(regs)
    new_regs[c] = 1 if regs[a] == regs[b] else 0
    return new_regs

cmds = [addr, addi,
        mulr, muli,
        banr, bani,
        borr, bori,
        setr, seti,
        gtir, gtri, gtrr,
        eqir, eqri, eqrr]

# regs = [3, 2, 1, 1]
# cnt = 0
# for i in range(len(cmds)):
#     cmd = cmds[i]
#     r2 = cmd(regs, 2, 1, 2)
#     print(i, regs, r2, r2 == [3,2,2,1])
#     if r2 == [3,2,2,1]:
#         cnt += 1
# print(cnt)

# parse the input
filename = argv[1]
before = []
vals = []
after = []
state = 1

with open(filename) as f:
    for line in f:
        line.rstrip()
        if state == 1:
            m = re.match('Before:.*(\d+), (\d+), (\d+), (\d+)', line)
            if m:
                before.append([int(x) for x in [m.group(1), m.group(2), m.group(3), m.group(4)]])
                state = 2
            else:
                state = 5
        elif state == 2:
            vals.append([int(x) for x in line.split(' ')])
            state = 3
        elif state == 3:
            m = re.match('After:.*(\d+), (\d+), (\d+), (\d+)', line)
            after.append([int(x) for x in [m.group(1), m.group(2), m.group(3), m.group(4)]])
            state = 4
        elif state == 4:
            state = 1
        elif state == 5:
            pass

tot = 0
print(len(before))
for i in range(len(before)):
    a,b,c = vals[i][1:]
#    print(a,b,c)
    cnt = 0
    for cmd in cmds:
        r2 = cmd(before[i], a, b, c)
        if r2 == after[i]:
            cnt += 1
    if cnt >= 3:
        tot += 1
print('part1', tot)
