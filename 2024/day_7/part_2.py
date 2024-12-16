
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

def concat_val(a, b):
    return int(str(a) + str(b))

def operate_comb(curr_target, arr, op, i, accumulate):

    global max_len

    if i >= max_len:
        return accumulate == curr_target

    accumulate = op(accumulate, arr[i])

    return (operate_comb(curr_target, arr, sum_val, i + 1, accumulate) or
            operate_comb(curr_target, arr, prod_val, i + 1, accumulate) or
            operate_comb(curr_target, arr, concat_val, i + 1, accumulate))
    


for i, target in enumerate(target):
    max_len = len(components[i])
    if operate_comb(target, components[i], sum_val, 0, 0):
        final_res += target

print(final_res)
