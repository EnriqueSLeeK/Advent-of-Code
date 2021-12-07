with open("input", "r") as f:
    crab_position = [int(crab) for crab in f.read().split(',')]

max_pos = max(crab_position)
min_pos = min(crab_position)

cost = []

def progression_sum(steps):
    if (steps == 0):
        return (0)
    return ((1 + steps) * steps) // 2

# Naive solver
for target in range(min_pos, max_pos):
    total_cost = 0
    for crab in crab_position:
        total_cost += progression_sum(abs(target - crab))
    cost.append(total_cost)

print(min(cost))
