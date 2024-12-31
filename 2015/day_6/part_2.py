
from collections import defaultdict

lines = []

with open('input', 'r') as f:
    for line in f:
        splitted = line.rstrip().split()
        if splitted[0] == 'turn':
            splitted = splitted[1:3] + splitted[-1:]
        else:
            splitted = splitted[0:2] + splitted[-1:]
        lines.append(splitted)

light_mapping = defaultdict(int)

def turn_on(start, end):
    for y in range(start[0], end[0]):
        for x in range(start[1], end[1]):
            light_mapping[(y, x)] += 1


def turn_off(start, end):
    for y in range(start[0], end[0]):
        for x in range(start[1], end[1]):
            if light_mapping[(y, x)] > 0:
                light_mapping[(y, x)] -= 1

def toggle(start, end):
    for y in range(start[0], end[0]):
        for x in range(start[1], end[1]):
            light_mapping[(y, x)] += 2

for action in lines:
    start = list(map(int, action[1].split(',')))
    end = list(map(int, action[2].split(',')))

    end[0] += 1
    end[1] += 1

    if action[0] == 'on':
        turn_on(start, end)
    elif action[0] == 'off':
        turn_off(start, end)
    else:
        toggle(start, end)

print(sum(list(light_mapping.values())))
