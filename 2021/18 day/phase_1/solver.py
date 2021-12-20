with open("input", "r") as f:
    lines = [line.strip() for line in f.readlines()]

def explode(line):
    for index, ((num, depth), (num_2, depth_2)) in enumerate(
            zip(line, line[1:])):
        if (depth <= 4 or depth != depth_2):
            continue
        if (index > 0):
            line[index - 1][0] += num
        if (index < len(line) - 2):
            line[index + 2][0] += num_2
        return (True, line[:index] +
                [[0, depth - 1]] +
                line[2 + index:])
    return (False, line)

def split(line):
    for index, (num, depth) in enumerate(line):
        if (num < 10):
            continue
        half = num // 2
        floor = half
        ceil = num - half
        return (True, line[:index] +
                [[floor, depth + 1], [ceil, depth + 1]] +
                line[index + 1:]) 
    return (False, line)

def parser(parsed_list):
    for line in lines:
        parsed_line = []
        depth = 0
        for k in line:
            if (k == '['):
                depth += 1
            elif (k == ']'):
                depth -= 1
            elif (k.isdigit()):
                parsed_line.append((int(k), depth))
        parsed_lines.append(parsed_line)

def reducer(initial, index, limit):
    if (index > limit):
        return (initial)
    initial += parsed_lines[index + 1]
    initial = [[num, depth + 1] for num, depth in initial]
    while (True):
        check, initial = explode(initial)
        if (check): continue
        check, initial = split(initial)
        if (not check): break
    return (reducer(initial, index + 1, limit))

def magnitude_calc(snail_number):
    while (len(snail_number) > 1):
        for i, ((num, depth), (num_2, depth_2)) in enumerate(
                zip(snail_number, snail_number[1:])):
            if (depth_2 != depth):
                continue
            val = num * 3 + num_2 * 2
            snail_number = snail_number[:i] + [
                    [val, depth - 1]] + snail_number[i + 2:]
            break
    return (snail_number[0][0])

parsed_lines = []
parser(parsed_lines)
print(magnitude_calc(reducer(parsed_lines[0].copy(),
                          0, len(parsed_lines) - 2)))
