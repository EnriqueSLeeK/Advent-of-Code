
import re

total = 0

def mult(arr):
    return arr[0] * arr[1]

with open('input.txt', 'r') as f:
    dont = False
    for line in f:
        found = re.findall(r'mul\(\d+,\d+\)|don\'t\(\)|do\(\)', line)

        for operation in found:

            if operation == 'don\'t()':
                dont = True
            elif operation == 'do()':
                dont = False
            elif not dont:
                index_start = operation.find('(')
                operand = list(map(int, operation[4:len(operation) - 1].split(',')))
                total += mult(operand)

    print(total)
