
target = []
components = []

with open('input.txt', 'r') as f:
# with open('test', 'r') as f:
    for line in f:
        splitted = line.split(':')
        target.append(int(splitted[0]))
        components.append(list(map(int,splitted[1].split())))

max_len = -1
final_res = 0

def sum_val(a, b):
    return a + b

def prod_val(a, b):
    return a * b

def operate_comb(curr_target, op, i, accumulate, component_idx):

    global max_len

    if i >= max_len:
        return accumulate == curr_target

    accumulate = op(accumulate, components[component_idx][i])

    return (operate_comb(curr_target, sum_val, i + 1, accumulate, component_idx) or
            operate_comb(curr_target, prod_val, i + 1, accumulate, component_idx))

for i, target in enumerate(target):
    max_len = len(components[i])
    if operate_comb(target, sum_val, 0, 0, i):
        final_res += target

print(final_res)
