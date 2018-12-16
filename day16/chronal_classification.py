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

regs = [3, 2, 1, 1]
cnt = 0
for i in range(len(cmds)):
    cmd = cmds[i]
    r2 = cmd(regs, 2, 1, 2)
    print(i, regs, r2, r2 == [3,2,2,1])
    if r2 == [3,2,2,1]:
        cnt += 1
print(cnt)
