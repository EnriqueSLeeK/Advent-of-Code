with open("input", "r") as f:
    lines = f.readlines()

lines = [line.replace('\n', '') for line in lines]
y_max = len(lines)
x_max = len(lines[0])

def check_index(y, x):
    if ( (x > -1 and x < x_max) and
         (y > -1 and y < y_max) ):
        return (int(lines[y][x]))
    return (9)

def look_aroud(elem, y, x):
    look = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for look_at in look:
        if (elem >=
            check_index(y + look_at[0],
                        x + look_at[1])):
            return (0)
    return (elem + 1)

danger_level = 0
for y_index in range(y_max):
    for x_index in range(x_max):
        digit = int(lines[y_index][x_index])
        danger_level += look_aroud(digit,
                                   y_index, 
                                   x_index)
print(danger_level)
