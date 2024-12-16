
import time

code_data = ""

with open('input.txt', 'r') as f:
# with open('test', 'r') as f:
# with open('a', 'r') as f:
    code_data = f.read().strip()

total = sum([int(digit) for digit in code_data])


def make_memory():
    memory = []
    mode = True
    count = 0
    for value_memory in code_data:
        quantity = int(value_memory)
        if mode:
            memory.extend([str(count)] * quantity)
            count += 1
        else:
            memory.extend(['.'] * quantity)
        mode ^= True
    return memory

def find_mem(memory, r):
    for i in range(r, -1, -1):
        if memory[i] != '.':
            return i
    return r

def defrag(memory):

    l = 0
    r = find_mem(memory, len(memory) - 1)

    while l < r:
        if memory[l] == '.':
            memory[l], memory[r] = memory[r], memory[l]

        r = find_mem(memory, r)
        l += 1

memory = make_memory()
defrag(memory)

total = 0
for i, value in enumerate(memory):
    if value == '.':
        break
    total += int(value) * i

print(total)
