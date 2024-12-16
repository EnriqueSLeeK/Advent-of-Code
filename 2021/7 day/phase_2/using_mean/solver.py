from statistics import mean
from math import floor, ceil

with open("input", "r") as f:
    crab_position = [int(crab) for crab in f.read().split(',')]

mean_dist = mean(crab_position)

dist = [floor(mean_dist), ceil(mean_dist)]

def progression_sum(steps):
    return ((1 + steps) * steps) // 2

total_cost = [0, 0]
i = 0
for target in dist:
    for crab in crab_position:
        total_cost[i] += progression_sum(abs(target - crab))
    i += 1

print(min(total_cost))
