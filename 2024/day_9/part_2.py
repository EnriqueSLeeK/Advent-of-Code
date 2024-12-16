
from collections import defaultdict

code_data = ""

with open('input.txt', 'r') as f:
# with open('test', 'r') as f:
# with open('a', 'r') as f:
    code_data = f.read().strip()

slots = []
total = sum([int(digit) for digit in code_data])

block_id_size = defaultdict(int)
block_id_end = defaultdict(int)

def make_memory():
    memory = []
    mode = True
    count = 0
    for value_memory in code_data:
        quantity = int(value_memory)
        if mode:
            memory.extend([str(count)] * quantity)
            block_id_size[count] = quantity
            block_id_end[count] = len(memory)
            count += 1
        else:
            memory.extend(['.'] * quantity)
            slots.append(quantity)
        mode ^= True
    return memory

def find_fit_slot(block_id):
    for i in range(len(slots)):

        if i > block_id:
            break

        if slots[i] >= block_id_size[block_id]:
            slots[i] -= block_id_size[block_id]
            return i

    return -1

def clean_block(memory, block_id):
    for i in range(block_id_end[block_id] - 1, -1, -1):
        if memory[i] != str(block_id) or block_id_size[block_id] == 0:
            break
        memory[i] = '.'
        block_id_size[block_id] -= 1


def defrag(memory):

    slot_idx = 0

    block_ids = list(block_id_size.keys())

    block_id_r = max(block_ids)

    code = []
    l = block_id_size[0]

    while block_id_r > 0:
        spot = find_fit_slot(block_id_r)

        if spot != -1:
            l = block_id_end[spot]
            offset = memory[l:].index('.')
            l += offset

            for k in range(block_id_size[block_id_r]):
                memory[l + k] = str(block_id_r)

            clean_block(memory, block_id_r)


        block_id_r -= 1


memory = make_memory()
defrag(memory)

checksum = 0
for i, value in enumerate(memory):
    if value != '.':
        checksum += int(value) * i

print(checksum)

