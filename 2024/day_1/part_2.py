
from collections import Counter

list_1 = []
list_2 = []

with open('input.txt', 'r') as f:
    for line in f:
        splitted = line.split()

        list_1.append(int(splitted[0]))
        list_2.append(int(splitted[1]))


list_2 = Counter(list_2)


total = 0

for m in list_1:
    total += m * list_2[m]

print(total)

