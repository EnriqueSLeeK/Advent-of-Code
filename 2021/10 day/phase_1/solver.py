with open("input", "r") as f:
    lines = f.readlines()

def expected_symbol(symbol):
    if (symbol == "("):
        return (")")
    elif (symbol == "["):
        return ("]")
    elif (symbol == "{"):
        return ("}")
    elif (symbol == "<"):
        return (">")

def corruption_code(symbol):
    if (symbol == ")"):
        return (3)
    elif (symbol == "]"):
        return (57)
    elif (symbol == "}"):
        return (1197)
    elif (symbol == ">"):
        return (25137)
    else:
        return (0)

def check_syntax(line):
    stack = []
    opening_symbol = ['(', '[', '{', '<']
    closing_symbol = [')', ']', '}', '>']
    for symbol in line:
        if (symbol in opening_symbol):
            stack.append(expected_symbol(symbol))
        else:
            if (stack.pop() != symbol):
                return (corruption_code(symbol))
    return (0)

total = 0
for line in lines:
    total += check_syntax(line)
print(total)
