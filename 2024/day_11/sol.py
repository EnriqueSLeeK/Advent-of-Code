
from collections import Counter

configuration = []
with open('input.txt', 'r') as f:
# with open('test', 'r') as f:
    configuration = f.read().strip().split()

stone_counter = Counter(configuration)

def stone_magic():
    global stone_counter

    iteration_stone_counter = Counter()
    for stone_number in list(stone_counter.keys()):
        if stone_number == '0':
            iteration_stone_counter['1'] += stone_counter[stone_number]

        elif len(stone_number) % 2 == 0:
            middle = len(stone_number) // 2
            iteration_stone_counter[stone_number[:middle]] += stone_counter[stone_number]
            iteration_stone_counter[str(int(stone_number[middle:]))] += stone_counter[stone_number]

        else:
            new_number = str(int(stone_number) * 2024)
            iteration_stone_counter[new_number] += stone_counter[stone_number]

        stone_counter[stone_number] = 0
    stone_counter = stone_counter + iteration_stone_counter

# for _ in range(25):
for _ in range(75):
    stone_magic()

total_stones = 0
for k in stone_counter:
    total_stones += stone_counter[k]
print(total_stones)
