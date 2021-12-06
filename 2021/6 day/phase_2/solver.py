from collections import defaultdict

with open("input", "r") as f:
    fish = [int(cycle) for list_cycle in f for cycle in list_cycle.split(",")]

days = 256

# Huge thanks to reddit:D
def calc():

    born = defaultdict(lambda: 0)

    #Populate the dictionary
    for day in fish:
        born[day] += 1
    #This loop it's in charge of calculating the subsequent offsprings
    for day in range(days):
        born[day] += born[day - 7] + born[day - 9]
    print(sum(born.values()) + len(fish))

calc()
