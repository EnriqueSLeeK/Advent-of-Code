from collections import defaultdict

with open("input", "r") as f:
    fish = [int(cycle) for list_cycle in f for cycle in list_cycle.split(",")]

days = 256

# Huge thanks to the Advent of 
# code subreddit for the help
def calc():

    born = defaultdict(lambda: 0)

    # First generation
    for day in fish:
        born[day] += 1
    # Calculating the subsequent generations
    for day in range(days):
        born[day] += born[day - 7] + born[day - 9]
    print(sum(born.values()) + len(fish))

calc()
