from statistics import median

with open("input", "r") as f:
    crab_position = [int(crab) for crab in f.read().split(',')]

crab_position.sort()
good_dist = int(median(crab_position))

tot = 0
for crab in crab_position:
    tot += abs(good_dist - crab)

print(tot)
