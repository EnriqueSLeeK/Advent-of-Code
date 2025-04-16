
from collections import defaultdict

operations = []

with open('test', 'r') as f:
# with open('input', 'r') as f:
    for line in f:
        operations.append(line.rstrip().split(' -> '))

vars = defaultdict(int)

def and_gate(var_1, var_2):
    return vars[var_1] & vars[var_2]

def or_gate(var_1, var_2):
    return vars[var_1] | vars[var_2]

def not_gate(var):
    return ~vars[var]

def shift_l(var, offset):
    return vars[var] << offset

def shift_r(var, offset):
    return vars[var] >> offset

for op in operations:
    try:
        value = int(op[0])
        vars[op[1]] = value
    except:
        operation = op[0].split()
        if 'AND' in operation:
            vars[op[1]] = and_gate(operation[0], operation[2])
        elif 'OR' in operation:
            vars[op[1]] = or_gate(operation[0], operation[2])
        elif 'NOT' in operation:
            vars[op[1]] = not_gate(operation[1])
        elif 'LSHIFT' in operation:
            vars[op[1]] = shift_l(operation[0], int(operation[2]))
        elif 'RSHIFT' in operation:
            vars[op[1]] = shift_r(operation[0], int(operation[2]))

# print(vars['a'])
print(vars)

        
