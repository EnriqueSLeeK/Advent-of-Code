with open("input", "r") as f:
#with open("t", "r") as f:
    lines = f.readlines()

lines = [line.replace('\n', '') for line in lines]
y_max = len(lines)
x_max = len(lines[0])

def check_index(y, x):
    if ( (x > -1 and x < x_max) and
         (y > -1 and y < y_max) ):
        return (int(lines[y][x]))
    return (9)

def find_low(elem, y, x):
    look = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for look_at in look:
        if (elem >=
            check_index(y + look_at[0],
                        x + look_at[1])):
            return
    return([y, x])

low_points = []
for y_index in range(y_max):
    for x_index in range(x_max):
        digit = int(lines[y_index][x_index])
        low = find_low(digit, y_index, x_index)
        if (low == None):
            continue
        else:
            low_points.append(low)

def basin(y, x, visited = []):
    point = [y, x]
    if (point in visited or
        check_index(point[0], point[1]) == 9):
        return (-1)
    visited.append(point)
    return (4 + basin(y + 1, x, visited) +
            basin(y - 1, x, visited) +
            basin(y, x + 1, visited) +
            basin(y, x - 1, visited) )

b = []
for points in low_points:
    b.append(basin(points[0], points[1]) + 1)

def remove_return(val):
    b.remove(val)
    return (val)

tot = 1
for k in range(3):
    tot *= remove_return(max(b))

print(tot)
