#!/usr/bin/env python3
from sys import argv
from collections import defaultdict

def time_needed(step, extra):
    return ord(step) - ord('A') + 1 + extra

remaining = set()
parents = defaultdict(set)
children = defaultdict(set)

filename = argv[1]
num_workers = int(argv[2])
extra = int(argv[3])
with open(filename) as f:
    for line in f:
        step1 = line[5]
        step2 = line[36]
        remaining.add(step1)
        remaining.add(step2)
        children[step1].add(step2)
        parents[step2].add(step1)

# initialize queue with root
queue = set()
for step in remaining:
    if len(parents[step]) == 0:
        queue.add(step)
print('initial queue:', queue)

res1 = ''
sec = -1
time_left = [0 for _ in range(num_workers)]
worker_step = [' ' for _ in range(num_workers)]
done = False
while not done:
    # update timing
    sec += 1
    done = True
    for i in range(num_workers):
        if time_left[i] == 1:
            time_left[i] = 0
            step = worker_step[i]
            worker_step[i] = ' '
            # queue.remove(step)
            remaining.remove(step)
            res1 += step
            for child in children[step]:
                if child in remaining and child not in worker_step:
                    queue.add(child)
                    done = False
        elif time_left[i] > 1:
            time_left[i] -= 1
            done = False

    # try to pick a job for each worker at time 0
    for i in range(num_workers):
        if queue and time_left[i] == 0:
            
            # which to do next?
            found_step = False
            for step in sorted(queue):
                if len(parents[step] & remaining) == 0:
                    found_step = True
                    break

            if not found_step:
                continue
            
            # ok, we're picking step
            print('sec', sec, 'picking', step)
            queue.remove(step)
            time_left[i] = time_needed(step, extra)
            worker_step[i] = step
            done = False
    print(sec, res1, queue, time_left, worker_step)

print('step1:', res1)
print(sec, time_left)
print('step2:', sec + sum(time_left))
