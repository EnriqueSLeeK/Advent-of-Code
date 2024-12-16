with open("input", "r") as f:
    lines = f.readlines()
# Clear line breaks
lines = [line.replace("\n", "") for line in lines]

def expected_symbol(symbol):
    if (symbol == "("):
        return (")")
    elif (symbol == "["):
        return ("]")
    elif (symbol == "{"):
        return ("}")
    elif (symbol == "<"):
        return (">")

def completion_point(stack):
    total_point = 0
    for i in range(len(stack) - 1, -1, -1):
        total_point *= 5
        if (stack[i] == ")"):
            total_point += 1
        elif (stack[i] == "]"):
            total_point += 2
        elif (stack[i] == "}"):
            total_point += 3
        elif (stack[i] == ">"):
            total_point += 4
    return (total_point)

def check_syntax(line):
    stack = []
    opening_symbol = ['(', '[', '{', '<']
    closing_symbol = [')', ']', '}', '>']
    for symbol in line:
        if (symbol in opening_symbol):
            stack.append(expected_symbol(symbol))
        else:
            # Filter corrupted lines
            if (stack.pop() != symbol):
                return (0)
    return (completion_point(stack))

points = []
for line in lines:
    point = check_syntax(line)
    if (point > 0):
        points.append(point)
points.sort()
print(points)
print(points[len(points) // 2])
