
from math import sin, cos, pi

t_map = None

visited = set()

with open('input.txt', 'r') as f:
# with open('test', 'r') as f:
    t_map = f.read().strip().split('\n')

max_x = len(t_map[0])
max_y = len(t_map)
multiplier = 1

def calculate_direction():
    global multiplier
    multiplier = (multiplier + 1) % 4
    radians = pi * multiplier * 0.5
    return tuple(map(int , [sin(radians) * -1, cos(radians)]))

def sum_tuples(t_a, t_b):
    return tuple(a + b for a, b in zip(t_a, t_b))

def check_bound(curr_coord):
    return curr_coord[0] >= max_y or curr_coord[1] >= max_x or \
            curr_coord[0] < 0 or curr_coord[1] < 0

def explore(x, y):

    direction = calculate_direction()
    curr_coord = (x, y)

    while True:

        if curr_coord not in visited:
            visited.add(curr_coord)

        new_coord = sum_tuples(curr_coord, direction)
        if check_bound(new_coord):
            break

        if t_map[new_coord[1]][new_coord[0]] == '#':
            direction = calculate_direction()
        else:
            curr_coord = new_coord

def find_guard():
    y_index = -1
    x_index = -1
    for y, line in enumerate(t_map):
        if '^' in line:
            y_index = y
            x_index = line.index('^')
            break
    return (y_index, x_index)

guard_index = find_guard()

explore(guard_index[1], guard_index[0])

print(len(visited))
for v in visited:
    print(v)
