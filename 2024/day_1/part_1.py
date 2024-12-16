
list_1 = []
list_2 = []

with open('input.txt', 'r') as f:
    for line in f:
        splitted = line.split()

        list_1.append(int(splitted[0]))
        list_2.append(int(splitted[1]))


list_1.sort()
list_2.sort()

total = 0

for m, n in zip(list_1, list_2):
    total += abs(m - n)

print(total)

