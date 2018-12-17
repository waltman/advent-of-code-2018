#!/usr/bin/env python3
from sys import argv
import copy
import re
from collections import defaultdict

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
pgm = []

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
            if re.match('^\d', line):
                pgm.append([int(x) for x in line.split(' ')])

tot = 0
tot_possible = 0
print(len(before))
possible_opcodes = []
for _ in range(len(cmds)):
    possible_opcodes.append(set(list(cmds)))
for i in range(len(before)):
    op,a,b,c = vals[i][0:]
    possible = []
    for cmd in cmds:
        r2 = cmd(before[i], a, b, c)
        if r2 == after[i]:
            possible.append(cmd)
        else:
            possible_opcodes[op] -= set([cmd])
    if len(possible) >= 3:
        tot += 1
print('part1', tot)
for i in range(len(possible_opcodes)):
    print(i, possible_opcodes[i])
print()

# now let's see if we can trim it down to one possible opcode per number
only_one = set()
for i in range(16):
    for po in possible_opcodes:
        if len(po) == 1:
            only_one |= po
    for po in possible_opcodes:
        if len(po) > 1:
            po -= only_one
for i in range(len(possible_opcodes)):
    print(i, possible_opcodes[i])

# convert to an array (gotta be an easier way to do this)
opcode = []
for po in possible_opcodes:
    a = [x for x in po]
    opcode.append(a[0])

# run the program
regs = [0, 0, 0, 0]
for instr in pgm:
    op, a, b, c = instr[0:]
    r2 = opcode[op](regs, a, b, c)
    regs = copy.deepcopy(r2)
print('part2', regs)
