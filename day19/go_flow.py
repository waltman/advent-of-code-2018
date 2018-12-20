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

cmds = {'addr': addr,
        'addi': addi,
        'mulr': mulr,
        'muli': muli,
        'banr': banr,
        'bani': bani,
        'borr': borr,
        'bori': bori,
        'setr': setr,
        'seti': seti,
        'gtir': gtir,
        'gtri': gtri,
        'gtrr': gtrr,
        'eqir': eqir,
        'eqri': eqri,
        'eqrr': eqrr}

# parse the input
filename = argv[1]
pgm = []
ipr = -1
pgms = []
with open(filename) as f:
    for line in f:
        line = line.rstrip()
        if line[0] == '#':
            ipr = int(line[4])
        else:
            arr = line.split(' ')
            pgm.append([cmds[arr[0]], int(arr[1]), int(arr[2]), int(arr[3])])
            pgms.append(line)

# # run the program
# ip = 0
# regs = [0] * 6
# while ip >= 0 and ip < len(pgm):
#     inst = pgm[ip]
#     f, a, b, c = inst[0:]
#     regs[ipr] = ip
#     r2 = f(regs, a, b, c)
# #    print(f'ip={ip} {regs} {pgms[ip]} {r2}')
#     ip = r2[ipr]+1
#     regs = copy.deepcopy(r2)

# print('part1:', regs[0])

# run the program again with different registers for part2
# (I bet this is going to take forever...)
ip = 0
regs = [0] * 6
regs[0] = 1
while ip >= 0 and ip < len(pgm):
    inst = pgm[ip]
    f, a, b, c = inst[0:]
    regs[ipr] = ip
    r2 = f(regs, a, b, c)
#    print(f'ip={ip} {regs} {pgms[ip]} {r2}')
    ip = r2[ipr]+1
    regs = copy.deepcopy(r2)

print('part2:', regs[0])
