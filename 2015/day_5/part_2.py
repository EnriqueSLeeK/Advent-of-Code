
from collections import Counter

lines = []
count = 0

with open('input', 'r') as f:
    for line in f:
        lines.append(line.rstrip())

for line in lines:
    has_pair = any(line[i:i + 2] in line[i + 2:] for i in range(len(line) - 1))
    has_repeat = any(line[i] == line[i + 2] for i in range(len(line) - 2))

    if has_pair and has_repeat:
        count += 1
    
print(count)
