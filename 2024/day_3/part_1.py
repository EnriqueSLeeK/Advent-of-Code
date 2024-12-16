
import re

total = 0

def mult(arr):
    return arr[0] * arr[1]

with open('input.txt', 'r') as f:
    for line in f:
        found = re.findall(r'mul\(\d+,\d+\)', line)
        for operation in found:
            index_start = operation.find('(')

            # print(operation[4:len(operation) - 1].split(','))
            operand = list(map(int, operation[4:len(operation) - 1].split(',')))
            total += mult(operand)
    print(total)
