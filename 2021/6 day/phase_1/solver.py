with open("input", "r") as f:
    fish = [int(cycle) for list_cycle in f for cycle in list_cycle.split(",")]

for day in range(80):
    for k in range(len(fish)):
        if (fish[k] > 0):
            fish[k] -= 1
        else:
            fish[k] = 6
            fish.append(8)
print(len(fish))
