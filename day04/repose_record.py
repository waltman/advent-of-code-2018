#!/usr/bin/env python3
from sys import argv
import re
from collections import defaultdict

records = []
filename = argv[1]
with open(filename) as f:
    for line in f:
        records.append(line.rstrip())

records.sort()

tot_asleep = defaultdict(int)
min_asleep = {}
guard_asleep = {}

for record in records:
    m = re.search('Guard #(\d+)', record)
    if m:
        guard = int(m.group(1))
    elif re.search('falls', record):
        asleep = int(record[15:17])
    else:
        wake = int(record[15:17])
        tot_asleep[guard] += wake - asleep
        if guard not in min_asleep:
            min_asleep[guard] = defaultdict(int)
        for minute in range(asleep, wake):
            min_asleep[guard][minute] += 1
            if minute not in guard_asleep:
                guard_asleep[minute] = defaultdict(int)
            guard_asleep[minute][guard] += 1

# fine best guard
best_guard = -1
best_time = -1
for guard, asleep in tot_asleep.items():
    if asleep > best_time:
        best_guard = guard
        best_time = asleep

# find best time for best guard
best_min = -1
best_time = -1
for minute, asleep in min_asleep[best_guard].items():
    if asleep > best_time:
        best_min = minute
        best_time = asleep
print('part 1:', best_guard * best_min)

# find best minute across all guards
best_min = -1
best_time = -1
best_guard = -1
for minute in guard_asleep:
    for guard, asleep in guard_asleep[minute].items():
        if asleep > best_time:
            best_min = minute
            best_time = asleep
            best_guard = guard

print('part 2:', best_guard * best_min)
