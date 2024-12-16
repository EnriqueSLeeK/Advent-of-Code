
from collections import defaultdict

page_mapping = defaultdict(list)
page_sequence = []

with open('input.txt', 'r') as f:
# with open('test', 'r') as f:
    paging_section = True
    for line in f:
        if line == '\n':
            paging_section = False
            continue

        if paging_section:
            x, y = list(map(int, line.split('|')))
            page_mapping[x].append(y)
        else:
            page_sequence.append(
                                 # set(
                                 list(
                                      map(int, line.split(','))
                                 )
                             )

middle_sum = 0

# ===== Check ordering =====================================
def check_ahead(sequence, i):
    for k in range(i + 1, len(sequence)):
        if sequence[k] not in page_mapping[sequence[i]]:
            return False
    return True

def check_previous(sequence, i):
    for k in range(i - 1, -1, -1):
        if sequence[i] not in page_mapping[sequence[k]]:
            return False
    return True

def check_elem_order(sequence, i):
    if check_ahead(sequence, i) and check_previous(sequence, i):
        return True
    return False

def check_order(sequence):
    for i in range(len(sequence)):
        if not check_elem_order(sequence, i):
            return False
    return True
# ===== Check ordering =====================================

def fix_order(sequence):
    forward_graph = defaultdict(list)
    for val in sequence:
        forward_graph[val]

    for i in range(len(sequence)):
        key = sequence[i]
        for value in sequence[:i] + sequence[i + 1:]:
            if value in page_mapping[key]:
                forward_graph[key].append(value)
    sorted_sequence = sorted(forward_graph,
                             key=lambda key: len(forward_graph[key]),
                             reverse=True)
    return sorted_sequence

for sequence in page_sequence:
    if not check_order(sequence):
        sequence = fix_order(sequence)
        middle_sum += sequence[len(sequence) // 2]

print(middle_sum)
